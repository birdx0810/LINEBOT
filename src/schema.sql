CREATE TABLE `users` (
	`user_id` INT NOT NULL AUTO_INCREMENT,
	`user_name` VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT '',
	PRIMARY KEY (`user_id`)
) ENGINE=InnoDB;

CREATE TABLE `logs` (
	`log_id` INT NOT NULL AUTO_INCREMENT,
	`user_id` INT(255) DEFAULT '',
	`log_content` VARCHAR CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '',
    `log_direction` BOOLEAN NOT NULL DEFAULT NULL,
	PRIMARY KEY (`log_id`)
    FOREIGN KEY (`user_id`) REFERENCES users(`user_id`)
) ENGINE=InnoDB;