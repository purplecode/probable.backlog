from django.http import HttpResponse
from common.database.Database import Database
from bson.json_util import dumps 
from django.views.decorators.csrf import csrf_exempt
import json


database = Database(database='backlog', port=27017).authenticateWithKeyPass('backlog')

class JsonResponse(HttpResponse):
    def __init__(self, content={}):
        super(JsonResponse, self).__init__(dumps(content))

class QueryParams(object):
    def __init__(self, request):
      payload = json.loads(request.body if request.body else "{}")
      self.filtering = payload['filtering'] if 'filtering' in payload else {}
      self.fields = payload['fields'] if 'fields' in payload else None
      self.sorting = payload['sorting'] if 'sorting' in payload else {}

    def getFields(self):
      return self.fields

    def getFiltering(self):
      return self.filtering

    def getSorting(self):
      return [(key, direction) for key, direction in self.sorting.iteritems()]


@csrf_exempt
def documents(request, collection):
    queryParams = QueryParams(request)
    documents = database.getCollection(collection).find(queryParams.getFiltering(), queryParams.getFields(), queryParams.getSorting())
    return JsonResponse([document for document in documents])

def document(request, collection, id):
    return JsonResponse(database.getCollection(collection).findOne({'id' : id}))