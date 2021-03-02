import requests
import json

def getAuthors(author_id):
    try:
        getRequest = requests.get(f"https://jsonapiplayground.reyesoft.com/v2/authors/{author_id}")
        print("\nResult: " + getRequest.reason + "\nStatus Code: " + str(getRequest.status_code))
    except Exception as e:
        print("Exception in getAuthors method: " + str(e))
    return getRequest.text


def addRecordsinDictionary(data):
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


def outputResult(data):
    try:
        print("\nTotal Record in Dictionary: " + str(len(data)) + "\n")
        for record in data:
            print("Authors Name: " + record + "\nTotal Books: " + str(data[record]) + "\n")
    except Exception as e:
        print("\nException in getAuthors method: " + str(e))




if __name__ == "__main__":
    author_id = 1

    getRequest = getAuthors(author_id)
    resultInDict = addRecordsinDictionary(getRequest)
    outputResult(resultInDict)
