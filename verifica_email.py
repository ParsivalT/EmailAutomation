from imbox import Imbox
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
HOST = 'imap.gmail.com'

mail = Imbox(hostname=HOST,
        username=EMAIL,
        password=PASSWORD,
        ssl=True,
        ssl_context=None,
        starttls=False)

""" messagens = mail.messages(raw='has:attachments')   """   
messagens = mail.messages()
boletos_directory = "/home/thi/Projetos/Python/Automacao_Email/boletos/"

for (uid, message) in messagens:
    if len(message.attachments) > 0:
        for attach in message.attachments:
            att_file = attach["filename"]

            if '.pdf' in att_file:
                print(f"Salvando {att_file}")
                download_path = f'{boletos_directory}{att_file}'  # Include filename in path

                with open(download_path, "wb") as fp:  # Open file in write binary mode
                    fp.write(attach['content'].read())


        

        


