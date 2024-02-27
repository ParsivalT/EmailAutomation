import smtplib 
from email.message import EmailMessage
from dotenv import load_dotenv
import os

# Carregando as Variaveis de Ambiente.
load_dotenv()

USER = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

# Iniciando o Servidor SMTP
servidor_email = smtplib.SMTP("smtp.gmail.com", 587)
servidor_email.starttls()

servidor_email.login(user=USER, password=PASSWORD)

msg = EmailMessage()
msg.set_content("Olá, este é um e-mail de teste.")
msg['Subject'] = 'Testando o Envio de E-mail'
msg['From'] = USER
msg['To'] = USER  # Altere para o destinatário desejado

servidor_email.send_message(msg)

servidor_email.quit()
