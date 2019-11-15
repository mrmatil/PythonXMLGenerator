from utils import XMLGenerator
import xml.etree.cElementTree as ET

class main:

    years = []
    XMLStart = '<?xml version="1.0" encoding="utf-8" ?>'

    def getYearsFromUser(self):

        tempInput = input("Please enter some years from 2015 to 2019, with ',' separating it")
        tempYears = tempInput.split(",")
        tempYearsInt = list(map(int,tempYears))
        # print(tempYearsInt)
        self.generateFullXML(tempYearsInt)


    def generateFullXML(self, years):

        xmlFiles = []

        for year in years:
            xmlFiles.append(XMLGenerator.GenerateXMLFromYears(year).parseJsonIntoObjects())

        with open('teams.xml','a') as file:
            file.write(self.XMLStart)

        for xml in xmlFiles:
            xml.write(open('teams.xml','a'), encoding='unicode')



if __name__ == '__main__':
    main().getYearsFromUser()

