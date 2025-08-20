import os
import sys
import json


from dotenv import load_dotenv

load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)


import certifi
ca=certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NewtworkDataExtract():
    def __int__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json_convertor(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
            
    def insert_data_mongobd(self,records,database, collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records    
            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            
            self.databse=self.mongo_client[self.database]
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return(len(self.records))
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)


if __name__=='__main__':
    FILE_PATH="Network_data\phisingData.csv"
    DATABASE='GANESH'
    collection="NetworkData"
    networkobj=NewtworkDataExtract() 
    records=networkobj.csv_to_json_convertor(file_path=FILE_PATH) 
    print(records)
    no_of_records=networkobj.insert_data_mongobd(records,DATABASE,collection) 
    print(no_of_records) 