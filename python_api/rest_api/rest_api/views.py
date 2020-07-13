from django.http import JsonResponse

from . import mongo

DB = mongo.MongoDB('127.0.0.1', 'local','startup_log')

dbconnector = {'log': DB}

def startupLog(request, dbname):
    res = {}
    res['items'] = []
    db = dbconnector[dbname]
    res['itemLen'] = db.Collection.count_documents({})

    for item in db.Collection.find({}):
        each = {'hostname':'',
                'startTime':''}
        each['hostname'] = item['hostname']
        each['startTime'] = item['startTime']

        res['items'].append(each)
    
    return JsonResponse(res, safe=False)