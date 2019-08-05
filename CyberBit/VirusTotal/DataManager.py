from abc import ABC

class DataManager:

    def __init__(self):
        self.json_data_list= []

    def add_json_data(self,data_json):
        self.json_data_list.append(data_json)

    def display_json_data(self):
        ip_list =[]
        is_mal_list = []
        import pandas as pd
        for data in self.json_data_list:
            ip = data["data"][0]["attributes"]["last_final_url"]
            ip_list.append(ip)
            is_malicious = self.isMalicious(data)
            is_mal_list.append(is_malicious)

        print(pd.DataFrame({'IP url': ip_list, 'Is malicious': is_mal_list}))

    def isMalicious(self, json_data):
        last_analysis_stats = json_data["data"][0]["attributes"]["last_analysis_stats"]
        if (last_analysis_stats["malicious"]!=0) or (last_analysis_stats["suspicious"]!=0):
            return True
        else:
            return False








