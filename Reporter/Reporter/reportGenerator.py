import sys
from repositories.aircraftRepository import aircraftRepository

class reportGenerator:
    "class generates reports"
    def __init__(self):
        self.aircraftRepository = aircraftRepository();

    def generateEuropeanAircraftReportItems(self):
        aircrafts = self.aircraftRepository.retrieveAircraftDetails()                        
        return [aircraft for aircraft in aircrafts if aircraft.CONTINENT == "Europe"]

    def generateNonEuropeanAircraftReportItems(self):
       aircrafts = self.aircraftRepository.retrieveAircraftDetails()        
       return [aircraft for aircraft in aircrafts if aircraft.CONTINENT != "Europe"]