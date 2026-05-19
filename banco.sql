CREATE DATABASE hotelaria_2;
-- ----------------------------------------------------------------
USE hotelaria_2;
-- ----------------------------------------------------------------
CREATE TABLE hospedes (
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR (100) NOT NULL,
    email VARCHAR (100) NULL,
    telefone VARCHAR (20) NULL,
    cpf VARCHAR (14) UNIQUE
);

INSERT INTO hospedes (nome, email, telefone, cpf)
VALUES (
    'Matheus',
    'matheus.catarucci7@gmail.com',
    '(19)9 99874-2782',
    '15505218458'
);
