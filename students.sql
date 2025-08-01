create database StudentsDB;
GO

use StudentsDB;
GO

create table Students (
    ID int primary key,
    Name nvarchar(100),
    Email nvarchar(100),
    Age int,
    Gender nvarchar(10),
    Course nvarchar(100)
);

select * from Students;
--update
alter table students add constraint Email unique(email);
-- i forgot to declare that emails are unique
