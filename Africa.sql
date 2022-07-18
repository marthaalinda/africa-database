CREATE TABLE `Location` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `country_name` text,
  `language` text
);

CREATE TABLE `Status` (
  `id` int PRIMARY KEY,
  `population` int,
  `income_group` text
);

CREATE TABLE `location_Status` (
  `location_id` int,
  `status_id` int,
  `independence` int
);

ALTER TABLE `location_Status` ADD FOREIGN KEY (`location_id`) REFERENCES `Location` (`id`);

ALTER TABLE `location_Status` ADD FOREIGN KEY (`status_id`) REFERENCES `Status` (`id`);
