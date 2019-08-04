from abc import ABC

class abstractVirusTotalRequesterManager(ABC):

    def __init__(self, ip_list):
        self.ip_list = ip_list

    def run(self):
        pass

    def requestVirusTotal(self, ip):
        # ip_url = r"https://www.virustotal.com//ui/urls/{}?relationships=last_serving_ip_address,network_location".format(ip)
        # import requests
        # req = requests.get(url=ip_url)
        # data_json = req.json()
        import json
        # read file
        with open(r"C:\Users\stavl\PycharmProjects\CyberBit\data.json", 'r') as myfile:
            data = myfile.read()
        # parse file
        data_json = json.loads(data)
        return data_json






