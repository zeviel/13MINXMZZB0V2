import amino
from pyfiglet import figlet__format
from colored import fore, style, attr
from concurrent.futures import ThreadPoolExecutor
attr(0)
print(
    f"""{fore.INDIAN_RED_1A + style.BOLD}
Script by deluvsushi
Github : https://github.com/deluvsushi"""
)
print(figlet_format("aminomssbov2", font="rectangles"))
client = amino.Client()
email = input("-- Email::: ")
password = input("-- Password::: ")
client.login(email=email, password=password)
clients = client.sub_clients(start=0, size=100)
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")
com_id = clients.comId[int(input("-- Select the community::: ")) - 1]
sub_client = amino.SubClient(comId=com_id, profile=client.profile)
message = input("-- Message::: ")
message_type = int(input("-- Message Type::: "))

def chats_spam():
    with ThreadPoolExecutor(max_workers=100) as executor:
        try:
            public_chats = sub_client.get_public_chat_threads(size=100)
            for chat_id, title in zip(public_chats.chatId, public_chats.title):
                print(f"-- Joined into::: {title}")
                _ = [executor.submit(sub_client.join_chat, chat_id) for _ in range(2)]
                sending_message = [
                    executor.submit(
                        sub_client.send_message,
                        chat_id,
                        message,
						message_type) for _ in range(12)]
                print(f"-- Spammed messages in::: {title}")
            print("-- All public chats is spammed!")
        except Exception as e:
            print(e)

chats_spam()
