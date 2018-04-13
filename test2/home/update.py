import sqlite3 as lite
import sys
import os
path = os.path.dirname(__file__) + "\\sqlite3.db"
con = lite.connect(path)
 
with con:
     
    cur = con.cursor()    
    cur.execute("INSERT INTO home_student VALUES('hoangdo','123','DoDinhHoang')")