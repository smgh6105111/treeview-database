import sqlite3


def dataentry():
	con=sqlite3.connect('treedata1.db')
	cur=con.cursor()
	
	cur.execute('CREATE TABLE IF NOT EXISTS treedata1 (id INTEGER PRIMARY KEY,enid,enfirstname text, enlastname text, engender text, enemail text, enhours text, enpayfor1 text, entax text, enpayment text) ')
	
	con.commit()
	con.close()
	
	
def adddata(enid,enfirstname,enlastname,engender,enemail,enhours,enpayfor1,entax,enpayment):
	con=sqlite3.connect('treedata1.db')
	cur=con.cursor()
	
	cur.execute('INSERT INTO treedata1 VALUES (NULL,?,?,?,?,?,?,?,?,?)',(enid,enfirstname,enlastname,engender,enemail,enhours,entax,enpayfor1,enpayment))
	con.commit()
	con.close()
	
	
def viewdata():
	con=sqlite3.connect('treedata1.db')
	cur=con.cursor()
	
	cur.execute('SELECT * FROM treedata1')
	rows=cur.fetchall()
	con.close()
	return rows
	
	
def deldata(id):
		con=sqlite3.connect('treedata1.db')
		cur=con.cursor()
		cur.execute('DELETE FROM treedata1 WHERE id=?',(id,))
		con.commit()
		con.close()
		


dataentry()