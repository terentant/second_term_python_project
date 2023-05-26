import sqlite3
from tkinter import *
from tkinter import ttk

conn = sqlite3.connect("C:\\Users\\anton\\PycharmProjects\\second_term_python_project\\scrape\\shogi.db")
cur = conn.cursor()

cur.execute('SELECT * FROM players LIMIT 30')
rows = cur.fetchall()

root = Tk()
root.title("List of players")
# root.geometry("250x200")
# root.attributes("-alpha", 0)

tree = ttk.Treeview(root, columns=[str(i) for i in range(len(rows[0]))])

for i, col in enumerate(cur.description):
    tree.heading(str(i), text=col[0])

for row in rows:
    tree.insert('', END, values=row)

tree.column("#0", stretch=NO, minwidth=0,  width=0)
tree.column("#1", stretch=NO, minwidth=20, width=20)
tree.column("#2", stretch=NO, minwidth=100, width=100)
tree.column("#3", stretch=NO, minwidth=100, width=100)
tree.column("#4", stretch=NO, minwidth=50, width=50)
tree.column("#5", stretch=NO, minwidth=50, width=50)
tree.column("#6", stretch=NO, minwidth=50, width=50)
tree.column("#7", stretch=NO, minwidth=50, width=50)
tree.column("#8", stretch=NO, minwidth=30, width=30)

tree.pack()

root.mainloop()

conn.close()