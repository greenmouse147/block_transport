BEGIN TRANSACTION;
CREATE TABLE "hash_inital" (
	`hash`	TEXT
);

CREATE TABLE "transactions" (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`address_entity`	TEXT,
  `address_user`	  TEXT,
  `reputation`   INTEGER,
  `tt`	         INTEGER,
  `event_code`	 INTEGER,
  `timestamp`	      TEXT,
  `gps`	            TEXT,
  `hash`	          TEXT,
  `transactionHash`	TEXT,
);

CREATE TABLE `confirmations` (
	`hash`	TEXT,
);
COMMIT;
