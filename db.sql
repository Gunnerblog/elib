
-- Table: books
CREATE TABLE books ( 
    id    INTEGER         NOT NULL,
    title VARCHAR( 100 ),
    PRIMARY KEY ( id ),
    UNIQUE ( title ) 
);

INSERT INTO [books] ([id], [title]) VALUES (2, 'A Christmas Carol ');
INSERT INTO [books] ([id], [title]) VALUES (5, 'Alice''s Adventures in Wonderland ');
INSERT INTO [books] ([id], [title]) VALUES (1, 'Animal Farm');
INSERT INTO [books] ([id], [title]) VALUES (7, 'Django');
INSERT INTO [books] ([id], [title]) VALUES (4, 'Great Expectations ');
INSERT INTO [books] ([id], [title]) VALUES (10, 'Harry Potter and the Goblet of Fire');
INSERT INTO [books] ([id], [title]) VALUES (11, 'Harry Potter and the Philosopher''s Stone');
INSERT INTO [books] ([id], [title]) VALUES (13, 'Persuasion');
INSERT INTO [books] ([id], [title]) VALUES (12, 'Tess of the d''Urbervilles');
INSERT INTO [books] ([id], [title]) VALUES (8, 'The Godfather');
INSERT INTO [books] ([id], [title]) VALUES (9, 'The Green Mile');
INSERT INTO [books] ([id], [title]) VALUES (6, 'The Hobbit');
INSERT INTO [books] ([id], [title]) VALUES (3, 'The Pickwick Papers');
INSERT INTO [books] ([id], [title]) VALUES (14, 'The Python Language Reference Manual ');

-- Table: authors
CREATE TABLE authors ( 
    id   INTEGER        NOT NULL,
    name VARCHAR( 50 ),
    PRIMARY KEY ( id ),
    UNIQUE ( name ) 
);

INSERT INTO [authors] ([id], [name]) VALUES (11, 'Adrian Holovaty');
INSERT INTO [authors] ([id], [name]) VALUES (2, 'Charles Dickens');
INSERT INTO [authors] ([id], [name]) VALUES (15, 'Dave Brueck');
INSERT INTO [authors] ([id], [name]) VALUES (14, 'Fred L. Drake');
INSERT INTO [authors] ([id], [name]) VALUES (1, 'George Orwell');
INSERT INTO [authors] ([id], [name]) VALUES (13, 'Guido van Rossum');
INSERT INTO [authors] ([id], [name]) VALUES (6, 'Irvine Welsh');
INSERT INTO [authors] ([id], [name]) VALUES (9, 'J. K. Rowling');
INSERT INTO [authors] ([id], [name]) VALUES (4, 'J. R. R. Tolkien');
INSERT INTO [authors] ([id], [name]) VALUES (12, 'Jacob Kaplan-Moss');
INSERT INTO [authors] ([id], [name]) VALUES (8, 'Jane Austen');
INSERT INTO [authors] ([id], [name]) VALUES (3, 'Lewis Carroll');
INSERT INTO [authors] ([id], [name]) VALUES (5, 'Mario Puzo');
INSERT INTO [authors] ([id], [name]) VALUES (7, 'Stephen King');
INSERT INTO [authors] ([id], [name]) VALUES (16, 'Stephen Tanner ');
INSERT INTO [authors] ([id], [name]) VALUES (10, 'Thomas Hardy');

-- Table: association
CREATE TABLE association ( 
    book_id   INTEGER,
    author_id INTEGER,
    FOREIGN KEY ( book_id ) REFERENCES books ( id ),
    FOREIGN KEY ( author_id ) REFERENCES authors ( id ) 
);

INSERT INTO [association] ([book_id], [author_id]) VALUES (1, 1);
INSERT INTO [association] ([book_id], [author_id]) VALUES (2, 2);
INSERT INTO [association] ([book_id], [author_id]) VALUES (3, 2);
INSERT INTO [association] ([book_id], [author_id]) VALUES (4, 2);
INSERT INTO [association] ([book_id], [author_id]) VALUES (5, 3);
INSERT INTO [association] ([book_id], [author_id]) VALUES (6, 4);
INSERT INTO [association] ([book_id], [author_id]) VALUES (7, 11);
INSERT INTO [association] ([book_id], [author_id]) VALUES (7, 12);
INSERT INTO [association] ([book_id], [author_id]) VALUES (8, 5);
INSERT INTO [association] ([book_id], [author_id]) VALUES (9, 7);
INSERT INTO [association] ([book_id], [author_id]) VALUES (10, 9);
INSERT INTO [association] ([book_id], [author_id]) VALUES (11, 9);
INSERT INTO [association] ([book_id], [author_id]) VALUES (12, 10);
INSERT INTO [association] ([book_id], [author_id]) VALUES (13, 8);
INSERT INTO [association] ([book_id], [author_id]) VALUES (14, 13);
INSERT INTO [association] ([book_id], [author_id]) VALUES (14, 14);
INSERT INTO [association] ([book_id], [author_id]) VALUES (14, 15);
INSERT INTO [association] ([book_id], [author_id]) VALUES (14, 16);

-- Table: users
CREATE TABLE users ( 
    id       INTEGER         NOT NULL,
    name     VARCHAR( 50 ),
    email    VARCHAR( 120 ),
    password VARCHAR( 16 ),
    is_staff BOOLEAN,
    PRIMARY KEY ( id ),
    UNIQUE ( name ),
    UNIQUE ( email ),
    CHECK ( is_staff IN ( 0, 1 )  ) 
);

INSERT INTO [users] ([id], [name], [email], [password], [is_staff]) VALUES (1, 'user', 'user@i.ua', 12344321, 1);
INSERT INTO [users] ([id], [name], [email], [password], [is_staff]) VALUES (2, 'testuser', 'testuser@gmail.com', 12344321, 0);
INSERT INTO [users] ([id], [name], [email], [password], [is_staff]) VALUES (3, 'testuser2', 'testuser2@gmail.com', 12344321, 0);
INSERT INTO [users] ([id], [name], [email], [password], [is_staff]) VALUES (4, 'testuser3', 'testuser3@gmail.com', 12344321, 0);
