# -*- coding: UTF-8 -*-

# author: luoboovo
# contact: fuyu16032001@gmail.com
# datetime: 2021/05/11
# software: PyCharm
#         =    =     =
#          =   =   =
#           =  =  =
#         ===========
#         =   萝    =
#         =   卜    =
#         =   神    =
#         =   保    =
#         =   佑    =
#         =   永    =
#         =   无    =
#         =   bug  =
#          =      =
#           =    =
#              =
import re

import requests
import json
import urllib.parse

frist_response = requests.get(
    url='https://app.bilibili.com/x/v2/feed/index?ad_extra=47964AFAF9F5B9AC82CBECCF0B4E6E883D61DEAE7DA7220530D50BE74C1B94EE0C0E2749461988D812F6878235988B6B9FA69AEE0BDFC07A65B560BBCE856F4A3F83EEFAC124866D2A19D3D1FF264CEDED0C3E2EF4019529F2891824CD0DD74755683B700D306CEDA9A44AC1C55EBBFE047E1ECB09EED40C7E8708E89D50040AD2026A8B4E02645ABA990D53C3F46FAC921367F43AF189FCCDF42F913F4110CEE2A40A26D6A42A2FD67190DE202F2C1E2CD4155C11F095BE2E31A50A1E7CCAFC507338ED2F7CFCAFF5142CB506A33B17B79AFE19787550654B3167DE9F9B474EAAE6FED95A901966B392DE28F9CACB807599B0B0D6B59DBF59F38C28B76CEB2C7529696B22CD58CDABC8F73894F4DB6661E8E2FEC7C67CFED5DB1408BF4CD6A59FDD83D2CD59BAD02A6CC4FB02A27317AE5FA7904BFFA7B76860FBF9D6CFEE7F692AB276C827A02937DCFC1F29FB7EB822945B1D40256D8377C8E5B86E420AE38DC37960C1A91952B3007BF03BADC07FBB0F0A8254D7A6F0B639C3AA3325481ABB0D5AF4D5DE3A1C16FEC8C82685FF946E23A8B95EA3AC21F6A6FBDBFA3347938880FD71F4BD0B4C4FEC6E29B83D51986A78734B4C9B0EE3A77ECB5ED6407CD13BA1E2C4C50C6BACAC7C60175774C46DE1D8E2B8B8BA57872E625215B0E9252F47A2250D503C6D2AAC49DF20D07D3BCD9CCAED297B0B9C63EC5C2AA6A72AE6F2DB395D3D89FE02E5ED1C406217CA6C6155E2AD7582EEBAAA03288CA5C9AA0CF04600EC6276114539BB6C999AE9352B99480CBCACC6E52467AFB31FB20A3DF9A9&appkey=1d8b6e7d45233436&autoplay_card=11&banner_hash=14522199998192363983&build=6235200&c_locale=zh_CN&channel=bili&column=2&device_name=SM-G9550&device_type=0&flush=6&fnval=272&fnver=0&force_host=0&fourk=0&guidance=0&https_url_req=0&idx=1620715342&inline_danmu=2&inline_sound=1&login_event=0&mobi_app=android&network=wifi&open_event=&platform=android&player_net=1&pull=true&qn=32&recsys_mode=0&s_locale=zh_CN&splash_id=&statistics=%7B%22appId%22%3A1%2C%22platform%22%3A3%2C%22version%22%3A%226.23.5%22%2C%22abtest%22%3A%22%22%7D&ts=1620715400&sign=741cf11b0dbbd79bea68b680c0b31140')
# a = json.loads(frist_response.json())
url_list = []

for i in range(len(frist_response.json()['data']['items'])):
    url_list.append(frist_response.json()['data']['items'][i]['uri'])

url_deconde = []
for i in url_list:
    url_deconde.append(re.findall(r'player_preload=(.*?)&player_rotate', urllib.parse.unquote(i))[0])

print(url_deconde[0])
json_url = json.loads(url_deconde[0])

video_list = []
audio_list = []

for i in range(len(json_url['dash']['video'])):
    video_list.append(json_url['dash']['video'][i]['base_url'])

for i in range(len(json_url['dash']['audio'])):
    audio_list.append(json_url['dash']['audio'][i]['base_url'])

print(video_list)
print(audio_list)

# video_url = json_url['dash']['video'][0]['base_url']
# audio_url = json_url['dash']['audio'][0]['base_url']

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Mobile Safari/537.36'
}
for i, v in enumerate(video_list):
    content = requests.get(url=v, headers=headers).content
    with open(f'video{i}.mp4', 'wb') as f:
        f.write(content)

for i, v in enumerate(audio_list):
    content = requests.get(url=v, headers=headers).content
    with open(f'audio{i}.mp4', 'wb') as f:
        f.write(content)

# content = requests.get(url=video_url, headers=headers).content
# a_content = requests.get(url=audio_url, headers=headers).content
#
# with open('video7.mp4', 'wb') as f:
#     f.write(content)
# with open('audio7.mp3', 'wb') as f:
#     f.write(content)
# for i in url_deconde:
#     print(json.loads(i))
# import ffmpeg
# import subprocess



# ffmpeg.concat(ffmpeg.input('video6.mp4'), ffmpeg.input('audio6.mp4'), v=1, a=1).output('video_late6.mp4').run()
# subprocess.run("ffmpeg -i video6.mp4 -i audio6.mp3 -c copy output.mp4")
