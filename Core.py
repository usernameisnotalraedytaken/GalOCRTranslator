# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 00:11:54 2020

@author: Admin
"""

tt=''

def trans_from_pic(filename):
    from aip import AipOcr
    
    """ 你的 APPID AK SK """
    APP_ID = '11791470'	
    API_KEY = 'UvHEHNW5Y2w536stRBE3CphB'
    SECRET_KEY = '74mxYmwu9SS5mG2tbSFp37YUilVXPt85'
    
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    
    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()
    
    image = get_file_content(filename)
    
    options = {}
    options["language_type"] = "JAP"
    
    ocr_result = client.basicGeneral(image, options)
    
    print('ocr_result=')
    print(ocr_result)
    
    len = ocr_result['words_result_num']
    
    text = ''
    
    for i in range(0,len):
        text += ocr_result['words_result'][i]['words']
    
    #print('text=')
    #print(text)
    tt=text
    #print('Translated=')
    
    import http.client
    import hashlib
    import urllib
    import random
    import json
    
    appid = '20180909000204654'  # 填写你的appid
    secretKey = 'NXpfmci5MwrUTmE05MPN'  # 填写你的密钥
    
    httpClient = None
    myurl = '/api/trans/vip/translate'
    
    fromLang = 'jp'   #原文语种
    toLang = 'zh'   #译文语种
    salt = random.randint(32768, 65536)
    q= text
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
    salt) + '&sign=' + sign
    
    
    httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
    httpClient.request('GET', myurl)
    # response是HTTPResponse对象
    response = httpClient.getresponse()
    result_all = response.read().decode("utf-8")
    result = json.loads(result_all)
    
    httpClient.close()
    if(result!={'error_code': '54000', 'error_msg': 'PARAM_FROM_TO_OR_Q_EMPTY'}):
        return result
    else:
        return 'Error!'

def google_trans(src):
    url = 'http://translate.google.cn/translate_a/single?client=gtx&dt=t&dj=1&ie=UTF-8&sl=ja_JP&tl=zh_CN&q=' + src
    import requests as r
    return r.get(url).json()

def youdao_trans(src):
    import requests as r
    return r.get('http://fanyi.youdao.com/translate?&doctype=json&type=JA2ZH_CN&i=' + src).json()['translateResult'][0]

import pyautogui as pag
input('Enter.');
x1,y1 = pag.position() #返回鼠标的坐标
input('Enter.');
x2,y2 = pag.position() #返回鼠标的坐标

print('Get.(',x1,',',y1,'),(',x2,',',y2,')')

from PIL import ImageGrab
 

import os

def Main():
    os.system('cls')
    img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    img.save('Image.jpg','JPEG')
    rq = trans_from_pic('Image.jpg')
    print(rq)
    if(rq=='Error!'):
        print(rq)
        return
    for i in rq['trans_result']:
        #print(i['src'])
        #print(i['dst'])
        print('--------')
        print('--------')
        #print()
        print('Text:')
        print(i['src'])
        print('Roman conversion:')
        from pykakasi import kakasi,wakati
         
        text = i['src']
        kakasi = kakasi()
        kakasi.setMode("H","a") # Hiragana to ascii, default: no conversion
        kakasi.setMode("K","a") # Katakana to ascii, default: no conversion
        kakasi.setMode("J","a") # Japanese to ascii, default: no conversion
        kakasi.setMode("r","Hepburn") # default: use Hepburn Roman table
        kakasi.setMode("s", True) # add space, default: no separator
        kakasi.setMode("C", True) # capitalize, default: no capitalize
        conv = kakasi.getConverter()
        result = conv.do(text)
        print(result)
        print()
        print('Translated:')
        print('Baidu:')
        print(i['dst'])
        print('Google:')
        print(google_trans(i['src'])['sentences'][0]['trans'])
        print('Youdao:')
        for ii in youdao_trans(i['src']):
            print(ii['tgt'], end='')
        print()
        print()
        img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        img.save('Image.jpg','JPEG')
        #input('Press Enter to continue')
        
from pynput import keyboard

def on_press(key):
    try:
        print('{0} pressed.'.format(key.char))
    except AttributeError:
        if(key == keyboard.Key.enter):
            import time
            time.sleep(0.3)
            Main()
        if(key == keyboard.Key.space):
            return False
        if(key == keyboard.Key.backspace):
            input('Enter.');
            x1,y1 = pag.position() #返回鼠标的坐标
            input('Enter.');
            x2,y2 = pag.position() #返回鼠标的坐标

            print('Get.(',x1,',',y1,'),(',x2,',',y2,')')
        if(key == keyboard.Key.left):
            Main()
        
with keyboard.Listener(on_press=on_press) as l:
    l.join()