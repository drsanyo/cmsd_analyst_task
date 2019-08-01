import sys
import pyodbc

class aircraftRepository:
    "class used to retrieve aircrat data"
    __connStr = ""

    def __init__(self):
        self.__connStr = (
            'DRIVER={SQL Server Native Client 11.0};'
            'SERVER=(localdb)\MSSQLLocalDB;'
            'Integrated Security=true')
        
    def retrieveAircraftDetails(self):
        try:
            conn = pyodbc.connect(self.__connStr, autocommit=True)
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Warehouse.dbo.vw_aircraft_details')
            return list(cursor.fetchall())
        except:
            print("Failed to get record from database: {}".format(error))
        finally:
            cursor.close()
            conn.close()                

