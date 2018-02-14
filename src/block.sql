BEGIN TRANSACTION;
CREATE TABLE `previous_hash` (
	`hash`	TEXT
);

CREATE TABLE `transactions` (
  `id`	INTEGER PRIMARY KEY AUTO_INCREMENT,
  `address_entity`	TEXT,
  `address_user`	  TEXT,
  `reputation`   INTEGER,
  `tt`	         INTEGER,
  `event_code`	 INTEGER,
  `timestamp`	      TIMESTAMP NOT NULL,
  `gps`	            TEXT,
  `hash`	          TEXT,
  `transactionHash`	TEXT
);

CREATE TABLE `hash_current_block` (
	`hash`	TEXT
);
COMMIT;
