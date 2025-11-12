# https://goheels.com/sports/mens-basketball/roster/2023-24
import pandas as pd
import numpy as np

player = {"Last Name": ['High', 'Cadeau', 'Trimble', 'Ingram', 'Ryan', 'Davis', 'Bacot', 'Wojcik', 'Washington', 'Lebo'],
          "First Name": ['Zayden', 'Elliot', 'Seth', 'Harrison', 'Cormac', 'RJ', 'Armando', 'Paxson', 'Jalen', 'Creighton'],
          "height": [81, 73, 75, 79, 77, 72, 83, 77, 82, 73],
          "weight": [225, 180, 195, 225, 195, 180, 240, 195, 230, 180]}
data = pd.DataFrame(player)

# bmi = weight in kg/ height in meters squared
data["bmi"] = (data["weight"]/2.205)/((data["height"]/39.37)**2)
data["bmi"] = np.floor(data["bmi"] * 100) / 100
print(data)

data.to_csv("bmi.csv")