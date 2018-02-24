# -*- coding: utf-8 -*-

import re
import requests
from lxml import etree


url_btc = 'https://www.coingecko.com/zh-tw/%E5%8C%AF%E7%8E%87%E5%9C%96/%E6%AF%94%E7%89%B9%E5%B9%A3/twd'
url_eth = 'https://www.coingecko.com/zh-tw/%E5%8C%AF%E7%8E%87%E5%9C%96/%E4%BB%A5%E5%A4%AA%E5%B9%A3/twd'
url_zec = 'https://www.coingecko.com/zh-tw/%E5%8C%AF%E7%8E%87%E5%9C%96/zcash/twd'
url_btg = 'https://www.coingecko.com/zh-tw/%E5%8C%AF%E7%8E%87%E5%9C%96/bitcoin-gold/twd'

# BTC
def get_btc_price(own):
    r = requests.get(url_btc)
    html = etree.HTML(r.content)
    price = html.xpath('//div/table/tbody/tr/td/span/text()')[0].split(' ')[1]
    price = re.sub(r',', "", price)
    own = float(own)
    message = format(own*price, '0.2f')
    
    return message

def get_now_btc_exchange():
    r = requests.get(url_btc)
    html = etree.HTML(r.content)
    price = html.xpath('//div/table/tbody/tr/td/span/text()')[0].split(' ')[1]
    price = re.sub(r',', "", price)
    price = format(float(price), '0.2f')
    message = "市場均價為台幣 " + price + " 元"
    
    return message

# ETH
def get_eth_price(own):
    r = requests.get(url_eth)
    html = etree.HTML(r.content)
    price = html.xpath('//div/table/tbody/tr/td/span/text()')[0].split(' ')[1]
    price = re.sub(r',', "", price)
    own = float(own)
    message = format(own*price, '0.2f')
    
    return message

def get_now_eth_exchange():
    r = requests.get(url_eth)
    html = etree.HTML(r.content)
    price = html.xpath('//div/table/tbody/tr/td/span/text()')[0].split(' ')[1]
    price = re.sub(r',', "", price)
    price = format(float(price), '0.2f')
    message = "市場均價為台幣 " + price + " 元"
    
    return message

# ZEC
def get_zec_price(own):
    r = requests.get(url_zec)
    html = etree.HTML(r.content)
    price = html.xpath('//div/table/tbody/tr/td/span/text()')[0].split(' ')[1]
    price = re.sub(r',', "", price)
    own = float(own)
    message = format(own*price, '0.2f')
    
    return message

def get_now_zec_exchange():
    r = requests.get(url_zec)
    html = etree.HTML(r.content)
    price = html.xpath('//div/table/tbody/tr/td/span/text()')[0].split(' ')[1]
    price = re.sub(r',', "", price)
    price = format(float(price), '0.2f')
    message = "市場均價為台幣 " + price + " 元"
    
    return message
    
# BTG
def get_btg_price(own):
    r = requests.get(url_btg)
    html = etree.HTML(r.content)
    price = html.xpath('//div/table/tbody/tr/td/span/text()')[0].split(' ')[1]
    price = re.sub(r',', "", price)
    own = float(own)
    message = format(own*price, '0.2f')
    
    return message
    
def get_now_btg_exchange():
    r = requests.get(url_btg)
    html = etree.HTML(r.content)
    price = html.xpath('//div/table/tbody/tr/td/span/text()')[0].split(' ')[1]
    price = re.sub(r',', "", price)
    price = format(float(price), '0.2f')
    message = "市場均價為台幣 " + price + " 元"
    
    return message





