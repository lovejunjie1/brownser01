import json

def loadJson(path):
    file_object = open(path, 'r')
    data = json.load(file_object)
    return data

def saveJson(data, path):
    jsonDump = json.dumps(data)
    file_object = open(path, 'w')
    file_object.write(jsonDump)
    file_object.close()
