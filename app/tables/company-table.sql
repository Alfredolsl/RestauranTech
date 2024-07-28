USE `RestauranTech`;

CREATE TABLE IF NOT EXISTS `company` (
    `company_id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(64) NOT NULL,
    `RFC` VARCHAR(256) NOT NULL,
    `fiscal_address` VARCHAR(256) NOT NULL,
    PRIMARY KEY (`company_id`)
);