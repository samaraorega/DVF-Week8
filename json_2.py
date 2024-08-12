#Exploring and transforming JSON schema

import json
with open('output.json') as f:
    data = json.load(f)
type(data)  
data.keys()
#dict_keys(['albums'])
type(data['albums'])
data['albums'].keys()

for key in data['albums'].keys():
    print(key, type(data['albums'][key]))

#We dissect the data to figure out where the dictionaries end and if there are lists you do the same as well
# We can also check the length of the lists if there are any


#Converting JSON to alternative data formats
import pandas as pd
df = pd.DataFrame(data['albums']['items'])
df