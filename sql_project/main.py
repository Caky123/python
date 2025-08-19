from database_manager import DatabaseManager

db = DatabaseManager("my_database.db")

db.add_user("Alice", 25)
db.add_user("Bob", 30)

users = db.get_users()
for user in users:
    print(user)

db.close()
