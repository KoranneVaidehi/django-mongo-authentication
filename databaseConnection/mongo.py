from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://Vaidehi:Vaidehi09@bdconnectioo.sdnwbgg.mongodb.net/?appName=bdconnectioo"
)

db = client["mongodjango"]      # 👈 ye database banega
users_collection = db["users"]  # 👈 ye collection banegi
