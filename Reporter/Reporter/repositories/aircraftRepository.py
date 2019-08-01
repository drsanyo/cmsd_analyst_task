import sys
import pyodbc
import logging
from repositories.configurationRepository import configurationRepository

class aircraftRepository:
    "class used to retrieve aircrat data"
    __connStr = ""

    def __init__(self):        
        self.__connStr = configurationRepository().getDatabaseConnectionString()
        
    def retrieveAircraftDetails(self):
        try:
            conn = pyodbc.connect(self.__connStr, autocommit=True)
            cursor = conn.cursor()
            cursor.execute(
                ('SELECT * FROM dbo.vw_aircraft_details '
                 'ORDER BY [CONTINENT], [BELONGS_TO_EU] DESC, [COMPANY_COUNTRY_CODE], '
                 '[OWNER_COMPANY_NAME], [MODEL_NUMBER], [TAIL_NUMBER]'))
            return list(cursor.fetchall())
        except pyodbc.Error as ex:
            logging.error("Failed to get record from database: {}".format(ex))
            raise
        finally:
            cursor.close()
            conn.close()                

