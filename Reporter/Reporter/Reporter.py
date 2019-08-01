import logging

from repositories.aircraftRepository import aircraftRepository
from reportGenerator import reportGenerator
from htmlFormatter import htmlFormatter
from emailSender import emailSender

logging.basicConfig(filename='log.log',level=logging.DEBUG)

reportItems = reportGenerator().generateEuropeanAircraftReportItems()
europeReport = htmlFormatter().createEuropeanAircraftReport(reportItems, "Aircrafts from Europe countries")

reportItems = reportGenerator().generateNonEuropeanAircraftReportItems()
nonEuropeReport = htmlFormatter().createEuropeanAircraftReport(reportItems, "Aircrafts from NON Europe countries")

emailSender().sendAutomaticEmailEmail(europeReport + " " + nonEuropeReport)

