-- creates table "unique_id" in my server
-- the column 'id' has a default value of '1' and must be unique
CREATE TABLE IF NOT EXISTS unique_id(
        id INT DEFAULT 1 UNIQUE,
        name VARCHAR(256)
);
