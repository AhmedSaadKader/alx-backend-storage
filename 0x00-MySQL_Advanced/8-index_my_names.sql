-- Creates an index idx_name_first on the table names and the first
-- letter of name
DELIMITER $$ ;
DROP INDEX IF EXISTS idx_name_first;
CREATE INDEX IF NOT EXISTS idx_name_first ON names (name(1));
