import telepot
import sys

bot = telepot.Bot("779550705:AAHT9jIqE4zF839tAnNZLYWH9UgRubw31dM")

cid = int(sys.argv[1])

log = bot.sendDocument(-cid, open('../img/horario.png', 'rb'), "Horário: Enviado via bot")

print(log)