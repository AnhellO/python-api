import sqlite3, os, random

DATABASE = os.getenv('DB')
random.seed(os.getenv('SEED'))

conn = sqlite3.connect(DATABASE)
print("Opened database successfully")

conn.execute('CREATE TABLE members (id INTEGER NOT NULL PRIMARY KEY, deductible INTEGER, stop_loss INTEGER, oop_max INTEGER)')
print("Table created successfully")

for i in range(1, 3):
    conn.execute(
        'INSERT INTO members (id, deductible, stop_loss, oop_max) VALUES (?, ?, ?, ?)',
        (
            i,
            random.choice([1000, 2000, 3000, 4000, 5000, 9999]),
            random.choice([10000, 20000, 30000, 40000, 50000, 99999]),
            random.choice([6000, 7000, 8000, 9000, 9997, 9998])
        )
    )

conn.commit()
print("Inserted some records successfully")

conn.close()