import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Define params

mailsender = "dummycuenta3@gmail.com"
mailreceip = "tanibet.escom@gmail.com"
mailserver = 'smtp.gmail.com: 587'
password = 'mxrfalaydmgolvaq'

def send_alert_attached(subject,imagen):
    """ Envía un correo electrónico adjuntando la imagen en IMG
    """
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = mailsender
    msg['To'] = mailreceip
    fp = open(imagen, 'rb')
    img = MIMEImage(fp.read())
    texto = MIMEText("Nombre del dispositivo: david-Inspiron-5575 \n "
               "Sistema Operativo: Ubuntu \n "
               "Informacion de contacto: davidfloresescalona@gmail.com \n "
               "Ubicacion: laboratorio de REDES \n")
    msg.attach(texto)
    fp.close()
    msg.attach(img)
    s = smtplib.SMTP(mailserver)

    s.starttls()
    # Login Credentials for sending the mail
    s.login(mailsender, password)

    s.sendmail(mailsender, mailreceip, msg.as_string())
    s.quit()