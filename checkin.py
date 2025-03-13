import requests
import string
import random

class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    END = '\033[0m'

def generate_secret_key(length=26):
    characters = string.ascii_letters + string.digits
    secret_key = ''.join(random.choices(characters, k=length))
    return secret_key

import msvcrt
def clear_input_buffer():
    while msvcrt.kbhit():
        msvcrt.getch()

function_url = "https://us-central1-gdsc-web-2d5fa.cloudfunctions.net/api/checkin"
code = generate_secret_key()
print("Code:", code)
courseId = input("請輸入課程代碼: ")

setting_response = requests.post(f'{function_url}/settings?course={courseId}&code={code}')
print('Setting Response:',setting_response.text) 
# 從 QR Code 掃描機獲取輸入

while(True):
    clear_input_buffer()
    print()
    userId = input("請掃描 QR Code: ").replace("/","")
    print(f'{userId}')
    response_post = requests.post(f'{function_url}?user={userId}&code={code}&course={courseId}')
    if(response_post.status_code == 200):
        print(f'{Color.GREEN}{response_post.text}{Color.END}', end = "")
    else:
        print(f'{Color.RED}{response_post.text}{Color.END}', end = "")