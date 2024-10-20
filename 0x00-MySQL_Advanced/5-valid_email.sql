-- SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.

DELIMITER $$
CREATE TRIGGER ResetValidEmailAttribute
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    -- Check if email has changed
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END$$

DELIMITER ;