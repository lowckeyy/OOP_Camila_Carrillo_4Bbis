CREATE TABLE login_system_db.users (
	id int NOT NULL,
	username varchar NOT NULL,
	pass varchar NOT NULL,
	nombre varchar NOT NULL,
	CONSTRAINT users_pk PRIMARY KEY (id)
);

INSERT INTO users (id, username, pass, nombre) 
VALUES (1, 'Key', '123', 'Keilany');