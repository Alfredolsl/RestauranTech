USE `RestauranTech`;

CREATE TABLE IF NOT EXISTS `__supplier` (
    `supplier_id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(128) NOT NULL,
    `api_key` VARCHAR(2048) NOT NULL,
    PRIMARY KEY (`supplier_id`)
);