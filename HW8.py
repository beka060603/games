
import sqlite3
connection = sqlite3.connect("db.sqlite3")
cursor = connection.cursor()
cursor.execute("CREATE TABLE cars(model TEXT, volume INTEGER, made TEXT, id INTEGER)")

cursor.execute("INSERT INTO cars VALUES ('Lada', 99, 'Rasha', 1)")

connection.close()

class Car:

    def __init__(self, model, volume, madel, id):
        self.model = model
        self.volume = volume
        self.madel = madel
        self.id = id

    def save(self):

        try:
            cursor.execute(f"INSERT INTO cars values (?, ?, ?, ?)",
                           (self.model, self.volume, self.madel, self.id))
            connection.commit()

        except Exception:
            cursor.execute(
                "CREATE TABLE cars (model TEXT, volume INTEGER, made TEXT, id INTEGER)")
            cursor.execute(f"INSERT INTO cars values (?, ?, ?, ?)",
                           (self.model, self.volume, self.madel, self.id))
            connection.commit()


    def link(self):
        cursor.execute(
            "CREATE TABLE cars_driwer (driwer_id INTEGER,FOREIGN KEY (cars_id) references"
            "cars(id),FOREIGN KEY (managers_id) references driwer(id), cars_id INTEGER)")
        connection.commit()

class Driver:

    def __init__(self, name, year, id):
        self.name = name
        self.year = year
        self.id = id

    def save(self):
        try:
            cursor.execute(f"INSERT INTO driwer values (?, ?, ?,)",
                           (self.name, self.year,  self.id))
            connection.commit()

        except Exception:
            cursor.execute("CREATE TABLE managers (id INTEGER , name TEXT, year INTEGER,)")
            cursor.execute(f"INSERT INTO managers values (?, ?, ?)",
                           (self.name, self.year, self.id))
            connection.commit()

car = Car(1, "bmv", 99, "german")
car.save()
car2 = Car(2, "Lexus", 350, "Japan")
car2.save()
i_am = Driver(3, "beka", 16, )
car.link()
