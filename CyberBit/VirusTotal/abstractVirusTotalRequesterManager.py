from abc import ABC

class abstractVirusTotalRequesterManager(ABC):

    def __init__(self, ip_list):
        self.ip_list = ip_list

    def run(self):
        pass

    def requestVirusTotal(self, ip):
        import requests
        malicius_url = ip
        json_url = r"https://www.virustotal.com/ui/search?relationships%5Bcomment%5D=author%2Citem&relationships%5Burl%5D=network_location%2Clast_serving_ip_address&limit=20&query=http%3A%2F%2F{}%2F".format(
            malicius_url)
        req = requests.get(url=json_url)
        data_json = req.json()
        return data_json





