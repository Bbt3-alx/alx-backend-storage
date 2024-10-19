--  SQL script that creates a trigger that decreases the quantity of an item after adding a new order.

CREATE TRIGGER decrease_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    nb_order = NEW.number
    items - nb_order
END;