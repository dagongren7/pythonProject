from selenium.webdriver.support.ui import WebDriverWait
import configparser,os
class ObjectMap(object):
    def __init__(self):
        self.uiObjMapPath = os.path.dirname(os.path.abspath(__file__))+"\\UiObjectMap.ini"
        print(self.uiObjMapPath)
    def getElementObject(self,driver,weSiteName,elementName):
        try:
            cf = configparser.ConfigParser()
            cf.read(self.uiObjMapPath)
            locators = cf.get(weSiteName,elementName).split(">")
            print("locators=",locators)
            locatorMethod = locators[0]
            locatorExpression = locators[1]
            element = WebDriverWait(driver,10).until(lambda x: x.find_element(locatorMethod,locatorExpression))
        except Exception as e:
            raise e
        else:
            return element
            
            
            
            
            
            
            
            
            
            
            
            
            