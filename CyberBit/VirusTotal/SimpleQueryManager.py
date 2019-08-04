from time import sleep
from VirusTotal.abstractVirusTotalRequesterManager import abstractVirusTotalRequesterManager

class SimpleQueryManager(abstractVirusTotalRequesterManager):

    def __init__(self, ip_list):
        abstractVirusTotalRequesterManager.__init__(self, ip_list)

    def run(self):
        self.runVirusTotalSimpleQuery()


    def runVirusTotalSimpleQuery(self):
        for ip in self.ip_list:
            data_json=self.requestVirusTotal(ip)
            sleep(25)








