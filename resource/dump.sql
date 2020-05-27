BEGIN TRANSACTION;
CREATE TABLE users(id INTEGER PRIMARY KEY,   username text, email text, phone text, website text, residate text);
INSERT INTO "users" VALUES(1,'Jeong','totkfa789@gmail.com','010-0000-0000','Jeong.com','2020-05-13 11:32:19');
INSERT INTO "users" VALUES(2,'Park','Park@gmail.com','010-1111-1111','Park.com','2020-05-13 11:32:19');
INSERT INTO "users" VALUES(3,'Lee','leenave.com','010-2222-2222','Lee.com','2020-05-13 11:32:19');
INSERT INTO "users" VALUES(4,'Cho','Cho@.com','010-3333-3333','Cho.com','2020-05-13 11:32:19');
INSERT INTO "users" VALUES(5,'Yoo','You@.com','010-4444-4444','You.com','2020-05-13 11:32:19');
COMMIT;
