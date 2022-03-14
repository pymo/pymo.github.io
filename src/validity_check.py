#!/usr/bin/python3

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

    def analyze(self, link):
        resultDict = self.disabledLink(link)
        if resultDict["code"] == 0:
            print("Exception")
            print(resultDict.get("status"))
        else:
            try:
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
  valid = BaiduNetdisk().analyze(game_entry['download_link'])
  if valid:
    print("OK      ",game_entry['title'])
  else:
    print("Invalid ",game_entry['title'])


