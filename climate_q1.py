import matplotlib.pyplot as plt
import sqlite3 as sqla

years = []
co2 = []
temp = []

connection = sqla.connect("climate.db")
cursor = connection.cursor()
cursor.execute("SELECT Year, CO2, Temperature FROM ClimateData")
data = cursor.fetchall()

for table in data:
    years.append(table[0])
    co2.append(table[1])
    temp.append(table[2])

connection.close()

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.tight_layout()  
plt.show() 
plt.savefig("co2_temp_1.png")


