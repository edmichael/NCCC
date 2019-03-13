#!python3
#Written by Chris Weber, Modesto PD and Ed Michael, Orlando PD for Cellebrite

# Import required modulesimport sys
import sqlite3
import sys, os

# Get database from command line

db_path = sys.argv[1]

# Pick tables/fields to work with

#print ("Enter the data below for the file. Names are case sensitive")

#TABLE_NAME = input ("What is the table name? ")

#FIELD_NAME = input ("What is the field name? ")

TABLE_NAME = "tab_sessions"

FIELD_NAME = "session_data"

# Open database, set up cursor to read database

conn = sqlite3.connect(db_path)

cur = conn.cursor()

# Create query

query = "SELECT {0} FROM {1};".format(FIELD_NAME, TABLE_NAME)

# Execute query

cur.execute(query)

# Go through returned rows

for index, row in enumerate(cur):

    # Get the first (zero'th) column from the returned row

    data = row[0]

    # Check if the data is binary, open the file in binary or text mode

    # accordingly and write the data out.

    if isinstance(data, bytes):

        file_name = "{0}.bin".format(index)

        output = open(file_name, "wb")
		
        output.write(data)


    else:

        file_name = "{0}.txt".format(index)

        output = open(file_name, "wt", encoding="utf-8")                                                           

        output.write(str(data))

    # close the file   

    output.close()

for fn in os.listdir('.'):
	file = fn
	if file.endswith('.bin'):
		f =open(file,'rb')
		f.seek(4)
		b = f.read()
		file = open(file+'.plist', 'wb')
		file.write(b)
		file.close()