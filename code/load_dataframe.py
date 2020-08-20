import pandas as pd
import numpy as np
import re

def strip(data):
    pattern = re.compile('[^0-9]', re.UNICODE)
    return re.sub(pattern, "", str(data))
    

filePath = '/Users/helix/Coding/attitude/data/'
data = pd.read_excel(filePath+'all_people.xlsx')
data = data[['id', '政治态度得分']]
data.columns = ['id', 'score']
data.dropna()
data.id = data.id.apply(strip)
print(data.head())
