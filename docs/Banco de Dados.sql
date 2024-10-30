CREATE DATABASE gerenciamento_tarefas;
USE gerenciamento_tarefas;


CREATE TABLE `usuario` (
	`id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`nome` VARCHAR(255) NOT NULL,
	`email` VARCHAR(255) NOT NULL,
	PRIMARY KEY(`id`)
);


CREATE TABLE `tarefa` (
	`id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`id_usuario` INTEGER NOT NULL,
	`nome_setor` VARCHAR(255) NOT NULL,
	`descricao` TEXT(65535) NOT NULL,
	`prioridade` ENUM('BAIXA', 'MEDIA', 'ALTA') NOT NULL,
	`status` ENUM('FAZER', 'FAZENDO', 'PRONTO') NOT NULL,
	`data_cadastro` DATETIME NOT NULL,
	PRIMARY KEY(`id`),
    FOREIGN KEY (`id_usuario`) REFERENCES `usuario`(`id`)
    ON UPDATE NO ACTION ON DELETE NO ACTION
);
