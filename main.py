import requests #puxar informação de uma API
import smtplib
import email.message

#COTAÇÃO DO DOLAR FOR MENOR QUE 5.10

#pegar informação que eu quero
#cotaçao dolar - awesome api
requisição = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")

requisicao_dicionario = requisição.json()

cotacao = float(requisicao_dicionario['USDBRL']['bid'])

print(cotacao)


#enviar um aviso - EMAIL

def enviar_email(cotacao):  
    corpo_email = f"""
    <p>Dolar está abaixo de R$5,10. cotação atual: R$ { cotacao } </p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Dólar está hoje abaixo de R$5,10."
    msg['From'] = ''
    msg['To'] = ''
    password = '' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

if cotacao <= 5.10:
    enviar_email(cotacao)
#fazer deploy - heroku

#Sem Deply, foi apenas estudos.