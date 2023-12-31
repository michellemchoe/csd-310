import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "Ms-259631",
    "host": "localhost",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    
    input ("\n\n  Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")
        
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")
    
    else:
        print(err)


    
            
cursor = db.cursor()


print("-- DISPLAYING studio RECORDS --")

cursor.execute("SELECT * FROM studio")
studio = cursor.fetchall()

for studio in studio:
    print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))


print("-- DISPLAYING genre RECORDS --")

cursor.execute("SELECT * FROM genre")
genre = cursor.fetchall()

for genre in genre:
    print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))
    
    
print("-- DISPLAYING short film RECORDS --")

cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
shortFilm = cursor.fetchall()

for shortFilm in shortFilm:
    print("Film Name: {}\nRuntime: {}\n".format(shortFilm[0], shortFilm[1]))

print("-- DISPLAYING director RECORDS in order --")

cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
director = cursor.fetchall()

for director in director:
    print("Film Name: {}\nDirector: {}\n".format(director[0], director[1]))
