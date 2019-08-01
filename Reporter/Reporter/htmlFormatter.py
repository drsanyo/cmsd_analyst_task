import os
import constants

class htmlFormatter:
    def createAircraftReport(self, reportItems, reportName):
        tableLines = self.__makeTableRows(reportItems)
        table = self.__makeTable(tableLines, reportName)
        page = self.__makePage(table)
        return page

    def __makePage(self, table):
        page = constants.pageTemplate.replace("{0}", table)
        return page 

    def __makeTable(self, gridLines, reportName):
        table =  constants.tableTemplate.format(
            reportName,
            gridLines)
        return table


    def __makeTableRows(self, reportItems):
        gridRows = ""
        for item in reportItems:
            color = self.__getLineColor(item)
            gridRow = constants.rowTemplate.format(
                item.TAIL_NUMBER,
                item.MODEL_NUMBER,
                item.MODEL_DESCRIPTION,
                item.OWNER_COMPANY_NAME,
                item.COMPANY_COUNTRY_CODE,
                item.COMPANY_COUNTRY_NAME,
                color);
            gridRows = gridRows + os.linesep + gridRow;
        return gridRows



    def __getLineColor(self, item):    
        if (item.CONTINENT == "Europe"):
            if (item.BELONGS_TO_EU == "T"):
                return "#ADD8E6" #light blue
            else:
                return "#F08080" #light red
        else:
            return "#D3D3D3" #light gray