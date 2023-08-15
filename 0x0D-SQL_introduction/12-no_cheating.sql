-- updates a certain row in "second_table"
-- only the name field can be used to specify which row to update
UPDATE second_table
SET score = 10
WHERE name = "Bob";
