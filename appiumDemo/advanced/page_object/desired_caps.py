from appium import webdriver
import yaml
import logging
import logging.config
from os import path
base_dir = path.dirname(path.abspath(__file__))
log_file_path = path.join(base_dir, 'log.conf')
logging.config.fileConfig(log_file_path)
# CON_LOG='./log.conf'
logging=logging.getLogger()

def appium_desired():
    desired_caps_path = path.join(path.dirname(path.abspath(__file__)), 'desired_caps.yaml')
    with open(desired_caps_path, 'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)

    desired_caps={}
    desired_caps['platformName']=data['platformName']
    desired_caps['platformVersion']=data['platformVersion']
    desired_caps['deviceName']=data['deviceName']

    desired_caps['appPackage']=data['appPackage']
    desired_caps['appActivity']=data['appActivity']
    desired_caps['noReset']=data['noReset']

    desired_caps['unicodeKeyboard']=data['unicodeKeyboard']
    desired_caps['resetKeyboard']=data['resetKeyboard']

    logging.info('start app...')
    driver=webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub',desired_caps)
    driver.implicitly_wait(8)
    return driver

if __name__ == '__main__':
    appium_desired()

