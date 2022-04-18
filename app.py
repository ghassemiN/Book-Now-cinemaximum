from crypt import methods
import json, re, telegram
import urllib.request as urllib2
from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
from credentials import *


global bot
global TOKEN
TOKEN = bot_token
chat_id = chat_id
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    #The webpage for crawling
    item_url = "https://www.cinemaximum.com.tr/en/doktor-strange-2-movie"

    page = urllib2.urlopen(item_url) 
    soup = BeautifulSoup(page, 'html.parser')

    get_div = soup.find("div", attrs={'class': 'movie-buttons'})
    text = get_div.text.strip()

    if "Book Now" in text:
        print("Book Now")
        send_msg()
        return jsonify("Book It No0o0o00o0o0o0ow")
        
    else:
        return jsonify("It has not opend yet")


@app.route('/'.format(TOKEN), methods=['POST'])
def send_msg():
    bot.sendMessage(chat_id=chat_id, text="BOOK NOW")
    return True

if __name__ == "__main__":
    app.run()