import random
import string
from database import DB
import bcrypt

def generate_auth_pair(db: DB, number: int, is_super: bool) -> dict: #Number of requaried quantity of pairs
    pairs_list = dict()
    is_admin = False
    characters = string.ascii_letters + string.digits
    for _ in range(number):
        salt = bcrypt.gensalt(12)
        login = ''.join(random.choice(string.ascii_letters) for _ in range(12))
        password = ''.join(random.choice(characters) for _ in range(10))
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
        pairs_list[login] = password
        db.insert_user(login, hashed_password, is_super, is_admin)
    return pairs_list


