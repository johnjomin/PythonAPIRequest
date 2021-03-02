import requests
import json

def getAuthors(pageSize, pageNumber):
    try:
        getRequest = requests.get(f"https://jsonapiplayground.reyesoft.com/v2/authors?page[size]={pageSize}&page[number]={pageNumber}")
    except Exception as e:
        print("Exception in getAuthors method: " + str(e))
    return getRequest.text


def addRecordsinDictionary(data):
    try:
        result = {}
        count = 1
        jsonResult = json.loads(data)
        for eachRecord in jsonResult.get("data"):
            if eachRecord.get("attributes").get("name") == None:
                print("\nThere are no more authors\n\n")
                break
            elif count == 15:
                print("\n15 pages has been processed\n")
                break
            else:
                result[eachRecord.get("attributes").get("name")] = len(eachRecord.get("relationships").get('books').get('data'))
            count +=1
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
    pageSize = 16
    pageNumber = 1

    getRequest = getAuthors(pageSize, pageNumber)
    resultInDict = addRecordsinDictionary(getRequest)
    outputResult(resultInDict)
