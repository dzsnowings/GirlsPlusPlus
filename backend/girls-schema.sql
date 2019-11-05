drop database if exists girls;
create database girls;
use girls;

create table members (
    ID int(10) primary key,
    name varchar(255),
    email varchar(255),
    major varchar(255),
    gender varchar(255),
    class varchar(255),
    why varchar(1000)
);
