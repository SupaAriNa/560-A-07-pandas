# https://goheels.com/sports/mens-basketball/roster/2023-24
import pandas as pd

roster_last = ['High', 'Cadeau', 'Trimble', 'Ingram', 'Ryan', 'Davis', 'Bacot', 'Wojcik', 'Washington', 'Lebo']
roster_first = ['Zayden', 'Elliot', 'Seth', 'Harrison', 'Cormac', 'RJ', 'Armando', 'Paxson', 'Jalen', 'Creighton']
height = [81, 73, 75, 79, 77, 72, 83, 77, 82, 73]
weight = [225, 180, 195, 225, 195, 180, 240, 195, 230, 180]
player = {"Last Name": roster_last,
          "First Name": roster_first,
          "height": height,
          "weight": weight}
data = pd.DataFrame(player)
print(data)
