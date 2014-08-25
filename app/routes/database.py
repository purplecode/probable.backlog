from django.http import HttpResponse
from common.database.Database import Database
from bson.json_util import dumps

database = Database(database='backlog', port=27017).authenticateWithKeyPass('backlog')

class JsonResponse(HttpResponse):
    def __init__(self, content={}):
        super(JsonResponse, self).__init__(dumps(content))

class QueryParams(object):
    def __init__(self, payload):
      self.filtering = payload['filtering'] if 'filtering' in payload else {}
      self.sorting = payload['sorting'] if 'sorting' in payload else {}


def documents(request, collection):
    queryParams = QueryParams(request.POST)
    return JsonResponse([doc for doc in database.getCollection(collection).find(queryParams.filtering)])