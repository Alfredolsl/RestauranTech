USE `RestauranTech`;

CREATE TABLE `footprint` (
    `footprint_id` INT NOT NULL AUTO_INCREMENT,
    `asset_id` INT NOT NULL,
    `footprint_name` VARCHAR(64) NOT NULL,
    `description` VARCHAR(512) NOT NULL,
    `picture` VARCHAR(2048)NOT NULL,
    `conversion` VARCHAR(16) NOT NULL,
    PRIMARY KEY (`footprint_id`),
    FOREIGN KEY (`asset_id`) REFERENCES `assets`(`asset_id`)
);