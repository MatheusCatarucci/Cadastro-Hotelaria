CREATE DATABASE hotelaria;
-- ----------------------------------------------------------------
USE hotelaria;
-- ----------------------------------------------------------------
CREATE TABLE hospedes (
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR (100) NOT NULL,
    email VARCHAR (100) NULL,
    telefone VARCHAR (20) NULL,
    cpf VARCHAR (14) UNIQUE
);