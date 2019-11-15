from utils import GettingDataFromAPI
import xml.etree.cElementTree as ET



class GenerateXMLFromYears:

    year = 0

    def __init__(self, year):
        self.year=year


    def getData(self):
        json = GettingDataFromAPI.getDataFromREST(self.year).getData()
        return json

    def parseJsonIntoObjects(self):
        jsonTemp = self.getData()
        allTeams = jsonTemp['league']['standard']

        teamsYear = ET.Element("Teams", year = "{}".format(self.year))
        NbaTeams = ET.SubElement(teamsYear,"NbaTeams")
        nonNbaTeams = ET.SubElement(teamsYear,"NonNbaTeams")

        for tempTeamsList in allTeams:
            if tempTeamsList['isNBAFranchise'] == True:
                tempTeam = ET.SubElement(NbaTeams,"team", name="{}".format(tempTeamsList['fullName']))
            else:
                tempTeam = ET.SubElement(nonNbaTeams,"team", name="{}".format(tempTeamsList['fullName']))
            try:
                ET.SubElement(tempTeam,"Nickname").text = "{}".format(tempTeamsList['nickname'])
                ET.SubElement(tempTeam, "teamShortName").text = "{}".format(tempTeamsList['teamShortName'])
                ET.SubElement(tempTeam,"Conference").text = "{}".format(tempTeamsList['confName'])
                if tempTeamsList['divName'] != "{}":
                    ET.SubElement(tempTeam, "Division").text = "{}".format(tempTeamsList['divName'])
            except:
                print("skipped something")

        print("{} completed".format(self.year))
        tree = ET.ElementTree(teamsYear)
        return tree


# GenerateXMLFromYears(2019).parseJsonIntoObjects()
