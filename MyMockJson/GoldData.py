import requests

class Gold(object):
    def __init__(self):
        self.url = "https://jsonapiplayground.reyesoft.com/v2/authors?page[size]=10"

    @property
    def get(self):
        try:
            r = requests.get(url=self.url, timeout=1)
            if r.ok:
                return r
            else:
                return None
        except requests.exceptions.Timeout:
            return "Bad Response"

# obj = Gold()
# print(obj.get.text)