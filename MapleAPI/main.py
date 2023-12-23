import MapleAPI
import time

with open("set.txt", "r") as f:
    apiKey = f.readline().split(':')[1].strip()

viewer = MapleAPI.MapleAPI(apiKey)
oGuildId = viewer.getOguildId("길드명", "서버명")
guildMembers = viewer.getGuildData(oGuildId, "2023-12-22", "basic").get("guild_member")
guildMembers_ocid = [  ]

c=0
for i in guildMembers:
    if viewer.getCharOcid(i) == 'Please input valid parameter':
        print(i)
        c+=1
    #guildMembers_ocid.append()
print(c)

print(guildMembers)
print(guildMembers_ocid)
