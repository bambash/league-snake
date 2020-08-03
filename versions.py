import requests


class DataDragon:
    # constants
    endpoint = "https://ddragon.leagueoflegends.com"

    def __init__(self, realm):
        self.realm = realm
        self.realm = requests.get(
            f"{self.endpoint}/realms/{self.realm}.json").json()
        self.versions = requests.get(
            f"{self.endpoint}/api/versions.json").json()
        self.latest = self.versions[0]
        self.champions = requests.get(
            f"{self.endpoint}/cdn/{self.latest}/data/en_US/champion.json").json()
