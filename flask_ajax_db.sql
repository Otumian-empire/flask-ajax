BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `info` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`firstname`	TEXT,
	`lastname`	TEXT
);
COMMIT;
