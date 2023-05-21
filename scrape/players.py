import pandas as pd
import sqlite3

url = 'http://fesashogi.eu/index.php?mid=5'

data = pd.read_html(url)
conn = sqlite3.connect('shogi.db')
data[0].to_sql('players', conn, if_exists='replace', index=False)
conn.close()

conn = sqlite3.connect('shogi.db')
cursor = conn.cursor()
cursor.execute("ALTER TABLE players RENAME COLUMN '0' TO id")
cursor.execute("ALTER TABLE players RENAME COLUMN '1' TO surname")
cursor.execute("ALTER TABLE players RENAME COLUMN '2' TO firstname")
cursor.execute("ALTER TABLE players RENAME COLUMN '3' TO eGrade")
cursor.execute("ALTER TABLE players RENAME COLUMN '4' TO jGrade")
cursor.execute("ALTER TABLE players RENAME COLUMN '5' TO ELO")
cursor.execute("ALTER TABLE players RENAME COLUMN '6' TO Games")
cursor.execute("ALTER TABLE players RENAME COLUMN '7' TO Nationality")
cursor.execute("DELETE FROM players WHERE id == surname ")

conn.commit()
conn.close()

conn = sqlite3.connect('shogi.db')
cursor = conn.cursor()
cursor.execute("DELETE FROM players WHERE id IS NULL")
conn.commit()
conn.close()