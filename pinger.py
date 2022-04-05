import vk_api
from vk_api.longpoll import VkLongPoll
import requests

phone_number = "9152415333"
key = "f3957576d3370df3e238dbfb6e9361cb84f0817d5c99fa96f044aca8f69228720afa06216d98a3821c50e"
session = requests.Session()

vk_session = vk_api.VkApi(login=phone_number, token=key)
session_api = vk_session.get_api()
longpoll = vk_api.longpoll.VkLongPoll(vk_session)

response = session_api.messages.getConversationMembers(peer_id=2000000053, fields="count, profiles")

message = ""
dict = response['items']
for item in dict:
	message += f"@id{str(item['member_id'])} "
print(message)