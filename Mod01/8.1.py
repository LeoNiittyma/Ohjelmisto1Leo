import mysql.connector

connection = mysql.connector.connect(
    port=3306,
    host="localhost",
    database="flight_game",
    user="root",
    passwd="!23#edcvBnmko=9",
    autocommit=True
)

cursor = connection.cursor()

icao = input("Anna lentokentän ICAO-koodi")

cursor.execute(f"SELECT name, municipality FROM airport WHERE ident = '{icao}'")

result = cursor.fetchall()

print(result)