import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

debug = True
def debug(text):
  if debug:
    print ("==> " + text)

class Email:
  def __init__(self, to, subject, message, sender = 'atticus@jamiehoward.co'):
    self.to = to
    self.subject = subject
    self.message = message
    self.sender = sender

  def send(self):
    # set up the server
    debug("setting up server")
    server = smtplib.SMTP("smtp.gmail.com", 25)
    debug("server.ehlo()")
    server.ehlo()
    debug("server.starttls()")
    server.starttls()
    debug("server.login()")
    server.login('jamie@blackairplane.com', '7fury#GgL')
    debug("Logged in to server")
    
    msg = MIMEMultipart('mixed')
    msg['Subject'] = self.subject
    msg['From'] = self.sender
    msg['To'] = self.to

    html = """\
        <html>
          <head></head>
          <body>
            <p>Testing email functionality</p>
          </body>
        </html>
    """
    msg.attach(MIMEText(html, 'html'))
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()

test = Email('jamie@blackairplane.com', 'Testing Atticus', 'Testing')
test.send()
