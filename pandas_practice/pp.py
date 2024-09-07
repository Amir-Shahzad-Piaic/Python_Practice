import pandas as pd
import numpy as np


# creating a DataFrame
data = {
    'names': ['amir', 'javeria', 'sonia', 'adnan', 'zeeshan', 'hamza'],
    'age(years)': [30, 29, 27, 23, 23, 18],
    'gender': ['M', 'F', 'F', 'M', 'M', 'M'],
    'city(current)': ['lahore', 'Muzaffargarh', 'kuwait', 'lahore', 'gujrat', 'Multan']
}
df = pd.DataFrame(data)
print(df)

# creating a DataFrame numpy tool