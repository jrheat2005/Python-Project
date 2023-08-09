import sqlite3
conn = sqlite3.connect('test1.db')
with conn:
    cur = conn.cursor()
    # create table tbl_files
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                col_files TEXT)")
    conn.commit()

conn = sqlite3.connect('test1.db')
# list of the files
list_of_files = ('information.docx','Hello.txt','myImage.png','myMovie.mpg', \
                 'World.txt','data.pdf','myPhoto.jpg')

# Increment through all the file
# looking for any file ending in .txt and printing it
for x in list_of_files:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files (col_files) VALUES (?)", (x,))
            print(x)
conn.close() #close connection
