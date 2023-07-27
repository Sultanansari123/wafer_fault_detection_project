from pymongo.mongo_client import MongoClient
import pandas as pd
import json

uri = "mongodb+srv://sultan123:<sultan123>@cluster0.ylhshpi.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

#create database name and collection name
DATABASE_NAME="pwskills"
COLLECTION_NAME="waferfault"

# Read the data as a data frame
df=pd.read_csv("C:\Users\91726\OneDrive\Documents\MlProject\wfd\notebooks\wafer_23012020_041211.csv")

# convert the data into json
json_record=json.load(df.T.to_json)

#now dump the data into database
client[DATABASE_NAME][COLLECTION_NAME]=json_record






