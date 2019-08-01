import sys
import configparser
import logging
from collections import namedtuple

class configurationRepository:
    "class is user to read all configuration from config file"    

    def __init__(self):
        self.configFileName = "config.ini"
        self.config = configparser.ConfigParser()
        self.config.read(self.configFileName)

    def getDatabaseConnectionString(self): 
        try:
            connStr = (
                'DRIVER={{{0}}};'
                'SERVER={1};'
                'DATABASE={2};'
                'Integrated Security={3}').format(
                    self.config['DEFAULT']['Driver'], 
                    self.config['DEFAULT']['Server'], 
                    self.config['DEFAULT']['Database'],                
                    self.config['DEFAULT']['IntegratedSecurity'])
            return connStr
        except:
            logging.error("Error while reading config file: {}".format(sys.exc_info()))
            raise
            
    def getEmailSendingOptions(self):       
        try:
            emailSendingOptions = namedtuple("emailSendingOptions", ["sender", "receiver", "subject", "address", "port", "user", "password"])
            return emailSendingOptions(
                self.config['EMAIL']['Sender'], 
                self.config['EMAIL']['Receiver'], 
                self.config['EMAIL']['Subject'], 
                self.config['EMAIL']['Address'], 
                self.config['EMAIL']['Port'],
                self.config['EMAIL']['User'],
                self.config['EMAIL']['Password'])
        except:
            logging.error("Error while reading config file: {}".format(sys.exc_info()))
            raise