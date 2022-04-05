import vk_api
import requests
import time
import random


A = 10
B = 20
limit = 100
link = "https://vk.com/wall-192350539_1031514"
owner_id = -192350539
post_id = 1031514

phone_number = "9152415333"
key = ""
session = requests.Session()

vk_session = vk_api.VkApi(login=phone_number, token=key)
session_api = vk_session.get_api()
longpoll = vk_api.longpoll.VkLongPoll(vk_session)

while 1:
	session_api.wall.createComment(owner_id = owner_id, post_id = post_id)
	time.sleep(random.randint(5, 15))
