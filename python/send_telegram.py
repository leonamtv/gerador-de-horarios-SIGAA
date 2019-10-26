import telepot
import sys

token = ""

if token != "" : 

    bot = telepot.Bot(token)

    cid = int(sys.argv[1])

    log = bot.sendDocument(-cid, open('../img/horario.png', 'rb'), "Horário: Enviado via bot")

    print(log)

else :
    print('token do telegram vazio').