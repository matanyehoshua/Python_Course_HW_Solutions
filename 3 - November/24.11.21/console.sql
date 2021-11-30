--create table students and its fields
CREATE TABLE STUDENTS
( ID INTEGER PRIMARY KEY,
 NAME TEXT,
 CITY TEXT,
 BIRTH INTEGER );

--create table grade and its fields
CREATE TABLE GRADE
( ID INTEGER PRIMARY KEY,
 GRADE INTEGER );

--inserting values into the table STUDENTS
INSERT INTO STUDENTS (ID, NAME, CITY, BIRTH)
VALUES (1, 'SHALOM', 'TEL AVIV', 1974);
INSERT INTO STUDENTS (ID, NAME, CITY, BIRTH)
VALUES (2, 'YURI', 'RAANANA', 1980);
INSERT INTO STUDENTS (ID, NAME, CITY, BIRTH)
VALUES (3, 'ANAT', 'RISHON', 1994);
INSERT INTO STUDENTS (ID, NAME, CITY, BIRTH)
VALUES (4, 'DANA', 'REHOVOT', 1990);
INSERT INTO STUDENTS (ID, NAME, CITY, BIRTH)
VALUES (5, 'OMER', 'JERUSALEM', 1987);

--inserting values into the table GRADE
INSERT INTO GRADE (ID, GRADE)
VALUES (1, 95);
INSERT INTO GRADE (ID, GRADE)
VALUES (2, 70);
INSERT INTO GRADE (ID, GRADE)
VALUES (3, 85);
INSERT INTO GRADE (ID, GRADE)
VALUES (4, 99);
INSERT INTO GRADE (ID, GRADE)
VALUES (5, 91);

--showing every student and every grade that each student got
SELECT * FROM GRADE;

--showing the avg of the entire class
SELECT AVG(GRADE) FROM GRADE

--adding a column named 'EXCELLENT'
ALTER TABLE GRADE
ADD EXCELLENT TEXT;
--updating the table where the grade is more than 90, 'EXCELLENT' will get a 'YES'
UPDATE GRADE
SET EXCELLENT = 'YES'
WHERE GRADE > 90;
--updating the table where the grade is less than 90, 'EXCELLENT' will get a 'NO'
UPDATE GRADE
SET EXCELLENT = 'NO'
WHERE GRADE < 90;