db = DatabaseManager("moje.db")

# Vytvoření tabulky
db.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")

# Vložení dat
db.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))
