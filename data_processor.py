import pandas as pd
import json
import flat_table
tweet_df = pd.read_json("refugee.json", lines = True) #read json file line by line to avoid error


#print(tweet_df.head())

# determine which columns are nested json
json_columns = []
for column in tweet_df.columns:
    if type(tweet_df.loc[0, column]) is dict:
        json_columns.append(column)

tweet_df = tweet_df.set_index(tweet_df['id'].values)

# convert nested_json to csv
for column in json_columns:
    # with open(column+".json", 'w') as outfile:
    #     json.dump(tweet_df[column].values, outfile)
    col_df = pd.DataFrame()
    data = tweet_df[column].values
    for item in data:
        if pd.isna(item): #solve the index problem
            pass
        else:
            col_df = col_df.append(item, ignore_index=True)
    print(col_df.head())
    col_df.to_csv(column+".csv")


df.to_csv("refugee.csv")




