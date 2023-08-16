-- creates a database "hbtn_0d_usa" and a table "states" within it
-- id is unique, auto generated and cant be NULL and is also a primary key
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
        id INT NOT NULL UNIQUE AUTO_INCREMENT,
        name VARCHAR(256) NOT NULL
);
