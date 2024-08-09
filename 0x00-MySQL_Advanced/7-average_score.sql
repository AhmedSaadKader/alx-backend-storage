-- Creates a storder procedure ComputeAverageScoreForUser that computes
-- and store the average score for a student.
DELIMITER $$ ;
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
UPDATE users
  SET average_score=(SELECT AVG(score) FROM corrections AS C WHERE C.user_id LIKE user_id)
  WHERE id LIKE user_id;
