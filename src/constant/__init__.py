import os


AWS_S3_BUCKET_NAME = "wafer-fault"
MONGO_DATABASE_NAME = "Wafer_Fault_Detection"
MONGO_COLLECTION_NAME = "Sensor_Data"


TARGET_COLUMN = "quality"
MONGO_DB_URL="mongodb+srv://tanushlichade:Tanush@cluster0.jvum79r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


MODEL_FILE_NAME = "model"
MODEL_FILE_EXTENSION = ".pkl"

artifact_folder =  "artifacts"