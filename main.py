from utils import XMLGenerator
from utils import MakeXmlPretty

class main:

    years = []
    allowedYears = [2016, 2017, 2018, 2019]
    XMLStart = '<?xml version="1.0" encoding="utf-8" ?><AllTeams>'

    def getYearsFromUser(self):

        tempInput = input("Please enter some years from 2016 to 2019, with ',' separating it")
        tempYears = tempInput.split(",")

        try:
            tempYearsInt = list(map(int,tempYears))
        except:
            print("You did not entered correct years")
            self.getYearsFromUser()

        # print(tempYearsInt)
        # print(self.allowedYears)

        if filter(lambda x: tempYearsInt in x, self.allowedYears):
            self.generateFullXML(tempYearsInt)
        else:
            print("You did not entered correct years")
            self.getYearsFromUser()


    def generateFullXML(self, years):

        xmlFiles = []

        for year in years:
            xmlFiles.append(XMLGenerator.GenerateXMLFromYears(year).parseJsonIntoObjects())

        with open('teams.xml','a') as file:
            file.write(self.XMLStart)

        for xml in xmlFiles:
            xml.write(open('teams.xml','a'), encoding='unicode')

        with open('teams.xml','a') as file:
            file.write("</AllTeams>")

        self.askForPretty()


    def askForPretty(self):
        answer = input("Do you want your XML to be pretty? type 'yes' or 'no' ")
        if answer == "yes":
            MakeXmlPretty.MakeXMLPretty()
        elif answer == "no":
            print("Completed")
        else:
            print("Type correct answer")
            self.askForPretty()


if __name__ == '__main__':
    main().getYearsFromUser()

