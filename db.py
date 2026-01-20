from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["car_lease_ai"]

contracts = db["contracts"]