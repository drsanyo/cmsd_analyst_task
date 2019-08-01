import sys

import repositories.aircraftRepository as aircraftRepository


repo = aircraftRepository.aircraftRepository()
aircraftDetails = repo.retrieveAircraftDetails()

for row in aircraftDetails:
    print(
        row.TAIL_NUMBER + " - " 
        + row.TAIL_NUMBER + " - " 
        + row.MODEL_NUMBER + " - " 
        + row.MODEL_DESCRIPTION + " - " 
        + row.OWNER_COMPANY_NAME + " - " 
        + row.COMPANY_COUNTRY_CODE + " - " 
        + row.COMPANY_COUNTRY_NAME)
