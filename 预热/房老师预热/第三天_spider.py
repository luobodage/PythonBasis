import requests

url = 'https://cn-hljheb-cmcc-bcache-02.bilivideo.com/upgcxcode/81/80/265738081/265738081_nb2-1-16.mp4?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&uipk=5&nbs=1&deadline=1608195278&gen=playurl&os=bcache&oi=1971861732&trid=5768d07eaf4a4b9ca3f47a5df80a35abh&platform=html5&upsig=c7b8f2d967103ff8e9b918d72160075f&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&cdnid=40089&mid=27860107&logo=80000000'

content = requests.get(
    url=url,
    # headers={
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
    # }
).content

with open('shipin.mp4', 'wb') as f:
    f.write(content)
