from appium import webdriver
import yaml

with open('desired_caps.yaml', 'r', encoding='utf-8') as f:
    data = yaml.load(f,Loader=yaml.FullLoader)

desired_caps={}
desired_caps['platformName']=data['platformName']
desired_caps['platformVersion']=data['platformVersion']
desired_caps['deviceName']=data['deviceName']

desired_caps['appPackage']=data['appPackage']
desired_caps['appActivity']=data['appActivity']
desired_caps['noReset']=data['noReset']

driver=webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub',desired_caps)