import vk_api
from vk_api.longpoll import VkLongPoll
import requests
from access_token import personal_token, number


A = 10
B = 20
limit = 100

phone_number = number
key = personal_token
session = requests.Session()

vk_session = vk_api.VkApi(login=phone_number, token=key)
session_api = vk_session.get_api()
longpoll = vk_api.longpoll.VkLongPoll(vk_session)

vk_session.method("messages.send", {"chat_id": 38, "message": "Время скрипту удалять сообщения дождя", "random_id": 0})


def deleter(delete_count):
    for i in range(delete_count):
        for event in longpoll.listen():
            if event.type == vk_api.longpoll.VkEventType.MESSAGE_NEW and event.to_me and event.from_chat:
                user_id = event.user_id
                chat_id = event.chat_id
                if chat_id == 38 and user_id == 351168531:  # id чата параллели и id человека
                    message_id = event.message_id
                    # user_get = vk_api.users.get(user_ids=user_id)
                    # user_get = user_get[0]
                    # first_name = user_get['first_name']
                    # second_name = user_get['second_name']
                    print(message_id)
                try:
                    session_api.messages.delete(message_ids=[message_id], delete_for_all=1)
                    vk_session.method("messages.send",
                                      {"chat_id": 38, "message": f"Удалил сообщение {user_id}", "random_id": 0})
                except Exception:
                    continue
                print("Часть выброшена", i, user_id)
                break

    vk_session.method("messages.send",
                      {"chat_id": 38, "message": f"удаление сообщений {user_id} закончено", "random_id": 0})
    print("Мусор вынесен.")


mc = int(input())
deleter(mc)
