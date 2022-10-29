import random
import string


def generate_auth_pair(number: int) -> list: #Number of requaried quantity of pairs
    pairs_list = []
    characters = string.ascii_letters + string.digits + string.punctuation
    for _ in range(number):
        result_str = ''.join(random.choice(string.ascii_letters) for _ in range(12))
        password = ''.join(random.choice(characters) for _ in range(10))
        pairs_list.append((result_str, password))
    return pairs_list


