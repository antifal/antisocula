import vk_api
import time

loginVK = 'andresitsup@gmail.com'
passwordVK = 'alegrosel001'

try:
    vk = vk_api.VkApi(login = loginVK, password = passwordVK)
    vk.auth()
except:
    print('something went wrong')
    time.sleep(9999)
print('start')
chat = input('chat id ')
chatname = input('chat name: ')
text = input('text ')
delay = int(input('delay '))
while(True):
    time.sleep(delay)
    vk.method('messages.editChat', {'chat_id':chat, 'title':chatname})
    vk.method('messages.send', {'chat_id':chat, 'message':text})
    print('chat name changed, text sended')

        
