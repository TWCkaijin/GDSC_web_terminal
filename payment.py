WEB_SECRET = "rezwxtyculutkdtiouyilt54489t65edfghjkl"
import requests

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

import msvcrt
def clear_input_buffer():
    while msvcrt.kbhit():
        msvcrt.getch()

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