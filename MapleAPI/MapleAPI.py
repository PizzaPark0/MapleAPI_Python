import requests

class MapleAPI:
    def __init__(self, api_key):
        self.key = api_key

    def getCharOcid(self, nickname : str) -> str: #get identifier from nickname
        resp = requests.get(
            url="https://open.api.nexon.com/maplestory/v1/id",
            headers={"x-nxopen-api-key" : self.key},
            params={"character_name" : nickname}
            )
        if resp.status_code != 200:
            return resp.json().get("error").get("message") #error message (string)
        else:
            return resp.json().get("ocid") #ocid (string)

    def getOguildId(self, guildname : str, worldname : str) -> str: #get identifier from guildname
        resp = requests.get(
            url=f"https://open.api.nexon.com/maplestory/v1/guild/id",
            headers={"x-nxopen-api-key" : self.key},
            params={"guild_name" : guildname, "world_name" : worldname}
            )
        if resp.status_code != 200:
            return resp.json().get("error") #error code (dict)
        else:
            return resp.json().get("oguild_id") #oguild_id (string)

    def getCharData(self, ocid : str, date : str, dataType : str) -> dict:
        '''
        [date]
        "YYYY-MM-DD" format string, after 2023-12-21, before a day ago
        
        [dataType]
        basic, popularity, stat, hyer-stat, propensity, ability, item-equiment,
        cashitem-equipment, symbol-equipment, set-effect, beauty-equipment, pet-equipment,
        skill, link-skill, vmatrix, hexametrix, hexametrix-stat, dojang
        '''
        resp = requests.get(
            url=f"https://open.api.nexon.com/maplestory/v1/character/{dataType}",
            headers={"x-nxopen-api-key" : self.key},
            params={"ocid" : ocid, "date" : date}
            )

        return resp.json() #get data

    def getGuildData(self, oguild_id : str, date : str, dataType : str) -> dict:
        '''
        [date]
        "YYYY-MM-DD" format string, after 2023-12-21, before a day ago
        
        [dataType]
        basic
        '''
        resp = requests.get(
            url=f"https://open.api.nexon.com/maplestory/v1/guild/{dataType}",
            headers={"x-nxopen-api-key" : self.key},
            params={"oguild_id" : oguild_id, "date" : date}
            )

        return resp.json() #get data

    def getUnionData(self, ocid : str, date : str, dataType : str) -> dict:
        '''
        [date]
        "YYYY-MM-DD" format string, after 2023-12-21, before a day ago
        
        [dataType]
        union, union-raider
        '''
        resp = requests.get(
            url=f"https://open.api.nexon.com/maplestory/v1/user/{dataType}",
            headers={"x-nxopen-api-key" : self.key},
            params={"ocid" : ocid, "date" : date}
            )

        return resp.json() #get data

if __name__=="__main__":
    f = open("set.txt", "r")
    apiKey = f.readline().split(':')[1].strip()
    f.close()
    a = MapleAPI_Viewer(apiKey)

    x = a.getCharOcid("이름")
    print(x)
