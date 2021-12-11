import smtplib

server=smtplib.SMTP('smptp.gmail.com',587)
server.starttls()
server.login('mu4636764@gmail.com','zeeshanusama')
server.sendmail('mu4636764@gmail.com','ali.murtaza.software.engineer@gmail.com','python test')

print("email sent")