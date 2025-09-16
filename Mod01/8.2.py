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

maakoodi = input("Anna maakoodi: ")

cursor.execute(f"SELECT type, count(*) FROM airport WHERE iso_country = '{maakoodi}' GROUP BY type")

result = cursor.fetchall()

print(result)