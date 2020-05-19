from tkinter import *
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
from tkinter import messagebox  
root=Tk()
root.title("facebook-bot")
root.geometry("550x600")
root.configure(bg="#13CA71")
l1=Label(root,text="Username:-",bg="#13CA71",fg="blue",font="Arial 15 bold")
l1.place(x=120,y=80)
user_field=Entry(root,width=30)
user_field.place(x=240,y=80)
l2=Label(root,text="password:-",bg="#13CA71",fg="blue",font="Arial 15 bold")
l2.place(x=120,y=120)
passw_field=Entry(root,show="*",width=30)
passw_field.place(x=240,y=120)
l3=Label(root,text="message:-",bg="#13CA71",fg="blue",font="Arial 15 bold")
l3.place(x=120,y=160)
msg=Text(root,height=10,width=30)
msg.place(x=240,y=160)
def down():
    options = Options()
    options.add_argument("--disable-notifications")
    driver=webdriver.Chrome(chrome_options=options, executable_path='/usr/bin/chromedriver')    
    driver.get('https://www.facebook.com/')
    driver.find_element_by_id('email').click()
    driver.find_element_by_id('email').send_keys(user_field.get())
    driver.find_element_by_id('pass').click()
    driver.find_element_by_id('pass').send_keys(passw_field.get())
    driver.find_element_by_id('pass').send_keys(Keys.ENTER)
    time.sleep(5)
    Element=driver.find_element_by_xpath("//*[@name='xhpc_message']")
    Element.click()
    Element.send_keys(msg.get("1.0",END))
    buttons=driver.find_elements_by_tag_name('button')
    for button in buttons:
            if(button.text=='Post'):
                        button.click()
b1=Button(root,text="send",bg="#13BFCA",font="Arial 15 bold",activebackground="#13BFCA",command=down)
b1.place(x=250,y=350)
root.mainloop()
