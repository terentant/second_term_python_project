import pandas as pd
import sqlite3
import urllib.parse


def player_url(surname, firstname):
    return 'http://fesashogi.eu/index.php?mid=5&player=' + \
           urllib.parse.quote(surname + ' ' + firstname, encoding='cp1252')


conn = sqlite3.connect('shogi.db')
cursor = conn.cursor()
cursor.execute('SELECT surname, firstname FROM players')
i = 0
for name in cursor.fetchall():
    i += 1
    if i % 100 == 0:
        print(i)
    url = player_url(name[1], name[0])
    data = pd.read_html(url)
    data[0].to_sql(name[1] + '_' + name[0] + '_rating', conn, if_exists='replace', index=False)
    data[1].to_sql(name[1] + '_' + name[0] + '_tournaments', conn, if_exists='replace', index=False)

conn.commit()
conn.close()
