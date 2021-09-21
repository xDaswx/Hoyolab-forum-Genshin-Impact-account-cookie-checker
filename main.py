import requests
import threading
#open cookies file
kj1 = open("cookies.txt", 'r')

#checker
def cokie():
    for line in kj1:
     zx = []
     datas = '{"avatar":"100108","avatar_url":"","gender":0,"introduce":""}'
     ab = line.strip()
     r = requests.post(url = 'https://api-os-takumi.mihoyo.com/community/user/wapi/userInfoEdit', headers = {'x-rpc-language': 'pt-pt','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.58 Safari/537.36','cookie': '{}'.format(ab)}, data=datas)
     jj = r.json()['message']
     if jj == 'OK':
         print('Working, message from server: {}'.format(jj))
     else:
       f = open('dead cookies.txt', 'a') 
       oIOR = ab + '\n'
       f.write(oIOR)
       f.close

#threads starting
t1 = threading.Thread(target=cokie)
t1.start()
t1.join()
