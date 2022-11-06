insert_user = "INSERT INTO users (login, password, is_admin, is_super) VALUES ('%s', '%s', %s, %s)"

get_user = "SELECT password, is_super, is_admin FROM users WHERE login = '%s'"

get_stats = '''select product_code, operation_date, avg_cost, name from stats 
where product_code = '%s' AND 
direction = '%s' AND 
operation_date >= date('01-%s') AND 
date('01-%s') >= operation_date 
LIMIT(100)''' # Ограничения на хостинге не позволяются больше(
