import os
import re
path = '/Users/helix/Coding/attitude/data/vector/zw/json/1/'

filenames = os.listdir(path)

for filename in filenames:
    old_name = path + filename
    new_name =  re.sub('[\u4e00-\u9fa5]', '', old_name)
    os.rename(old_name, new_name)
