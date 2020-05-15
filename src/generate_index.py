#!/usr/bin/python3

import json

game_db=[]
with open('gamedb.json','r', encoding='utf-8-sig') as fp:
  game_db=json.load(fp)

output=[]
for game_entry in game_db:
  game_id = str(game_entry['game_id'])
  output.append('<!-- ------------------------------------------------------------------------------ -->')
  output.append('<span onclick="toggle_visibility(\'gameid'+game_id+'\')" class="toggleheader">')
  output.append('<table class="gametitle_table"><tr><td class="gametitle_table_td1"><u>'+game_entry['title']+'</u></td>')
  platforms = ""
  for platform in game_entry['platforms']:
    platforms+='<img src="images/'+platform+'.png">'
  output.append('<td class="gametitle_table_td3">'+platforms+' 发布日期：'+game_entry['publish_date']+'</td></tr>')
  output.append('</table></span>')
  output.append('<div style="display:none" id="gameid'+game_id+'" H="'+('y' if game_entry['contains_h'] else 'n')+'" class="togglebody">')
  if game_entry['publish_site']:
    output.append('移植发布地址：<a href='+game_entry['publish_site']+'>'+game_entry['publish_site']+'</a><br>')
  if 'author' in game_entry and game_entry['author']:
    output.append('移植者：'+game_entry['author']+'<br>')
  output.append('<h3>游戏介绍</h3>')
  output.append(game_entry['introduction'])
  if game_entry['download_link']:
    output.append('<div class="dllink"><h3>游戏下载</h3>')
    output.append('下载链接：<a href="'+game_entry['download_link']+'"  target="_blank">'+game_entry['download_link']+'</a> 提取码: '+game_entry['download_pass'])
    if 'unzip_pass' in game_entry:
      output.append(' 解压密码: '+game_entry['unzip_pass'])
    output.append('</div>')
  if 'screenshots' in game_entry and len(game_entry['screenshots']) > 0:
    output.append('<h3>游戏截图</h3><div class="screenshots">')
    for screenshot in game_entry['screenshots']:
      output.append('<img src="images/grey.gif" style="max-height: 360px" data-original="'+screenshot+'">')
    output.append('</div>')
  output.append('</div>')

with open('index.template','r', encoding='utf-8-sig') as fp:
  data = fp.read()
  game_table_str='\n'.join(output)
  data = data.replace('GAME_TABLE_HERE',game_table_str,1)

with open('index_real.html','w') as fp:
  fp.write(data)
