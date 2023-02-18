

tg_api = '6227517925:AAEG62y40j_iGJqvXdTSceUlejR1OdRagTQ'
id_mine = 1307289323
#5187664625, 1307289323

import telegram




bot = telegram.Bot(token= tg_api)

async def send_telegram_message(telegram_id, text_to_send):
    try:
        await bot.sendMessage(int(telegram_id), text_to_send)
    except Exception as e:
        print(e)

send_telegram_message(id_mine,"testare 1 SDA")

# import requests
# message = "testare 1 SDA"
#
# url = f"https://api.telegram.org/bot{tg_api}/sendMessage?chat_id={id_mine}&text={message}"
# print(requests.get(url).json()) # this sends the message