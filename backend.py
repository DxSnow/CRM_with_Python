import sqlite3

class Database:


    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS db(id INTEGER PRIMARY KEY, name TEXT, email TEXT, country TEXT, product TEXT, sales_amount TEXT, phone TEXT, date TEXT)")
       

    def add(self,name,email,country,product,sales_amount,phone,date):
        self.cur.execute("INSERT INTO db VALUES(NULL,?,?,?,?,?,?,?)",(name,email,country,product,sales_amount,phone,date))
        self.conn.commit()
    
    def view(self):
        return self.cur.execute("SELECT * FROM db").fetchall()
        
        
    def search(self, name = None, email = None,country = None,product = None,sales_amount = None,phone = None,date = None):
        self.cur.execute("SELECT * FROM db WHERE name = ? OR email = ? OR country = ? OR product = ? OR sales_amount = ? OR phone = ? OR date = ?", (name,email,country,product,sales_amount,phone,date))
        rows = self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM db WHERE id =?",(id,)) #don't forget the comma after id
        self.conn.commit()
    
    def update(self,name,email,country,product,sales_amount,phone,date):
        self.cur.execute("UPDATE db SET name = ?,email = ?,country = ?,product = ?,sales_amount = ?,phone = ?,date = ?WHERE id = ?", (self, name,email,country,product,sales_amount,phone,date,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()



