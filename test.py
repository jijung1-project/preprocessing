import pandas as pd
import re

data = pd.read_csv('data.csv')
for i in range(0, len(data)):
    p = re.compile("^[^,]+")
    b = p.findall(str(data["감독"][i]))
    data["감독"][i] = b[0]


data.to_csv('data.csv',index=False)