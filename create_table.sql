CREATE DATABASE IF NOT EXISTS quiz_game;

USE quiz_game;

CREATE TABLE scores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    score INT
);
