BEGIN TRANSACTION;
CREATE TABLE produtos (
	id INTEGER NOT NULL, 
	nome VARCHAR NOT NULL, 
	codigo VARCHAR NOT NULL, 
	preco FLOAT NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (codigo)
);
INSERT INTO "produtos" VALUES(1,'Produto Teste SmartCheckout','7894900011517',10.99);
INSERT INTO "produtos" VALUES(2,'Produto GTIN-8 Teste','96385074',5.99);
INSERT INTO "produtos" VALUES(3,'Produto GTIN-12 Teste','036000291452',7.99);
INSERT INTO "produtos" VALUES(4,'Produto GTIN-14 Teste','10614141000415',12.99);
COMMIT;