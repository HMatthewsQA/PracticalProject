use tickets_db;
CREATE TABLE IF NOT EXISTS tickets(
	id INTEGER NOT NULL AUTO_INCREMENT,
	letterstring VARCHAR(100) NOT NULL,
	primeno INTEGER NOT NULL,
	win BOOLEAN,
	PRIMARY KEY(id)
	);