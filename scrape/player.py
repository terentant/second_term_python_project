import pandas as pd
import sqlite3


def player_url(surname, name):
    return 'http://fesashogi.eu/index.php?mid=5&player=' + surname + '+' + name


conn = sqlite3.connect('shogi.db')
cursor = conn.cursor()
cursor.execute('SELECT surname, firstname FROM players LIMIT 1')
print(cursor.fetchone())
print(cursor.fetchone())
conn.close()
