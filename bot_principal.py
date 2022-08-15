from selenium import webdriver
import telebot 

lista_status = []

#chave disponibilizada pelo telegram
chave_api = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

bot = telebot.TeleBot(chave_api)


#função pesquisa no site de rastreamento
def sitepesquisa(código):
    navegador = webdriver.Chrome()
    navegador.get("https://www.linkcorreios.com.br/")
    teste = navegador.find_element("name", "id")
    teste.send_keys(código)
    navegador.find_element("xpath", '//*[@id="page"]/main/section/div/div/form/div/div[2]/input').click()
    status = navegador.find_element("xpath", '//*[@id="page"]/main/div[4]/div/div/div[1]/div/div/ul')
    texto = status.text
    lista_status.append(texto)


#função resposta 
@bot.message_handler(commands=["c"])
def pedindo_codigo(msg):
    msg2 = msg.text
    codigo = msg2.split(" ")[1]
    
    sitepesquisa(codigo)
    
    bot.reply_to(msg, lista_status)




#retornar 
def verificar(msg):
    return True


#mensagem principal do BOT
@bot.message_handler(func=verificar) 
def resposta(msg):  

    msg_inical= """@SykesRastreioBot!
    
Ola, tudo bom? Sou um bot para te auxiliar no rastreio de suas encomendas.

Siga as seguintes instruções:

Digite '/c (seu codigo)' 
ex: /c XXXXXXX

Espere alguns segundos e tenha seu rastreio de forma rapida
"""

    lista_status.clear()
    
    #enviar msg
    bot.reply_to(msg, msg_inical)

 


bot.polling()









