import smtplib
from email.message import EmailMessage

from string import Template
from  pathlib import Path # os path

html=Template(Path('index.html').read_text())

email= EmailMessage()
email['from'] ='Isiak Lukman'
email['to']= 'lukman.isiaka01@gmail.com'
email['subject']='You won 1,000,000 dollars!'

email.set_content(html.substitute({'name':'WALIYAT'}),'html')


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('Pythonproject86@gmail.com', 'Mobol001$')
	#smtp.login('iolukman86@gmail.com', 'Mobol001$')
	smtp.send_message(email)

	print('all is good')
