import requests
import json

def getAuthors(pageSize):
    try:
        getRequest = requests.get(f"https://jsonapiplayground.reyesoft.com/v2/authors?page[size]={pageSize}")
    except Exception as e:
        print("Exception in getAuthors method: " + str(e))
    return getRequest.text


def addRecordsinDictionary(data):
    try:
        result = {}
        jsonResult = json.loads(data)
        for eachRecord in jsonResult.get("data"):
            result[eachRecord.get("attributes").get("name")] = len(eachRecord.get("relationships").get('books').get('data'))
    except Exception as e:
        print("Exception in addRecordsinDictionary method: " + str(e))
    return result


def outputResult(data):
    try:
        for record in data:
            print("Authors Name: " + record + "\nTotal Books: " + str(data[record]) + "\n")
    except Exception as e:
        print("Exception in getAuthors method: " + str(e))




if __name__ == "__main__":
    pageSize = 10
    getRequest = getAuthors(pageSize)
    resultInDict = addRecordsinDictionary(getRequest)
    outputResult(resultInDict)
