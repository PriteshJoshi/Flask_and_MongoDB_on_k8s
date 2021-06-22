import os

def get_mongo_url():
  mongo_username = os.environ['MONGO_USERNAME']
  mongo_passwd = os.environ['MONGO_PASSWORD']
  mongo_server = os.environ['MONGODB_SERVER']
  mongo_url = 'mongodb://' + mongo_username + ':' + mongo_passwd + '@' + mongo_server + ':27017/'
  return mongo_url
