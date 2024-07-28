USE `RestauranTech`;

CREATE TABLE IF NOT EXISTS `branch` (
    `branch_id` INT NOT NULL AUTO_INCREMENT,
    `company_id` INT NOT NULL,
    `name` VARCHAR(64) NOT NULL,
    `address` VARCHAR(256) NOT NULL,
    `fiscal_address` VARCHAR(256) NOT NULL,
    PRIMARY KEY (`branch_id`),
    FOREIGN KEY (`company_id`) REFERENCES `company`(`company_id`)
);