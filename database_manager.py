import sqlite3

class DatabaseManager:
    def __init__(self, db_path):
        self.db_path = db_path

    def execute(self, query, params=None, fetch=False, fetchone=False):
        if params is None:
            params = ()
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            result = None
            if fetchone:
                result = cursor.fetchone()
            elif fetch:
                result = cursor.fetchall()
            return result

#    def execute_many(self, query, param_list):
#        with sqlite3.connect(self.db_path) as conn:
#            cursor = conn.cursor()
#            cursor.executemany(query, param_list)

#    def execute_script(self, script):
#        with sqlite3.connect(self.db_path) as conn:
#            cursor = conn.cursor()
#            cursor.executescript(script)
