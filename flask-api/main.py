from flask import Flask, jsonify, request
from pymongo import MongoClient
from .utils import get_mongo_url

app = Flask(__name__)
@app.route('/', methods=['GET'])
def get_all_users():

    mongo_url = get_mongo_url()
    client = MongoClient(mongo_url)
    db = client.userdata
    collection_userinfo = db.userinfo
    result = []
    for user in collection_userinfo.find():
        user['_id'] = str(user['_id'])
        result.append(user)
    client.close()
    return jsonify({'result':result})

@app.route('/', methods=['POST'])
def add_user_details():
    mongo_url = get_mongo_url()
    client = MongoClient(mongo_url)
    db = client.userdata
    collection_userinfo = db.userinfo
    data = request.get_json(force=True)
    collection_userinfo.insert_one(data)
    return jsonify(message= "User added successfully..")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
