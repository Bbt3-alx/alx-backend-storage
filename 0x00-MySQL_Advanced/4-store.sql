--  SQL script that creates a trigger that decreases the quantity of an item after adding a new order.

DELIMITER $$
CREATE TRIGGER decrease_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    -- Decrease the quantity of the item after an order is placed
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END;

DELIMITER ;