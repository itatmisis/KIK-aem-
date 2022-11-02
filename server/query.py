insert_user = "INSERT INTO users (login, password, is_admin, is_super) VALUES ('%s', '%s', %s, %s)"
select_salt = "SELECT salt FROM users WHERE login = '%s'"
select_user = "SELECT COUNT() FROM users WHERE login = '%s' and password = '%s'"
get_pass = "SELECT password FROM users WHERE login = %s"

