import requests

class getDataFromREST:

    year = 1

    def __init__(self, year):
        self.year=year

    def getData(self):
        url = "http://data.nba.net/prod/v1/{}/teams.json".format(self.year)

        response = requests.request("GET",url)

        return response.json()


# print(getDataFromREST(2019).getData())

