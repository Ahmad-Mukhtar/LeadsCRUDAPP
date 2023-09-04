create database leads;
use leads;
CREATE TABLE leadsinfo (
   ID int NOT NULL AUTO_INCREMENT,
    Name varchar(255) NOT NULL,
    Email varchar(255),
    company varchar(255),
    phone varchar(11),
    PRIMARY KEY (ID)
);
