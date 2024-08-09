-- SQL scrip that creates a stored procedure AddBonuse that adds a
-- new correction for a student
DELIMITER $$ ;
DROP PROCEDURE IF EXISTS AddBonus;
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score FLOAT)
BEGIN
  DECLARE project_id INT;
  IF NOT EXISTS(SELECT id FROM projects WHERE name LIKE project_name)
    THEN
      INSERT INTO projects (name) VALUES (project_name);
    END IF;
  SELECT id INTO project_id FROM projects WHERE name LIKE project_name;
  INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score); 
END
