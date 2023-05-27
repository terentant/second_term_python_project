import sqlite3

conn = sqlite3.connect('shogi.db')
cursor = conn.cursor()
cursor.execute('SELECT surname, firstname FROM players')
i = 0
for name in cursor.fetchall():
    i += 1
    if i % 100 == 0:
        print(i)
    cur_alter = conn.cursor()
    tablename = name[1] + '_' + name[0]
    try:
        cursor.execute("ALTER TABLE " + tablename + "_tournaments RENAME COLUMN '0' TO Event")
        cursor.execute("ALTER TABLE " + tablename + "_tournaments RENAME COLUMN '1' TO Date")
        cursor.execute("ALTER TABLE " + tablename + "_tournaments RENAME COLUMN '2' TO Elo")
        cursor.execute("ALTER TABLE " + tablename + "_tournaments RENAME COLUMN '3' TO Shift")
        cursor.execute("ALTER TABLE " + tablename + "_tournaments RENAME COLUMN '4' TO Rank")
        cursor.execute("ALTER TABLE " + tablename + "_tournaments RENAME COLUMN '5' TO Games")
        cursor.execute("ALTER TABLE " + tablename + "_tournaments RENAME COLUMN '6' TO Promotes_to")
        cursor.execute("DELETE FROM " + tablename + "_tournaments WHERE Event == Date")
        cursor.execute("DELETE FROM " + tablename + "_tournaments WHERE Event == 'Event'")
    except:
        print("exception")
conn.commit()
conn.close()
