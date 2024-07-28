USE `RestauranTech`;

CREATE TABLE IF NOT EXISTS `order` (
    `order_id` INT NOT NULL AUTO_INCREMENT,
    `branch_id` INT NOT NULL,
    `user_id` INT NOT NULL,
    `supplier_id` INT NOT NULL,
    `order_date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `total_price` DOUBLE NOT NULL,
    `expected_delivery_date` DATE NOT NULL,
    PRIMARY KEY (`order_id`),
    FOREIGN KEY (`branch_id`) REFERENCES `branch`(`branch_id`),
    FOREIGN KEY (`user_id`) REFERENCES `user`(`user_id`),
    FOREIGN KEY (`supplier_id`) REFERENCES `__supplier`(`supplier_id`)
);