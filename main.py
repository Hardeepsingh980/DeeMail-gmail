from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog
from csv import DictReader
import _thread
import send_mail_f
import login

try:
    f = open('logs.csv','r')
    d = f.read(1024)
    f.close()
    if d != '':
        pass
    else:
        login.login()
except:
    login.login()














def main_loop():
    ## ----------------------------------------------------------------------
    f = open('logs.csv','r')
    r = DictReader(f)
    global username
    global password
    for i in r:
        username = i['username']
        password = i['password']
    f.close()
        
    ##-----------------------------------------------------------------------



    def logout_func():
        f = open('logs.csv','w')
        f.write('')
        win.destroy()




    def vald_email():
        to = to_e.get()
        subject = subject_e.get()
        message = mail_text.get(1.0,END)
        if '@' in to and '.com' in to:
            try:
                send_mail_f.send_mail(username,password,to,subject,message)
                mb.showinfo('Sent',f'Mail successfuly sent to {to}')
            except:
                mb.showerror('Connection error','Unable to connect to internet. Please check your internet connection.')
        else:
            mb.showerror('Error','Invalid Email Address')



    def send_mul_mail_loop():
        to = to_e.get()
        subject = subject_e.get()
        message = mail_text.get(1.0,END)
        for mail in mail_list:
               send_mail_f.send_mail(username,password,mail,subject,message)
        mb.showinfo('Sent',f'Mail successfuly sent to {len(mail_list)} people')
        load.destroy()


    def load_send():
        global load
        load = Tk()
        load.geometry('+200+200')
        load.resizable(0,0)
        Label(load, text='Sending Mails......',font=('Cambria',13)).pack()
        load.mainloop()




    def send_mul_mail():
        try:        
            _thread.start_new_thread(send_mul_mail_loop,())
            _thread.start_new_thread(load_send,())
        except:
            mb.showerror('Error','Please attack a CSV file containing emails. for more help refer to info button')





    def csv_func():
        try:
            f = filedialog.askopenfile(initialdir='E:\\', title='Select file to open',)
            r = DictReader(f)
            global mail_list
            mail_list = []    
            try:
                for row in r:
                        mail_list.append(row['email'])
            except:
                mb.showerror('Error','Error Reading The CSV File. Please refer to info button for help.')
        except:
            pass





    def about_func():
        mb.showinfo('About', 'This is an exclusive distribution of DeeMail created By Hardeep Singh. This application was designed to send emails. This has features like sending emails, sending multiple emails, setting, about. Hope you like the application. Please share your feedbacks.')




    def mul_mail_func():
        ## Log Bg
        log_bg.place(x=1000)
        log_img.place(x=1000)
        log_in_as.place(x=1000)
        name.place(x=1000)

        ## Menu Options
        menu_bg.place(x=1000)
        mail_b.place(x=1000)
        mul_mail_b.place(x=1000)
        setting_b.place(x=1000)
        about_b.place(x=1000)
        cl_l.place(x=1000)
        logout_b.place(x=1000)

        ## Plus Button
        plus_button.place(x=1000)

        ## Compose Email
        header_l.place(x=20,y=50)
        to_l.place(x=40,y=120)

        ## To
        to_e.place(x=1000)

        ##Csv
        csv_b.place(x=90,y=120)
        csv_ab.place(x=270,y=120)

        
        subject_l.place(x=40,y=170)
        subject_e.place(x=120,y=170)
        mail_text.place(x=40,y=220)
        send_b.place(x=300,y=440)
        cancel_b.place(x=360,y=440)

        send_b['command'] = send_mul_mail





    def home_func():
        ## Log Bg
        log_bg.place(x=0,y=33)
        log_img.place(x=50,y=50)
        log_in_as.place(x=40,y=120)
        name.place(x=10,y=145)

        ## Menu Options
        menu_bg.place(x=0,y=32)
        mail_b.place(x=10,y=200)
        mul_mail_b.place(x=5,y=250)
        setting_b.place(x=5,y=300)
        about_b.place(x=10,y=360)
        cl_l.place(x=250,y=200)
        logout_b.place(x=10,y=410)

        ## Plus Button
        plus_button.place(x=370,y=420)

        ## Compose Email
        header_l.place(x=1000)
        to_l.place(x=1000)
        to_e.place(x=1000)
        subject_l.place(x=1000)
        subject_e.place(x=1000)
        mail_text.place(x=1000)
        send_b.place(x=1000)
        cancel_b.place(x=1000)

        ##Mul_mail
        csv_ab.place(x=1000)
        csv_b.place(x=1000)

        

    def email_func():
        ## Log Bg
        log_bg.place(x=1000)
        log_img.place(x=1000)
        log_in_as.place(x=1000)
        name.place(x=1000)

        ## Menu Options
        menu_bg.place(x=1000)
        mail_b.place(x=1000)
        mul_mail_b.place(x=1000)
        setting_b.place(x=1000)
        about_b.place(x=1000)
        cl_l.place(x=1000)
        logout_b.place(x=1000)

        ## Plus Button
        plus_button.place(x=1000)

        ## Compose Email
        header_l.place(x=20,y=50)
        to_l.place(x=40,y=120)
        to_e.place(x=90,y=120)
        subject_l.place(x=40,y=170)
        subject_e.place(x=120,y=170)
        mail_text.place(x=40,y=220)
        send_b.place(x=300,y=440)
        cancel_b.place(x=360,y=440)
        send_b['command'] = vald_email
        csv_ab.place(x=1000)


    bg = '#408080'

    win = Tk()
    win.geometry('450x487')
    win.resizable(0,0)
    win.title('DeeMail')

    Label(win, text='',bg=bg,width=450,font=('arial black',15,'bold'),relief='groove').pack()
    Label(win, text='DeeMail',bg=bg,fg='white',font=('arial black',12,'bold')).place(x=350,y=2)

    home_img = PhotoImage(file='resources/home.png')
    Button(win, image=home_img,bg=bg,bd=0,command=home_func).place(x=8,y=4)


    plus_img = PhotoImage(file='resources/plus2.png') 
    plus_button = Button(win, image=plus_img,bd=0,command=email_func)




    ##Menu Bar

    menu_bg = Label(win, text='',bg=bg,width=15,font=('arial black',15,'bold'),relief='groove',height=16)
    log_bg = Label(win,bg=bg,width=30,height=9,relief='groove')
    login_img =PhotoImage(file='resources/login.png')
    log_img = Label(win,image=login_img,bg=bg)
    log_in_as = Label(win, text='Logged In As : ',bg=bg,font=('',13),fg='white')
    name = Label(win, text=username,bg=bg,font=('',10,'bold'),fg='white')
    if len(username) > 25:
        name['font'] = ('',9,'bold')
    mail_img = PhotoImage(file='resources/mail.png')
    mail_b = Button(win, image=mail_img, bg=bg,bd=0,text=' Compose Email',compound='left',fg='white',font=('arial black',10,'bold'),command=email_func)
    mul_mail_img = PhotoImage(file='resources/mul_mail.png')
    mul_mail_b = Button(win, image=mul_mail_img, bg=bg,bd=0,text=' Multiple Emails',compound='left',fg='white',font=('arial black',10,'bold'),command=mul_mail_func)
    setting_img = PhotoImage(file='resources/camera-settings-icon-white-300x300.png')
    setting_b = Button(win, image=setting_img, bg=bg,bd=0,text=' Settings',compound='left',fg='white',font=('arial black',10,'bold'))
    about_img = PhotoImage(file='resources/about.png')
    about_b = Button(win, image=about_img, bg=bg,bd=0,text=' About',compound='left',fg='white',font=('arial black',10,'bold'),command=about_func)
    logout_img = PhotoImage(file='resources/logout-24.png')
    logout_b = Button(win, image=logout_img, bg=bg,bd=0,text=' Log Out',compound='left',fg='white',font=('arial black',10,'bold'),command=logout_func)

    cl_l = Label(win, text='Click + button\nto send email.',fg='#c8c8c8',font=('arial black',15,'bold'))




    ## Compose Email
    header_l = Label(win, text='Compose Email',font=('Cambria',20))
    to_l = Label(win, text='To : ',font=('Cambria',15))
    to_e = Entry(win, font=('Cambria',15),width=30)
    subject_l = Label(win, text='Subject : ',font=('Cambria',15))
    subject_e = Entry(win, font=('Cambria',15),width=27)
    mail_text = Text(win,wrap=WORD, font=('Cambria',13),height=10,width=43)
    send_b = Button(win, text='Send',bg='green',fg='white',bd=0, font=('Cambria',13),command=vald_email)
    cancel_b = Button(win, text='Cancel',bg='red',fg='white',bd=0, font=('Cambria',13),command=home_func)
    csv_b = Button(win,  text='Attach Email CSV file',bd=2, font=('Cambria',13),command=csv_func)
    about2_img = PhotoImage(file='resources/about (2).png')
    csv_ab = Button(win, image=about2_img,bd=0,command=lambda : mb.showinfo('Info','Attach a CSV file containing all the email addresses to whom you want to send the mail. Remember that the first line of the CSV file should be "email" other wise it will raise error.'))





    home_func()

    win.mainloop()


main_loop()

