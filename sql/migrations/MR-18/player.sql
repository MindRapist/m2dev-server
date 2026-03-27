-- MR-18: Guild comment player name update

ALTER TABLE `guild_comment` MODIFY COLUMN `name`    varchar(24)  DEFAULT NULL;
