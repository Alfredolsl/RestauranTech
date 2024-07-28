USE `RestauranTech`;

CREATE TABLE IF NOT EXISTS `role` (
    `role_id` INT NOT NULL AUTO_INCREMENT,
    `role_name` VARCHAR(128),
    `place_order_allowed` BOOLEAN NOT NULL  DEFAULT 1,
    `count_inventory_allowed` BOOLEAN NOT NULL DEFAULT 1,
    `adjust_inventory_allowed` BOOLEAN NOT NULL DEFAULT 1,
    `accept_adjustments_allowed` BOOLEAN NOT NULL DEFAULT 1,
    PRIMARY KEY (`role_id`)
);