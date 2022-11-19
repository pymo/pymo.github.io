#!/usr/bin/python3

import csv
import json
import os
import urllib.request
import subprocess
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

current_path = os.path.dirname(os.path.abspath(__file__))
game_db = []
with open(os.path.join(current_path,'gamedb.json'),'r', encoding='utf-8-sig') as fp:
  game_db = json.load(fp)
#Failed links will get retried up to 3 times.
for retry in range(3):
  invalid_games = []
  for game_entry in game_db:
    valid = BaiduNetdisk().analyze(game_entry['download_link'])
    if not valid:
      invalid_games.append(game_entry)
  game_db = invalid_games
if invalid_games:
  email_subject = "pymo game download link broken"
  email_body = "The following games become invalid:\n\n"
  for game_entry in invalid_games:
    email_body += game_entry['title']+"\n"
  subprocess.call(["mailme.sh", email_subject, email_body])
  print(email_body)
else:
  print("All pass.")

