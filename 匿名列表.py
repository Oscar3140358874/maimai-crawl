import requests
from bs4 import BeautifulSoup
import json

url = 'https://maimai.cn/sdk/web/content/get_list'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
           'Cookie': 'HWWAFSESID=82e30974cdc62f64e0; HWWAFSESTIME=1720809468292; seid=s1720809470524; guid=GBwaHRBMT0sSEB5PTxkQHhgaGhBLSRNOEE8THEwQS08ZSxAdHxISVh0fGhIaHRpWHBkEHRkfBUNYS0xLeQoaBBoEGgQcGBsFT0dFWEJpCgNFQUlPbQpPQUNGCgZmZ35iYQIKHBkEHRkfBV5DYUhPfU9GWlprCgMddR8bdRobCnIKeWUKSUtnCkZPXkRjChFCWUVeRENJS2cCChoEHwVLRkZDUEVn; AGL_USER_ID=579f26fc-d74c-4b56-bf00-670216a8606a; _buuid=d52f2e12-2c9d-4e84-8a62-b8290d3e13f9; browser_fingerprint=1D8BA63D; maimai_pc_login_show_tooltip=1; u=242083468; u.sig=4NLrWuh2D1JROtnfnNQzRyI1yfA; access_token=1.bcb448e7e7c66762433a4001ccd7a401; access_token.sig=HKjYcLJRSFwFP2R4xuN5_D2H4gc; u=242083468; u.sig=4NLrWuh2D1JROtnfnNQzRyI1yfA; access_token=1.bcb448e7e7c66762433a4001ccd7a401; access_token.sig=HKjYcLJRSFwFP2R4xuN5_D2H4gc; channel=www; channel.sig=tNJvAmArXf-qy3NgrB7afdGlanM; maimai_version=4.0.0; maimai_version.sig=kbniK4IntVXmJq6Vmvk3iHsSv-Y; session=eyJzZWNyZXQiOiJUaFpybTNpenhtTUVRclRkcHdPSWN5LWQiLCJ1IjoiMjQyMDgzNDY4IiwiX2V4cGlyZSI6MTcyMDg5NzgyNjU0OCwiX21heEFnZSI6ODY0MDAwMDB9; session.sig=DLpG5JJJv7z20Mk80u4nmEpQJQM; maimai_pc_chat_max_mid=1911008441; csrftoken=eFi6vrqD-7WuADWpTiEO2-xZaWCfWoceJGAs',
           'Referer': 'https://maimai.cn/gossip_list',
           'X-Csrf-Token': 'eFi6vrqD-7WuADWpTiEO2-xZaWCfWoceJGAs'}


def change_page_number(number: int):

    params = {'api': 'gossip/v3/square',
              'u': '242083468',
              'page': number,
              'before_id': 0}
    result = []
    re = requests.get(url, params=params, headers=headers)
    data = json.loads(re.text)
    for text in data['list']:
        result.append(text['text'])
    return result

with open('脉脉职言2.txt', 'w') as fout:
    for i in range(1, 11):
        print('craw_page', i)
        result = change_page_number(i)
        fout.write('\n'.join(result))
