import matplotlib.pyplot as plt
import pandas as pd

cd = pd.read_csv("climate.csv")
years = cd["Year"]
co2 = cd["CO2"]
temp = cd["Temperature"]

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
plt.savefig("co2_temp_2.png") 

