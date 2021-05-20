import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
 
class EmailController:

    def send_pop_as_email(transaction_reference):

        # body of the email
        body = '''
        Good day,
        Please find attached a copy of your proof of payment

        Kind regards
        Nigel Zulu
        '''
        # ============================================
        # sender email address eg zulunigelb@gmail.com
        # these will be used to authenticate to gmail
        sender = 'test@nigel.zulu'
        password = '*******'
    
        # enter the reciever email address eg danielzulu@gmail.com
        receiver = 'zulunigelb@gmail.com'
        
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = receiver
        message['Subject'] = 'ZB BANK PROOF OF PAYMENT'
        
        message.attach(MIMEText(body, 'plain'))
        
        # select the file you want to send
        pdfname = 'generated-pdf/'+transaction_reference+'.pdf'

        # rewrite the name of the pdf
        pdffilename = transaction_reference+'.pdf'
        
        # prepare payload
        binary_pdf = open(pdfname, 'rb')
        
        payload = MIMEBase('application', 'pdf', Name=pdfname)
        payload.set_payload((binary_pdf).read())

        encoders.encode_base64(payload)
        
        payload.add_header('Content-Disposition', 'attachment', filename=pdffilename)
        message.attach(payload)
        
        #use gmail with port
        session = smtplib.SMTP('smtp.gmail.com', 587)
        
        #enable security
        session.starttls()
        
        #login with mail_id and password
        session.login(sender, password)
        
        text = message.as_string()
        session.sendmail(sender, receiver, text)
        session.quit()
        print('Mail Sent')



