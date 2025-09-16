import mysql.connector
import geopy
from geopy import distance

connection = mysql.connector.connect(
    port=3306,
    host="localhost",
    database="flight_game",
    user="root",
    passwd="!23#edcvBnmko=9",
    autocommit=True
)

cursor = connection.cursor()

icao1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ")
icao2 = input("Anna toisen lentäkentän ICAO-koodi: ")

cursor.execute(f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{icao1}'")
icao1_tulos = cursor.fetchall()
cursor.execute(f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{icao2}'")
icao2_tulos = cursor.fetchall()

print("Lentokenttien välinen etäisyys on",distance.distance(icao1_tulos, icao2_tulos).km,"km.")

