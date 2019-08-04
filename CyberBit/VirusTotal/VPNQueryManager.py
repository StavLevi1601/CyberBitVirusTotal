from VirusTotalRequesterManager import VirusTotalRequesterManager

class VPNQueryManager(VirusTotalRequesterManager):

    def __init__(self,ip_list):
        VirusTotalRequesterManager.__init__(self,ip_list)

    def virusTotalQuery(self):
        pass



