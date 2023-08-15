-- converts a database, table and a specific row to utf-8
-- it also updates the collates
ALTER DATABASE hbtn_0c_0 TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY name TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
