from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url
uri = "..."

#create a new client and connectt to server
client = MongoClient(uri)

#create database name and collection name
DATABASE_NAME="Wafer_Fault_Detection"
COLLECTION_NAME='Sensor_Data'

df = pd.read_csv(r"D:\College VIIT\4th year\Internship\Project\notebooks\wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0",axis=1)

json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
