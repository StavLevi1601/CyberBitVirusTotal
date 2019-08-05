from time import sleep

from VirusTotal.DataManager import DataManager
from VirusTotal.abstractVirusTotalRequesterManager import abstractVirusTotalRequesterManager

class SimpleQueryManager(abstractVirusTotalRequesterManager):

    def __init__(self, ip_list):
        abstractVirusTotalRequesterManager.__init__(self, ip_list)

    def run(self):
        self.runVirusTotalSimpleQuery()


    def runVirusTotalSimpleQuery(self):
        dataManager = DataManager()
        for ip in self.ip_list:
            data_json=self.requestVirusTotal(ip)
            #sleep(25)
            dataManager.add_json_data(data_json)
        dataManager.display_json_data()








