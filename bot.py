# -*- coding: utf-8 -*-
import telebot
import time
import config
import os
import tempfile
import random
import requests
from telebot import types
from telebot import util
from datetime import datetime
from modules.wiki import Wiki
from modules.reddit import Reddits
from modules.bash import Bash
from modules.urbdict import Urbdict
from modules.xtuff import Boobs,Butts
from modules.imdb import Imdb
from modules.tools import ChatUserName

bot = telebot.TeleBot(config.token())

#############################################
# loger                                     #
#############################################
def listener(messages):
    for m in messages:
        cid = m.chat.id
        chat_type = m.chat.type
        chat_title = m.chat.title
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        username = ChatUserName(m)
        #[time][cid][chat_type][chat_title][username][m.text]
        mensaje = ("[%s][%s][%s][%s][%s][%s]"%(now,cid,chat_type,chat_title,username,m.text))
        f = open( 'files/log', 'a')
        f.write(mensaje + "\n")
        f.close()

bot.set_update_listener(listener)

#############################################
# Return message                            #
#############################################

def nsfw(cid, uid, chattype, msg):
  if chattype == "group":
    bot.send_photo(uid, msg)
  else:
    bot.send_photo(cid, msg)

def nsfwReddit(cid, uid, chattype, msg):
  if chattype == "group":
    bot.send_message(uid, msg)
  else:
    bot.send_message(cid, msg)


#############################################
# Handlers                                  #
#############################################
@bot.message_handler(commands=['windows'])
def command_windows(m):
    cid = m.chat.id
    bot.send_message(cid, 'Vete a la mierda')

@bot.message_handler(commands=['thread'])
def command_thread(m):
    cid = m.chat.id
    text = "[Hilo GNU/Linux](https://www.mediavida.com/foro/hard-soft/gnulinux-hilo-general-489974)"
    bot.send_message(cid, text, parse_mode="Markdown")

@bot.message_handler(commands=['repo'])
def command_repo(m):
    cid = m.chat.id
    msg = '[Repositorio en Github](https://github.com/ajerezr/bot-mv-telegram)'
    bot.send_message(cid, msg, parse_mode="Markdown")

@bot.message_handler(commands=['imb'])
def command_imdb(m):
    cid = m.chat.id
    msg = Imdb(m)
    bot.send_message(cid, msg, parse_mode="Markdown")

@bot.message_handler(commands=['butts'])
def command_butts(m):
    cid = m.chat.id
    uid = m.from_user.id
    chattype = m.chat.type
    number = random.randint(1, 3000)
    text = Butts(number)
    with open(str(number)+'.jpg', 'wb') as photo:
       photo.write(requests.get(text).content)
    photo = open(str(number)+'.jpg', 'rb')
    nsfw(cid, uid, chattype, photo)
    os.remove(str(number)+'.jpg')

@bot.message_handler(commands=['boobs'])
def command_boobs(m):
    cid = m.chat.id
    uid = m.from_user.id
    chattype = m.chat.type
    number = random.randint(1, 3000)
    text = Boobs(number)
    with open(str(number)+'.jpg', 'wb') as photo:
       photo.write(requests.get(text).content)
    photo = open(str(number)+'.jpg', 'rb')
    nsfw(cid, uid, chattype, photo)
    os.remove(str(number)+'.jpg')

@bot.message_handler(commands=['urbdict'])
def command_urbdict(m):
    cid = m.chat.id
    urb = Urbdict(m)
    bot.send_message(cid, urb)

@bot.message_handler(commands=['bash'])
def command_bash(m):
    cid = m.chat.id
    cmd = Bash(m)
    bot.send_message(cid, cmd, parse_mode= 'Markdown')

@bot.message_handler(commands=['wiki'])
def command_wiki(m):
    cid = m.chat.id
    wikipedia = Wiki(m)
    bot.send_message(cid, wikipedia)

@bot.message_handler(commands=['asian_gif'])
def command_assian_gifs(m):
    cid = m.chat.id
    uid = m.from_user.id
    chattype = m.chat.type
    tits = Reddits('asians_gif')
    nsfwReddit(cid, uid, chattype, tits)

@bot.message_handler(commands=['asianhotties'])
def command_assianhotties(m):
    cid = m.chat.id
    uid = m.from_user.id
    chattype = m.chat.type
    tits = Reddits('asianhotties')
    nsfwReddit(cid, uid, chattype, tits)

@bot.message_handler(commands=['AsiansGoneWild'])
def command_AsiansGoneWild(m):
    cid = m.chat.id
    uid = m.from_user.id
    chattype = m.chat.type
    tits = Reddits('AsiansGoneWild')
    nsfwReddit(cid, uid, chattype, tits)

@bot.message_handler(commands=['anal'])
def command_anal(m):
    cid = m.chat.id
    uid = m.from_user.id
    chattype = m.chat.type
    tits = Reddits('anal')
    nsfwReddit(cid, uid, chattype, tits)

@bot.message_handler(commands=['RealGirls'])
def command_RealGirls(m):
    cid = m.chat.id
    uid = m.from_user.id
    chattype = m.chat.type
    tits = Reddits('RealGirls')
    nsfwReddit(cid, uid, chattype, tits)

@bot.message_handler(commands=['wallpapers'])
def command_wallpapers(m):
    cid = m.chat.id
    uid = m.from_user.id
    chattype = m.chat.type
    wall = Reddits('wallpapers')
    bot.send_message(cid, wall)

#############################################
# peticion
#############################################
# Con esto, le decimos al bot que siga funcionando
# incluso si encuentra algún fallo.
bot.polling(none_stop=True)
