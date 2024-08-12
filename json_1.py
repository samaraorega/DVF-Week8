#Normally in a dictionary structure
#Importing the JSON module
import json

#Loading json data
with open('nyc_2001_campaign_finance.json') as f:
    data = json.load(f)
print(type(data))

#Sice its a dict, we check the keys
data.keys()

#Investigating the data types stored
for v in data.values():
    print(type(v))

#Viewing how the data looks like
import pandas as pd
pd.set_option("max_colwidth", 120)
pd.DataFrame(
    data=data['meta']['view'].values(),
    index=data['meta']['view'].keys(),
    columns=["value"]
)

#Extracting values from json files
data['meta']['view'].keys()
#dict_keys(['id', 'name', 'attribution', 'averageRating', 'category', 'createdAt', 'description', 'displayType', 'downloadCount', 'hideFromCatalog', 'hideFromDataJson', 'indexUpdatedAt', 'newBackend', 'numberOfComments', 'oid', 'provenance', 'publicationAppendEnabled', 'publicationDate', 'publicationGroup', 'publicationStage', 'rowClass', 'rowsUpdatedAt', 'rowsUpdatedBy', 'tableId', 'totalTimesRated', 'viewCount', 'viewLastModified', 'viewType', 'columns', 'grants', 'metadata', 'owner', 'query', 'rights', 'tableAuthor', 'tags', 'flags'])
data['meta']['view']['description']
#Output
'A listing of public funds payments for candidates for City office during the 2001 election cycle'

#When writing in a json file
#with open('doc_info_list.json', 'w') as f:
  #Gjson.dump(doc_info_list, f)