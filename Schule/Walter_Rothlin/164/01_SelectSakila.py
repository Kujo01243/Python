#!/usr/bin/python3

# ------------------------------------------------------------------
# Name: 01_SelectSakila.py
# Source: https://raw.githubusercontent.com/walter-rothlin/Source-Code/master/Python_WaltisExamples/Code_08_MySql/01_SelectSakila.py
#
# Description: Connects to sakila and queries data
#
# Autor: Josias Theil
#
# History:
# ------------------------------------------------------------------

# Install driver first: python -m pip install mysql-connector-python
import mysql.connector  # mysql-connector-python not default mässiger one

print("Connecting to sakila....", end="", flush=True)
mydb = mysql.connector.connect(
  host        = "localhost",
  user        = "stammdatenuser",
  password    = "Stammdatenuser",
  database    = "Stammdaten",
  auth_plugin = 'mysql_native_password'
)
print("completed!")

stm_selectCities = """
    SELECT * from Iban
"""

mycursor = mydb.cursor()
mycursor.execute(stm_selectCities)
myresult = mycursor.fetchall()

print("Records found:", len(myresult), myresult)

print("+------+--------------------------------+------------+")
print("| Id   | City                           | Country ID |")
print("+------+--------------------------------+------------+")
for aRec in myresult:
    print("| {plh:4d} |".format(plh=aRec[0]), end="")
    print(" {plh:30s} |".format(plh=aRec[1]), end="")
    print(" {plh:10d} |".format(plh=aRec[2]), end="")
    print()
    print("+------+--------------------------------+------------+")
