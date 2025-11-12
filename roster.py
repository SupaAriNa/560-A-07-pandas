# https://goheels.com/sports/mens-basketball/roster/2023-24
import pandas as pd

roster = ['High', 'Cadeau', 'Trimble', 'Ingram', 'Ryan', 'Davis', 'Bacot', 'Wojcik', 'Washington', 'Lebo']
player = {"Last Name": roster}
data = pd.DataFrame(player)
print(data)
