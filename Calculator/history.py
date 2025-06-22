import sqlite3
import csv

conn = sqlite3.connect('history.db')
c = conn.cursor()

c.execute("SELECT * FROM history")
rows = c.fetchall()

with open('history_export.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Operation', 'Result'])  # Header
    writer.writerows(rows)

print("History exported to history_export.csv")

conn.close()
