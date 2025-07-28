create database StudentsDB;
GO

use StudentsDB;
GO

CREATE TABLE Students (
    ID INT PRIMARY KEY,
    Name NVARCHAR(100),
    Email NVARCHAR(100),
    Age INT,
    Gender NVARCHAR(10),
    Course NVARCHAR(100)
);

select * from Students;