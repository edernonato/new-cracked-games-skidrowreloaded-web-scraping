from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import requests
from bs4 import BeautifulSoup
import smtplib
from datetime import date

URL = "https://www.skidrowreloaded.com/"

response = requests.get(URL)
website = response.text

soup = BeautifulSoup(website, "html.parser")

print(soup.find(name="h2").a.get("href"))

game_tags = [game.text for game in soup.find_all(name="h2")]
game_links = [game_link.a.get("href") for game_link in soup.find_all(name="h2")]

for game in game_links:
    print(game)

for game in game_tags:
    print(game)


email_from = "edernonato47teste@hotmail.com"
password = "Eder@teste321"
SMTP = "smtp-mail.outlook.com"
PORT = 587

connection = smtplib.SMTP(SMTP, PORT)
connection.starttls()
connection.login(user=email_from, password=password)
email_to = "edernonato47@hotmail.com"
games_email = ""

html_start = f'''
    <html>
        <body>
            <h4>Cracked Games list First Page {date.today()} </h2>
        '''
html_end = '''
        </body>
    </html>
    '''

a_tags = []

for gameIndex in range(len(game_tags)):
    hyperlink = u'<a href="'+game_links[gameIndex] + '">' + game_tags[gameIndex] + '</a>'
    a_tags.append(hyperlink)

for a in a_tags:
    html_start += "\n" + a + "<br>" + "\n"

html = html_start + html_end

email_message = MIMEMultipart()
email_message['From'] = email_from
email_message['To'] = email_to
email_message['Subject'] = f'SkidrowReloaded Cracked games  - {date.today()}'
email_message.attach(MIMEText(html, "html"))
email_string = email_message.as_string()

connection.sendmail(from_addr=email_from, to_addrs=email_to, msg=email_string)
