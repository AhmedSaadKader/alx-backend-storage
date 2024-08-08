-- SQL script that creates a trigger that resets the attribute
-- valid_email only when the email has been changed
CREATE TRIGGER validate_email AFTER UPDATE ON users
FOR EACH ROW
BEGIN
  IF NEW.email != OLD.email THEN
    SET NEW.valid_ = 0;
  END IF;
END;
