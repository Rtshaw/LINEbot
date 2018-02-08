# -*- coding: utf-8 -*-

import requests
import random
from lxml import etree
from bs4 import BeautifulSoup
from flask import Flask, request, abort
from imgurpython import ImgurClient

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# get channel_secret and channel_access_token from environment variable

channel_secret = 'channel_secret'
channel_access_token = 'channel_access_token'

# push_token = user_id
user_id = 'user_id'

client_id = 'client_id'  # imgur client id
client_secret = 'client_secret'  # imgur client secret

album_id_beauty = 'album_id_beauty'  # imgur album id
album_id_cat = 'album_id_cat'  # imgur album id
album_id_2d = 'album_id_2d' # imgur album id

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)


url_btc = 'https://www.coingecko.com/zh-tw/%E5%8C%AF%E7%8E%87%E5%9C%96/%E6%AF%94%E7%89%B9%E5%B9%A3/twd'
url_eth = 'https://www.coingecko.com/zh-tw/%E5%8C%AF%E7%8E%87%E5%9C%96/%E4%BB%A5%E5%A4%AA%E5%B9%A3/twd'
url_zec = 'https://www.coingecko.com/zh-tw/%E5%8C%AF%E7%8E%87%E5%9C%96/zcash/twd'

# BTC
def get_btc_price(own):
    s = requests.Session()
    r = requests.get(url_btc)
    soup = BeautifulSoup(r.text, 'lxml')
    currency_btc = soup.find(class_= "table")
    currency_btc = currency_btc.find_all('td')[1].text
    currency_btc = float(currency_btc)
    own = float(own)
    exchange_btc = format(own*currency_btc, '0.2f')
    
    return exchange_btc

def get_now_btc_exchange():
    s = requests.Session()
    r = requests.get(url_btc)
    soup = BeautifulSoup(r.text, 'lxml')
    currency_btc = soup.find(class_="table")
    currency_btc = currency_btc.find_all('td')[1].text
    currency_btc = "市場均價為台幣 "+currency_btc+" 元"
    
    return currency_btc

# ETH
def get_eth_price(own):
    s = requests.Session()
    r = requests.get(url_eth)
    soup = BeautifulSoup(r.text, 'lxml')
    currency_eth = soup.find(class_= "table")
    currency_eth = currency_eth.find_all('td')[1].text
    currency_eth = float(currency_eth)
    own = float(own)
    exchange_eth = format(own*currency_eth, '0.2f')
    
    return exchange_eth

def get_now_eth_exchange():
    s = requests.Session()
    r = requests.get(url_eth)
    soup = BeautifulSoup(r.text, 'lxml')
    currency_eth = soup.find(class_="table")
    currency_eth = currency_eth.find_all('td')[1].text
    currency_eth = "市場均價為台幣 "+currency_eth+" 元"
    
    return currency_eth

# ZEC
def get_zec_price(own):
    s = requests.Session()
    r = requests.get(url_zec)
    soup = BeautifulSoup(r.text, 'lxml')
    currency_zec = soup.find(class_= "table")
    currency_zec = currency_zec.find_all('td')[1].text
    currency_zec = float(currency_zec)
    own = float(own)
    exchange_zec = format(own*currency_zec, '0.2f')
    
    return exchange_zec

def get_now_zec_exchange():
    s = requests.Session()
    r = requests.get(url_zec)
    soup = BeautifulSoup(r.text, 'lxml')
    currency_zec = soup.find(class_="table")
    currency_zec = currency_zec.find_all('td')[1].text
    currency_zec = "市場均價為台幣 "+currency_zec+" 元"
    
    return currency_zec


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello guys~'

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == '說明':
        message = TextSendMessage(text='假如所持有量為0.1btc\n輸入0.1btc即可。\n\n想知道btc市場均價\n輸入btc即可。\n\n其他幣別依此類推\n目前僅支援 btc/eth/zec')
        line_bot_api.reply_message(event.reply_token, message)
    
    if event.message.text == 'bot --help':
        message = TextSendMessage(text='本 bot 除了可以查價之外\n還有其他功能哦 (๑´ڡ`๑)\n\n只要輸入 \'others\' 或\'其他功能\'即可喔')
        
    if ('btc' in event.message.text) :
        try:
            if event.message.text == "btc":
                message = get_now_btc_exchange()
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
            else:
                own = event.message.text.split('btc')[0]
                price = get_btc_price(own)
                message = "現值台幣 "+price+" 元"
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
        except:
            error_message = TextSendMessage(text='格式錯誤')
            line_bot_api.reply_message(event.reply_token, error_message)
        return 0
            
    if ('BTC' in event.message.text) :
        try:
            if event.message.text == "BTC":
                message = get_now_btc_exchange()
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=message)
                )
            else:
                own = event.message.text.split('BTC')[0]
                price = get_btc_price(own)
                message = "現值台幣 "+price+" 元"
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=message)
                )
        except:
            error_message = TextSendMessage(text='格式錯誤')
            line_bot_api.reply_message(event.reply_token, error_message)
        return 0
            
    if ('eth' in event.message.text) :
        try:
            if event.message.text == "eth":
                message = get_now_eth_exchange()
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=message)
                )
            else:
                own = event.message.text.split('eth')[0]
                price = get_eth_price(own)
                message = "現值台幣 "+price+" 元"
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=message)
                )
        except:
            error_message = TextSendMessage(text='格式錯誤')
            line_bot_api.reply_message(event.reply_token, error_message)
        return 0
            
    if ('ETH' in event.message.text) :
        try:
            if event.message.text == "ETH":
                message = get_now_eth_exchange()
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=message)
                )
            else:
                own = event.message.text.split('ETH')[0]
                price = get_eth_price(own)
                message = "現值台幣 "+price+" 元"
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=message)
                )
        except:
            error_message = TextSendMessage(text='格式錯誤')
            line_bot_api.reply_message(event.reply_token,error_message)
        return 0
    
    if ('zec' in event.message.text) :
        try:
            if event.message.text == "zec":
                message = get_now_zec_exchange()
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=message)
                )
            else:
                own = event.message.text.split('zec')[0]
                price = get_zec_price(own)
                message = "現值台幣 "+price+" 元"
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=message)
                )
        except:
            error_message = TextSendMessage(text='格式錯誤')
            line_bot_api.reply_message(event.reply_token, error_message)
        return 0
            
    if ('ZEC' in event.message.text) :
        try:
            if event.message.text == "ZEC":
                message = get_now_zec_exchange()
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
            else:
                own = event.message.text.split('ZEC')[0]
                price = get_zec_price(own)
                message = "現值台幣 "+price+" 元"
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
        except:
            error_message = TextSendMessage(text='格式錯誤')
            line_bot_api.reply_message(event.reply_token, error_message)
        return 0
        
    if event.message.text == "三次元":
        client = ImgurClient(client_id, client_secret)
        images = client.get_album_images(album_id_beauty)
        index = random.randint(0, len(images) - 1)
        url = images[index].link
        image_message = ImageSendMessage(
            original_content_url=url,
            preview_image_url=url
        )
        line_bot_api.reply_message(
            event.reply_token, image_message)
        return 0
    
    if event.message.text == "二次元":
        client = ImgurClient(client_id, client_secret)
        images = client.get_album_images(album_id_2d)
        index = random.randint(0, len(images) - 1)
        url = images[index].link
        image_message = ImageSendMessage(
            original_content_url=url,
            preview_image_url=url
        )
        line_bot_api.reply_message(
            event.reply_token, image_message)
        return 0
    
    if event.message.text == "貓咪":
        client = ImgurClient(client_id, client_secret)
        images = client.get_album_images(album_id_cat)
        index = random.randint(0, len(images) - 1)
        url = images[index].link
        image_message = ImageSendMessage(
            original_content_url=url,
            preview_image_url=url
        )
        line_bot_api.reply_message(
            event.reply_token, image_message)
        return 0
    
    if event.message.text == "其他功能" or event.message.text == "others":
        buttons_template = TemplateSendMessage(
            alt_text = 'others template',
            template = ButtonsTemplate(
                thumbnail_image_url = 'https://i.imgur.com/3isip2K.jpg',
                title = '居然被發現了 ε٩(๑> ₃ <)۶з',
                text = '請擇一',
                actions = [
                    MessageTemplateAction(
                        label = '貓咪',
                        text = '貓咪'
                    ),
                    MessageTemplateAction(
                        label = '妹子',
                        text = '妹子'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    
    if event.message.text == "妹子":
        buttons_template = TemplateSendMessage(
            alt_text = '妹子 template',
            template = ButtonsTemplate(
                thumbnail_image_url = 'https://i.imgur.com/3isip2K.jpg',
                title = '只能選一種哦 (๑•́ ₃ •̀๑)',
                text = '請選擇',
                actions = [
                    MessageTemplateAction(
                        label = '二次元',
                        text = '二次元'
                    ),
                    MessageTemplateAction(
                        label = '三次元',
                        text = '三次元'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    

if __name__ == "__main__":
    app.run()
