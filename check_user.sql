 id    | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| email | varchar(255)     | YES  | UNI | NULL    |                |
| pswd  | varchar(255)     | YES  |     | NULL    |                |
| token | tinyint(1) 

DELIMITER //
CREATE PROCEDURE check_user(p text, e text) 
BEGIN
 select tiny from check_user wher
 
END //
DELIMITER;
