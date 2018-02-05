BEGIN wallet;
CREATE TABLE `wallets` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`privateKey`	TEXT,
	`publicKey`	TEXT,
	`address`	TEXT
);
COMMIT;
