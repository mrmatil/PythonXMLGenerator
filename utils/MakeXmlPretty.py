import xml.dom.minidom


class MakeXMLPretty:
    def __init__(self):
        self.__getDataFromFile__()
        self.__makeXmlPretty__()

    def __getDataFromFile__(self):
        with open('teams.xml','r') as xmlFile:
            self.xmlInStr = xmlFile.read()

    def __makeXmlPretty__(self):
        prettyXML = xml.dom.minidom.parseString(self.xmlInStr)
        prettyXML = prettyXML.toprettyxml()
        with open('teams.xml','w') as xmlFile:
            xmlFile.write(prettyXML)
        print("Completed")