BEGIN TRANSACTION;
CREATE TABLE `previous_hash` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	`hash`	TEXT
);

CREATE TABLE `transactions` (
  `id`	INTEGER NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  `address_entity`	TEXT,
  `address_user`	  TEXT,
  `reputation`   INTEGER,
  `tt`	         INTEGER,
  `event_code`	 INTEGER,
  `timestamp`	      TEXT,
  `gps`	            TEXT,
  `hash`	          TEXT,
  `transactionHash`	TEXT
);

CREATE TABLE `hash_current_block` (
	`id`	INTEGER NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`hash`	TEXT
);
COMMIT;
