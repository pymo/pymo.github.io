import csv
import json
import os
import urllib.request
import time

from bs4 import BeautifulSoup

class BaiduNetdisk(object):

    def __init__(self):
        pass

    def disabledLink(self, link):
        """
        :param link: baiduNetdisk download Link
        :return: 0-False / html-True
        """
        try:
            headers = {
                'User-Agent': 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)'
            }

            req = urllib.request.Request(url=link, headers=headers, method='GET')
            response = urllib.request.urlopen(req, None, 8)
            html = response.read()
            return {"code": 1, "status": html}
        except Exception as e:
            return {"code": 0, "status": e.__str__()}

    def anylies(self, link):
        resultDict = self.disabledLink(link)
        if resultDict["code"] == 0:
            print("Exception")
            print(resultDict.get("status"))
        else:
            try:
                # print(resultDict.get("status").decode('utf-8'))
                # ak = str(resultDict.get("status"),encoding = "utf8")
                # print(type(resultDict.get("status")))
                # for i in range(len(ak)):
                #     print(ak[i])
                soup = BeautifulSoup(resultDict.get("status"), 'html.parser') 
                count = 0
                for k in soup.find_all('div', class_='share-error-left'):
                    count += 1
                if count == 0:
                    return True
                else:
                    return False

            except Exception as e:
                print("302：", e.__str__())

game_db=[]
with open('gamedb.json','r', encoding='utf-8-sig') as fp:
  game_db=json.load(fp)
for game_entry in game_db:
  just = BaiduNetdisk().anylies(game_entry['download_link'])
  if just:
    print("\n ------- ",game_entry['title'], " OK")
  else:
    print("\n ------- ",game_entry['title'], " Invalid")


