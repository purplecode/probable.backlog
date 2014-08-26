from bson import ObjectId

def wrapIdsIntoObjects(query):
  if '_id' in query:
    subquery = query['_id']
    if type(subquery) is str or type(subquery) is unicode:
      query['_id'] = ObjectId(subquery)
    elif type(subquery) is dict:
      for key, value in subquery.iteritems():
        if type(value) is str or type(value) is unicode:
          query['_id'][key] = ObjectId(value)
        elif type(value) is list:
          query['_id'][key] = map(lambda id: ObjectId(id), value)
  return query


class Collection():
  def __init__(self, collection):
    self.collection = collection

  def fullName(self):
    return self.collection.full_name

  def remove(self, query={}):
    return self.collection.remove(wrapIdsIntoObjects(query))

  def insert(self, data):
    return self.collection.insert(data)

  def find(self, query={}, fields=None, sort=None, skip=0, limit=0):
    cursor = self.collection.find(spec=wrapIdsIntoObjects(query), fields=fields, skip=skip, limit=limit)
    if sort: cursor.sort(sort)
    return cursor

  def findOne(self, query={}, fields=None):
    return self.collection.find_one(wrapIdsIntoObjects(query), fields)

  def findById(self, id):
    return self.findOne({'_id': ObjectId(id)})

  def aggregate(self, fields, aggregation, match={}):
    # ['a', 'b'] -> {'a' : '$a', 'b' : '$b'}
    fields = dict(zip(fields, ['$%s' % field for field in fields]))
    group = dict({'_id': fields}, **aggregation)
    return self.collection.aggregate([{'$match': match}, {'$group': group}])

  def contains(self, query):
    return self.findOne(query) is not None

  def distinct(self, property):
    return self.collection.distinct(property)

  def count(self):
    return self.collection.count()

  def update(self, query, document, upsert=False):
    self.collection.update(query, document, upsert)

  def append(self, query, key, values):
    self.collection.update(wrapIdsIntoObjects(query), {"$addToSet": {key: {"$each": values}}}, True)

