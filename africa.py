import csv


from cs50 import SQL 

open ("africa.db","w").close()


db = SQL("sqlite:///africa.db")

db.execute("CREATE TABLE Location(Location_id INTEGER, Country TEXT, Languages TEXT,PRIMARY KEY(Location_id))")
db.execute("CREATE TABLE Status (Status_id INTEGER, Population INTEGER, Income_group TEXT, PRIMARY KEY(Status_id))")
db.execute("CREATE TABLE location_Status(Independence INTEGER, Location_id INTEGER, Status_id INTEGER, PRIMARY KEY(Location_id), FOREIGN KEY(Location_id) REFERENCES Location(Location_id),FOREIGN KEY(Status_id) REFERENCES Status(Status_id))")



with open("africa.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:
        countries= row["Country_name"]
        income=row["Income_group"]
        language=row["Language"]
        population=row["Population"]
        independence=row["Independence"]

        location =db.execute("INSERT INTO location(Country, Languages) VALUES(?,?)",countries, language)
        Status= db.execute("INSERT INTO Status(Population, Income_group) VALUES(?,?)",population, income)
        location_Status= db.execute("INSERT INTO location_Status(Status_id, Location_id,Independence) VALUES((SELECT Status_id FROM Status WHERE Population=?),(SELECT Location_id FROM Location WHERE Country =?),?)",countries,population,independence)