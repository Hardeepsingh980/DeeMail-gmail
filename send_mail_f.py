import smtplib



def send_mail(username,password,recv, subject, message):
        conn = smtplib.SMTP('smtp.gmail.com' , 587)
        conn.ehlo()
        conn.starttls()
        conn.login(username,password)
        msg = 'Subject : '+subject + '\n\n' +message
        conn.sendmail(username, recv, msg)
        conn.quit()
      



##conn = smtplib.SMTP('smtp.gmail.com' , 587)
##conn.ehlo()
##conn.starttls()
##conn.login('hardeeptestmail@gmail.com','hdeep980')
##conn.sendmail('hardeeptestmail@gmail.com','hardeep0khalsa122@gmail.com','Hello')
