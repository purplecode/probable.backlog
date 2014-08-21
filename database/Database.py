import pymongo
from database.KeyPass import KeyPass
from database.Collection import Collection

class Database():
  def __init__(self, database, port=27017):
    client = pymongo.MongoClient(host='localhost', port=port)
    self.connection = client[database]
    self.database = database
    self.port = port

  def authenticate(self, username, password):
    self.connection.authenticate(name=username, password=password)
    return self

  def authenticateWithKeyPass(self, username):
    password = KeyPass().getDatabasePassword(KeyPass.MONGO, database=self.database, port=self.port, username=username)
    return self.authenticate(username, password)

  def getCollection(self, name):
    return Collection(self.connection[name])
