import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import bcrypt
import query
import models

class DB:
    def __init__(self, db_creds: dict) -> None:
        try:
            self.connection = psycopg2.connect(
                host=db_creds['host'],
                user=db_creds['user'],
                password=db_creds['password'],
                database=db_creds['db']
            )
            self.cur = self.connection.cursor()
            self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        except Exception as ex:
            print(ex)
    
    def get_user(self, login: str) -> tuple:      
        self.cur.execute(query.get_user%login)
        user_information: list = self.cur.fetchall()
        if len(user_information) == 0:
            return None
        return user_information[0]

    def check_user(self, login: str, password: str) -> models.AuthorizationResult:
        user_information: tuple = self.get_user(login)
        result = models.AuthorizationResult()
        if user_information is None:
            return result
        hashed_password, is_super, is_admin = user_information
        result.is_super = is_super
        result.is_admin = is_admin
        result.is_ok = bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
        return result

    def insert_user(self, login: str, password: str, is_admin: bool, is_super: bool) -> None:
        self.cur.execute(query.insert_user%(login, password, is_admin, is_super))

    def get_stats(self, product, direction, start, end) -> dict:
        total_stats = []
        self.cur.execute(query.get_stats%(product, direction, start, end))
        for position in self.cur.fetchall():
            product_code, operation_date, avg_cost, name = position
            total_stats.append(
                        {
                            'product_code': product_code,
                            'operation_date': operation_date.strftime('%d-%Y'),
                            'avg_cost': float(avg_cost),
                            'name': name
                        }
                    )
        return {'stats': total_stats}

    def get_recs(self) -> dict:
        total_recs = []
        self.cur.execute('select * from recs')
        for position in self.cur.fetchall():
            _, product_code, name, recs_type = position
            total_recs.append(
                        {
                            'product_code': product_code,
                            'name': name,
                            'recs_type': recs_type
                        }
                    )
        return {'stats': total_recs}



if __name__ == '__main__':
    from os import getenv
    from dotenv import load_dotenv
    load_dotenv()
    db_creds = {"user": getenv("LCT_PG_USER"),
                "password": getenv("LCT_PG_PASSWD"),
                "host": getenv("LCT_PG_HOST"),
                "db": getenv("LCT_PG_DB")}
    db = DB(db_creds) 
    print(db.check_user('admin', 'admin'))
