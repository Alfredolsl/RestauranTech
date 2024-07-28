USE `RestauranTech`;

CREATE TABLE IF NOT EXISTS `inventory` (
    `branch_id` INT NOT NULL,
    `asset_id` INT NOT NULL,
    `quantity_in_stock` DOUBLE NOT NULL,
    `unit_of_measure` VARCHAR(16) NOT NULL,
    `average_price` DOUBLE NOT NULL,
    `shelf_life` INT NOT NULL,
    `shelf_life_unit` varchar(64) NOT NULL,
    `user_id` INT NOT NULL,
    PRIMARY KEY (`branch_id`, `asset_id`),
    FOREIGN KEY (`branch_id`) REFERENCES `branch`(`branch_id`),
    FOREIGN KEY (`asset_id`) REFERENCES `assets`(`asset_id`)
);