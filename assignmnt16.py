          #ASSIGNMENT-16 (DATABASE)
# Q.1- Create a database. Create the following tables:
# and Insert values in the tables.
# 1.Book
import pymysql 
db=pymysql.connect('localhost','root','ashkaur11','student')
cursor = db.cursor()
cursor.execute("desc book")
print(cursor.fetchall())
db.close()

 
# 2.Titles
import pymysql 
db=pymysql.connect('localhost','root','ashkaur11','acadview')
cursor = db.cursor()
cursor.execute("desc titles")
print(cursor.fetchall())
db.close() 


# 3.Publishers
import pymysql 
db=pymysql.connect('localhost','root','ashkaur11','acadview')
cursor = db.cursor()
cursor.execute("desc publishers")
print(cursor.fetchall())
db.close() 


# 4.Zipcodes
import pymysql 
db=pymysql.connect('localhost','root','ashkaur11','acadview')
cursor = db.cursor()
cursor.execute("desc zipcodes")
print(cursor.fetchall())
db.close() 


# 5.AuthorsTitles
import pymysql 
db=pymysql.connect('localhost','root','ashkaur11','acadview')
cursor = db.cursor()
cursor.execute("desc authorstitle")
print(cursor.fetchall())
db.close()
 
# 6.Authors
import pymysql 
db=pymysql.connect('localhost','root','ashkaur11','acadview')
cursor = db.cursor()
cursor.execute("desc authors")
print(cursor.fetchall())
db.close() 



# Q.2- Insert values in the tables.
import pymysql 
db=pymysql.connect('localhost','root','ashkaur11','student')
cursor = db.cursor()
cursor.execute("select * from book")
print(cursor.fetchall())
db.close()

 
# 2.Titles
import pymysql 
db=pymysql.connect('localhost','root','ashkaur11','acadview')
cursor = db.cursor()
cursor.execute("select * from titles")
print(cursor.fetchall())
db.close() 


# 3.Publishers
import pymysql 
db=pymysql.connect('localhost','root','ashkaur11','acadview')
cursor = db.cursor()
cursor.execute("select * from publishers")
print(cursor.fetchall())
db.close() 


# 4.Zipcodes
import pymysql 
db=pymysql.connect('localhost','root','ashkaur11','acadview')
cursor = db.cursor()
cursor.execute("select * from zipcodes")
print(cursor.fetchall())
db.close() 


# 5.AuthorsTitles
import pymysql 
db=pymysql.connect('localhost','root','ashkaur11','acadview')
cursor = db.cursor()
cursor.execute("select * from authorstitle")
print(cursor.fetchall())
db.close()
 
# 6.Authors
import pymysql 
db=pymysql.connect('localhost','root','ashkaur11','acadview')
cursor = db.cursor()
cursor.execute("select * from authors")
print(cursor.fetchall())
db.close() 


# Q.3- Update any values in any of the tables. Print the original and updated values.
# 6.Authors
import pymysql 
db=pymysql.connect('localhost','root','ashkaur11','acadview')
cursor = db.cursor()
cursor.execute(" select * from authors")
print(cursor.fetchall())
db.close() 
