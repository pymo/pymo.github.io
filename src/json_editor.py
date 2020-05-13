import json
import os
import re

game_db=[]
with open('gamedb.json','r', encoding='utf-8-sig') as fp:
  game_db=json.load(fp)
html_info=dict()
with open('input.txt','r', encoding='utf-8-sig') as fp:
  for line in fp.readlines():
    items = line.strip().split(',')
    if len(items) == 4:
      baidu_folder = items[0]
      html_info[baidu_folder]=items[1:]
    else:
      raise Exception("Failed to parse "+line)
print(html_info)
for game_entry in game_db:
  baidu_folder = game_entry['baidu_folder']
  if baidu_folder in html_info:
    print('Modifying game ',game_entry['game_id'],game_entry['baidu_folder'])
    download_link, download_pass, unzip_pass = html_info[baidu_folder]
    game_entry['download_link']=download_link
    game_entry['download_pass']=download_pass
    game_entry['unzip_pass']=unzip_pass
game_db.sort(key=lambda x: x['publish_date'], reverse=True)
with open('gamedb_new.json','w') as fp:
  json.dump(game_db, fp, ensure_ascii=False, sort_keys=True, indent=2)
