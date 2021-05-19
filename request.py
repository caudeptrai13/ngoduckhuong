import requests
import json

url = "https://api.covid19api.com/summary"


class DownloadCovidInfo:
    def __init__(self, url):
        self.req = __import__('requests')
        self.url = url

    def get_all_data(self):
        return self.req.get(self.url).json()

    def get_data_by_country(self,country):
        data = self.get_all_data()
        return list(filter(lambda x : x["Country"] == country, data["Countries"]))

    def save_to_file(self, file):
        with open(file,"w") as f:
            f.write(json.dumps(self.get_all_data(),indent=4))

a = DownloadCovidInfo(url)
print(a.get_all_data())
print(a.get_data_by_country("Viet Nam"))
a.save_to_file("data.txt")