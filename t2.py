import asyncio
import telegram
#pip install python-telegram-bot



#bot link = http://t.me/sda_17xy_robot
# !!! pentru a putea trimite mesaje, trebuie mai intai sa intrati pe pagina bot-ului si sa apasati /start.
#Acesta e un fel de acord ca robotul sa poata interactiona cu voi

#pentru a va afla id-ul contului, scrieti aici> https://t.me/raw_info_bot


tg_api = '6227517925:AAEG62y40j_iGJqvXdTSceUlejR1OdRagTQ'
#pentru a seta un bot, interactionati cu https://t.me/BotFather
#dar acum puteti folosi acest token pentru bot-ul creat https://t.me/sda_17xy_robot

id_Constantin = 1307289323
text_to_send = "Aloha"

async def send_mes(id,text):
    bot = telegram.Bot(tg_api)
    async with bot:
        await bot.sendMessage(id,text)


asyncio.run(send_mes(id_Constantin, text_to_send))
