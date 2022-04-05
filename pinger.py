import vk_api
from vk_api.longpoll import VkLongPoll
import requests

phone_number = ""
key = ""
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
