import xml.etree.ElementTree as ET
import sqlite3

conn=sqlite3.connect('product.sqlite')
cur=conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS PRODUCT ;

CREATE TABLE PRODUCT (
    Prod_id INTEGER NOT NULL PRIMARY KEY,
    Prod_Name TEXT UNIQUE,
    Prod_Price INTEGER
    );
''')

fname=raw_input("Enter File Name :")
if len(fname)<1 : fname='product.xml'

stuff = ET.parse(fname)
all = stuff.findall('Product')
for entry in all :
    id=entry[0]
    name=entry[1]
    price=entry[2]
      
    cur.execute('''INSERT OR IGNORE INTO Product (Prod_id,Prod_Name,Prod_Price) 
        VALUES ( ?,?,? )''', ( id,name,price ) )
    conn.commit()