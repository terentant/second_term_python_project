import sqlite3
from tkinter import *
from tkinter import ttk


def click_button():
    global root, combobox, tree, entry, btn, conn
    btn.destroy()
    cur = conn.cursor()
    tree.destroy()
    if combobox.get() == 'All countries':
        cur.execute('SELECT * FROM players LIMIT ' + entry.get())
    else:
        cur.execute('select * from players where nationality == "' + combobox.get() + '" limit ' + entry.get())

    rows = cur.fetchall()

    tree = ttk.Treeview(root, columns=[str(i) for i in range(len(rows[0]))], selectmode="browse")

    for i, col in enumerate(cur.description):
        tree.heading(str(i), text=col[0])

    for row in rows:
        tree.insert('', END, values=row)
    tree.column("#0", stretch=NO, minwidth=0, width=0)
    tree.column("#1", stretch=NO, minwidth=30, width=20)
    tree.column("#2", stretch=NO, minwidth=100, width=100)
    tree.column("#3", stretch=NO, minwidth=100, width=100)
    tree.column("#4", stretch=NO, minwidth=50, width=50)
    tree.column("#5", stretch=NO, minwidth=50, width=50)
    tree.column("#6", stretch=NO, minwidth=50, width=50)
    tree.column("#7", stretch=NO, minwidth=50, width=50)
    tree.column("#8", stretch=NO, minwidth=30, width=30)

    tree.pack(anchor="sw", padx=20, pady=30)
    tree.bind("<Double-1>", on_select)

    btn = ttk.Button(text="Показать", command=click_button)
    btn.pack(anchor="n")

    entry.place(relx=0.05, rely=0.86, width=100)

    label = ttk.Label(text='лучших игроков из')
    label.place(relx=0.4, rely=0.86)

    cur.execute("select nationality from players")
    nat = list(set(cur.fetchall()))
    nat.sort()
    nat = ['All countries'] + nat
    allnat = nat[0]
    combobox = ttk.Combobox(textvariable=allnat, values=nat, state="readonly")
    combobox.set(nat[0])
    combobox.place(relx=0.7, rely=0.86, width=100)


def on_select(event):
    global conn
    cur = conn.cursor()

    item_id = event.widget.selection()[0]
    values = event.widget.item(item_id)['values']

    new_window = Toplevel(root)

    cur.execute('select * from ' + values[2]+'_'+values[1]+'_tournaments')
    rows = cur.fetchall()
    new_window.title(values[1]+' '+values[2])
    tree_1 = ttk.Treeview(new_window, columns=[str(i) for i in range(len(rows[0]))], selectmode="browse")

    for i, col in enumerate(cur.description):
        tree_1.heading(str(i), text=col[0])

    for row in rows:
        tree_1.insert('', END, values=row)
    tree_1.column("#0", stretch=NO, minwidth=0, width=0)
    tree_1.column("#1", stretch=NO, minwidth=250, width=250)
    tree_1.column("#2", stretch=NO, minwidth=150, width=150)
    tree_1.column("#3", stretch=NO, minwidth=40, width=40)
    tree_1.column("#4", stretch=NO, minwidth=40, width=40)
    tree_1.column("#5", stretch=NO, minwidth=40, width=40)
    tree_1.column("#6", stretch=NO, minwidth=30, width=30)

    tree_1.pack(anchor="sw", padx=20, pady=30)


conn = sqlite3.connect("C:\\Users\\anton\\PycharmProjects\\second_term_python_project\\scrape\\shogi.db")
root = Tk()
root.resizable(False, False)
root.title("List of players")

tree = ttk.Treeview()

entry = ttk.Entry()
entry.insert(0, '30')

btn = ttk.Button(text="Показать", command=click_button)
btn.pack(anchor="n")

combobox = ttk.Combobox()
combobox.set('All countries')

click_button()

root.mainloop()
conn.close()
