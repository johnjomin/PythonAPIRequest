import requests
import json

class JsonAPIExercise1(object):

    def __init__(self):
        self.pageSize = 10
        self.url = f"https://jsonapiplayground.reyesoft.com/v2/authors?page[size]={self.pageSize}"

    def getAuthors(self): 
        try:
            getRequest = requests.get(url=self.url, timeout=1)
        except requests.exceptions.Timeout:
            return "Bad Response"
        except Exception as e:
            print("Exception in getAuthors method: " + str(e))
        return getRequest


    def addRecordsinDictionary(self, data):
        try:
            result = {}
            jsonResult = json.loads(data)
            for eachRecord in jsonResult.get("data"):
                result[eachRecord.get("attributes").get("name")] = len(eachRecord.get("relationships").get('books').get('data'))
        except Exception as e:
            print("Exception in addRecordsinDictionary method: " + str(e))
        return result

    def outputResult(self, data):
        try:
            for record in data:
                print("Authors Name: " + record + "\nTotal Books: " + str(data[record]) + "\n")
        except Exception as e:
            print("Exception in getAuthors method: " + str(e))

    @property
    def get(self):
        obj = JsonAPIExercise1()
        getRequest = obj.getAuthors()
        resultInDict = obj.addRecordsinDictionary(getRequest.text)
        obj.outputResult(resultInDict)


# obj = JsonAPIExercise1()
# obj.get