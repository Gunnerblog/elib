from sqlalchemy import Column, Integer, String, Boolean, Table, ForeignKey
from sqlalchemy.orm import relationship

from database import Base
from database import db_session

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable = False)
    email = Column(String(120), unique=True, nullable = False)
    password = Column(String(16), nullable = False)
    is_staff = Column(Boolean)

    def __init__(self, name=None, email=None, password=None, is_staff = False):
        self.name = name
        self.email = email
        self.is_staff = is_staff
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.name)

    def create(self, username, email, password):
        user = User(username, email, password)
        db_session.add(user)
        db_session.commit()

        return user

    def get(self, username):
        user = User.query.filter(User.name == username).first()
        return user

    def authentication(self, email, password):
        user = User.query.filter(User.email == email, User.password == password).first()
        return user


association_table = Table('association', Base.metadata,
    Column('book_id', Integer, ForeignKey('books.id')),
    Column('author_id', Integer, ForeignKey('authors.id'))
)

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), unique=True, nullable = False)
    authors = relationship("Author",
                    secondary=association_table)

    def __init__(self, title=None):
        self.title = title

    def __repr__(self):
        return '<Book %r>' % (self.title)

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable = False)

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<Author %r>' % (self.name)

    def __str__(self):
        return self.name


class Search():

    def __init__(self, search_query):
        self.search_query = search_query

    def get_result(self):
            books = db_session.query(Book).join(Book.authors).filter(Author.name == self.search_query).subquery()
            authors_results = db_session.query(Book, Author).join(Book.authors, books)

            books = db_session.query(Book).filter(Book.title == self.search_query)
            books_results = db_session.query(Book, Author).join(Book.authors, books)
            all_results = list(authors_results) + list(books_results)

            result_dict = {}
            #create keys in dict
            for item in all_results:
                if item[0] not in result_dict:
                    result_dict[item[0]] = []

            for item in all_results:
                result_dict[item[0]].append(item[1])

            return result_dict
