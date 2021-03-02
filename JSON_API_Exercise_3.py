import requests
import json

class JsonAPIExercise3(object):
    def __init__(self, authorID = 0):
        self.authorID = authorID
        self.url = f"https://jsonapiplayground.reyesoft.com/v2/authors/{self.authorID}"

    def get_authorID(self):
        return self.authorID

    def set_authorID(self, x):
        self.authorID = x

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
            eachRecord = jsonResult.get("data")
            result[eachRecord.get("attributes").get("name")] = len(eachRecord.get("relationships").get('books').get('data'))
        except Exception as e:
            if jsonResult.get("errors"):
                print("\nNo Records found under Request to be implemented in Dictionary")
            else:
                print("\nException in addRecordsinDictionary method: " + str(e))
        return result


    def outputResult(self, data):
        try:
            print("\nTotal Record in Dictionary: " + str(len(data)) + "\n")
            for record in data:
                print("Authors Name: " + record + "\nTotal Books: " + str(data[record]) + "\n")
        except Exception as e:
            print("\nException in getAuthors method: " + str(e))


    def get(self, authorID):
        obj = JsonAPIExercise3(authorID)
        obj.set_authorID(authorID)
        getRequest = obj.getAuthors()
        resultInDict = obj.addRecordsinDictionary(getRequest.text)
        obj.outputResult(resultInDict)

# obj = JsonAPIExercise3()
# obj.get(2)