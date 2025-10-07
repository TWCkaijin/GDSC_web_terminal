WEB_SECRET = "rezwxtyculutkdtiouyilt54489t65edfghjkl"
import requests
import string
import random
import sys
import termios
import os

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def clear_input_buffer():
    # 檢查標準輸入是否是終端
    if os.isatty(sys.stdin.fileno()):
        termios.tcflush(sys.stdin, termios.TCIFLUSH)
    else:
        print("標準輸入不是終端，無法清除輸入緩衝區。")

function_url = "https://us-central1-gdsc-web-2d5fa.cloudfunctions.net/api/payment"
payload = {'code': WEB_SECRET}

while True:
    clear_input_buffer()
    print("請掃描 QR Code...",end='')
    userId = input("")
    if userId:
        response_post = requests.post(f'{function_url}?user={userId[1:]}', json=payload)
        print(f'{color.GREEN}{response_post.text}{color.END}')
    else:
        print("未能掃描到 QR Code，請重試。")