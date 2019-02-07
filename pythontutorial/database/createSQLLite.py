import sqlite3

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()


def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")
    print('After table creation')

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(1452549219,'2016-01-11 13:53:39','Python',6)")
    conn.commit()
    print('after insert')
    c.close()
    conn.close()


create_table()
data_entry()