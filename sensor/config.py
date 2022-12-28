import pymongo
import pandas as pd
import json
from dataclasses import dataclass
import os

# Provide the mongodb localhost url to connect python to mongodb.


@dataclass
class EnviromentVariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URL")
    aws_access_key_id:str = os.getenv("AWS_ACCESS_KEY")
    aws_access_secret_key:str = os.getenv("AWS_ACCESS_KEY_SECRET")

env_var = EnviromentVariable()

mongo_client = pymongo.MongoClient(env_var.mongo_db_url)
    