import sqlite3


peopleValues = (('Jean-Baptiste Zorg', 'Human', 122), ('Korben Dallas', 'Meat Popsicle', 100), 
                ("Ak'not", 'Mangalore', -5))

with sqlite3.connect('Roster_database.db') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS People")
    c.execute("CREATE TABLE People(Name TEXT, Species TEXT, IQ INT)")
    c.executemany("INSERT INTO People VALUES(?, ?, ?)", peopleValues)
    c.execute("UPDATE People SET Species = 'Human' WHERE Name = 'Korben Dallas'")
    c.execute("SELECT Name, IQ FROM People WHERE Species == 'Human'")
    while True:
            row = c.fetchone()
            if row is None:
                    break
            print(row)

    connection.commit()
 
