import sys
#import Logger

#global g_logger
from VirusTotal.SimpleQueryManager import SimpleQueryManager


class VirusTotalManager:

    def __init__(self, ips_path):
        self.ips_path= ips_path

    def run(self):
        self.read()
        self.runVirusTotalManagerQuery()

    def read(self):
        with open(self.ips_path) as file:  # Use file to refer to the file object
            self.ip_list = file.read().split(",")
            print(self.ip_list)
            return

    def runVirusTotalManagerQuery(self):
         QueryManager = SimpleQueryManager(self.ip_list)
         QueryManager.run()


    def writeData(self):
        pass


def main(args):
    vt_manager = VirusTotalManager("ip_list.txt")
    vt_manager.run()

if __name__ == "__main__":
    main(sys.argv[1:])
