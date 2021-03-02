import requests
import json

class JsonAPIExercise2(object):
    '''
    JSON API Exercise 2 enables to populate result of Authors whose does not
    extend beyond 15 and no more authors to be found.
    '''
    def __init__(self):
        '''
        This is an init function and variables defined in order to be executed.
        '''
        self.pageSize = 16
        self.pageNumber = 1
        self.url = f"https://jsonapiplayground.reyesoft.com/v2/authors?page[size]={self.pageSize}&page[number]={self.pageNumber}"


    def getAuthors(self):
        '''
        Sends GET HTTP request and returns the result!

        Returns:
            str: The result of GET Response
        '''
        try:
            getRequest = requests.get(url=self.url, timeout=1)
        except requests.exceptions.Timeout:
            return "Bad Response"
        except Exception as e:
            print("Exception in getAuthors method: " + str(e))
        return getRequest


    def addRecordsinDictionary(self, data):
        '''
        Retrieves GET Response as text and returns the data into dictionary

        Args:
            data (str): HTTP Response in text format
        
        Returns:
            dict: The result populated in Dictionary
        '''
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


    def outputResult(self, data):
        '''
        Output elements from dictionary

        Args:
            data (dict): Parameter in Dictionary format
        '''
        try:
            for record in data:
                print("Authors Name: " + record + "\nTotal Books: " + str(data[record]) + "\n")
        except Exception as e:
            print("Exception in getAuthors method: " + str(e))


    @property
    def get(self):
        '''
        Function to execute HTTP GET Response and convert result in Dictionary.
        Also to Output the results.
        '''
        obj = JsonAPIExercise2()
        getRequest = obj.getAuthors()
        resultInDict = obj.addRecordsinDictionary(getRequest.text)
        obj.outputResult(resultInDict)

# obj = JsonAPIExercise2()
# obj.get