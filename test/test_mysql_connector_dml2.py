
import datetime
import mysql.connector

cnx = mysql.connector.connect(user='ygct', password='ygct',
                              host='127.0.0.1',
                              database='employees')
cursor = cnx.cursor()

query = ("SELECT first_name, last_name, hire_date FROM employees "
         "WHERE hire_date BETWEEN %s AND %s")

hire_start = datetime.date(2017, 1, 1)
hire_end = datetime.date(2017, 12, 31)

cursor.execute(query, (hire_start, hire_end))

for (first_name, last_name, hire_date) in cursor:
  print("{}, {} was hired on {:%d %b %Y}".format(
    last_name, first_name, hire_date))

cursor.close()
cnx.close()

