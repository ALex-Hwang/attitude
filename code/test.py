import json
import numpy as np
import os
import pandas as pd

filePath = '/Users/helix/Coding/attitude/data/vector/宁波大学/json/1/'
fileNames = os.listdir(filePath)
for fileName in fileNames:
    shit = open(filePath+fileName)
    test = json.load(shit)
    test = np.array(test['vectors'])
    print(test.shape)
    shit.close()