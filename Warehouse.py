from tkinter import *
from tkinter import ttk
import sqlite3 as sql
from tkinter import filedialog
import pandas as pd
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # important
from tkinter import *
from PIL import ImageTk, Image
import io


root = Tk()
loginpage = Toplevel()
registerpage = Toplevel()
productpage = Toplevel()
employeepage = Toplevel()
mojodipage = Toplevel()
sabtvorod = Toplevel()
reqkalapage = Toplevel()
sefareshkala = Toplevel()  
sabtKhoroj = Toplevel()
history = Toplevel()
# matplot = Toplevel()
Qabz = Toplevel()
# tarikhche = Toplevel()
style = ttk.Style()
     
#---------PagesBGs-Images---------------
img1 = PhotoImage(file = "pics/login.png")
img2 = PhotoImage(file = 'pics/mainpg.png')
img3 = PhotoImage(file = 'pics/register-page.png')
img12 = PhotoImage(file = 'pics/product-pg.png')
img24 = PhotoImage(file = 'pics/AddEmployee-pg.png')
img25 = PhotoImage(file = 'pics/mojodi-pg.png')
img27 = PhotoImage(file = 'pics/sabtVorodPage.png')
img29 = PhotoImage(file = 'pics/reqPage.png')
img31 = PhotoImage(file = 'pics/SefareshKalaPg.png')
img33 = PhotoImage(file = 'pics/ExportKalaPg.png')
img36 = PhotoImage(file ='pics/HistoryPg.png')
img37 = PhotoImage(file = 'pics/qabzPg.png')
img38 = PhotoImage(file = 'pics/tarikhchePg.png')
#---------Main-PageBtns-Images----------
img4 = PhotoImage(file = 'pics/fish.png')
img5 = PhotoImage(file = 'pics/darkhast.png')
img6 = PhotoImage(file = 'pics/mojodi.png')
img7 = PhotoImage(file = 'pics/resid.png')
img8 = PhotoImage(file = 'pics/sabtKala.png')
img9 = PhotoImage(file = 'pics/sabtKarbar.png')
img35 = PhotoImage(file = 'pics/SabtKhorojBtn.png')
img41 = PhotoImage(file = 'pics/HistoryBtn.png')
#---------login-PageBtns-Images----------
img10 = PhotoImage(file = 'pics/login-btn.png')
img15 = PhotoImage(file = 'pics/cheshm-baste.png')
#---------Register-PageBtns-Images----------
img11 = PhotoImage(file = 'pics/register-btn.png')
#---------product-PageBtns-Images----------
img13 = PhotoImage(file = 'pics/sabt-btn.png')
img14 = PhotoImage(file = 'pics/main-btn.png')
img16 = PhotoImage(file = 'pics/select-img.png')
img18 = PhotoImage(file = 'pics/hazf-hame.png')
img19 = PhotoImage(file = 'pics/hazf-choose.png')
img20 = PhotoImage(file = 'pics/hazf.png')
img21 = PhotoImage(file = 'pics/update.png')
img22 = PhotoImage(file = 'pics/sub-update.png')
img23 = PhotoImage(file = 'pics/Search-btn.png')
img28 = PhotoImage(file = 'pics/Search-btn1.png')
#---------product-select-Images----------
img17 = PhotoImage(file = 'pics/resid.png')
#---------Add-employee-PageBtns-Images----------
#---------mojodi-PageBtns-Images----------
img26 = PhotoImage(file = 'pics/searchBtn-mojodi.png')
#---------reqProduct-PageBtns-Images----------
img30 = PhotoImage(file = 'pics/sefaresh-btn.png')
#---------DarKhast-PageBtns-Images----------
img32 = PhotoImage(file ='pics/khoroj-btn.png')
#---------DarKhast-PageBtns-Images----------
img34 = PhotoImage(file = 'pics/export-btn.png')
#---------History-PageBtns-Images----------
img39  = PhotoImage(file = 'pics/qabz-btn.png')
img40 = PhotoImage(file = 'pics/chart-btn.png')
class app:
    '''
    Hani ShahabiZadeh
    2023/04/2
    age 18 
    Advanced Python project
    Version 1 Warehouse app
    '''
    def __init__(self,event = None): 
        self.MainPage()
        self.loginPage()
        self.registerPage()
        self.ProductPage()
        self.AddEmployeePage()
        self.mojodi_page()
        self.exportProductPage()
        self.historyPage()
        self.qabzPage()
        self.lst = []
        self.lst_emp = []
        self.lst_mojodi = []
        self.lst_vorodi = []
        self.lst_vorodi_req = []
        self.lst_sefaresh = []
        self.lst_export = []
        self.count = 1
        self.count1 = 0
        self.count2 = 0
        self.count3 = 1
        self.sabtVorodPage()
        self.reqKalaPage()
        self.SefareshKalaPage()
        self.checkRegisterTable()
    def MainPage(self, event = None) :
        root.geometry('1200x720+150+20')
        root.state('withdraw')
        root.title('نرم افزار انبار داری')
        self.main_lbl = Label(root, width = 1184 , height = 709 , bg = 'white' , image = img2 )

        self.fishBtn = Button(root, width = 157 , height  = 62 , image = img4 , activebackground= '#EEEEEE', borderwidth = 0 , command = self.darKhastKhoroj)
        self.fishBtn.place(x = 90 , y = 120)

        self.fishBtn.bind('<Enter>',lambda event : self.hoverBtn(img4,'pics/fish-hover.png'))
        self.fishBtn.bind('<Leave>',lambda event : self.hoverBtn(img4,'pics/fish.png'))

        self.sabtKhorojBtn = Button(root, width = 157 , height  = 62 , image = img35 , activebackground= '#EEEEEE', borderwidth = 0 , command = self.exportProductPopUp)
        self.sabtKhorojBtn.place(x = 626 , y = 190)

        self.sabtKhorojBtn.bind('<Enter>',lambda event : self.hoverBtn(img35,'pics/SabtKhorojBtn-hover.png'))
        self.sabtKhorojBtn.bind('<Leave>',lambda event : self.hoverBtn(img35,'pics/SabtKhorojBtn.png'))
        

        self.darkhastKharidBtn = Button(root, width = 157 , height  = 62 , image = img7 ,activebackground= '#EEEEEE', borderwidth = 0 , command = self.DarkhastKharid)
        self.darkhastKharidBtn.place(x = 263 , y = 120)  

        self.darkhastKharidBtn.bind('<Enter>',lambda event : self.hoverBtn(img7,'pics/resid-hover.png'))
        self.darkhastKharidBtn.bind('<Leave>',lambda event : self.hoverBtn(img7,'pics/resid.png'))


        self.darkhastBtn = Button(root, width = 157 , height  = 62 , image = img5,activebackground= '#EEEEEE', borderwidth = 0 , command= self.sabtvorodKala)
        self.darkhastBtn.place(x = 436 , y = 120)

        self.darkhastBtn.bind('<Enter>',lambda event : self.hoverBtn(img5,'pics/darkhast-hover.png'))
        self.darkhastBtn.bind('<Leave>',lambda event : self.hoverBtn(img5,'pics/darkhast.png'))

        self.mojodiBtn = Button(root, width = 157 , height  = 62 , image = img6 , activebackground= '#EEEEEE', borderwidth = 0, command = self.MojodiPage)
        self.mojodiBtn.place(x = 609 , y = 120)

        self.mojodiBtn.bind('<Enter>',lambda event : self.hoverBtn(img6,'pics/mojodi-hover.png'))
        self.mojodiBtn.bind('<Leave>',lambda event : self.hoverBtn(img6,'pics/mojodi.png'))

        self.sbtKarbarBtn = Button(root, width = 157 , height  = 63 , image = img9,activebackground= '#EEEEEE', borderwidth = 0, command = self.sabtKarmandPage)
        self.sbtKarbarBtn.place(x = 782 , y = 120)

        self.sbtKarbarBtn.bind('<Enter>',lambda event : self.hoverBtn(img9,'pics/sabtKarbar-hover.png'))
        self.sbtKarbarBtn.bind('<Leave>',lambda event : self.hoverBtn(img9,'pics/sabtKarbar.png'))

        self.sbtKalaBtn = Button(root, width = 157 , height  = 62 , image = img8,activebackground= '#EEEEEE', borderwidth = 0 , command = self.sabtKalaPage )
        self.sbtKalaBtn.place(x = 955 , y = 121)

        self.sbtKalaBtn.bind('<Enter>',lambda event : self.hoverBtn(img8,'pics/sabtKala-hover.png'))
        self.sbtKalaBtn.bind('<Leave>',lambda event : self.hoverBtn(img8,'pics/sabtKala.png'))
      
        self.tarikhcheSefareshatBtn = Button(root, width = 190 , height  = 63 , image = img41 ,activebackground= '#EEEEEE', borderwidth = 0, command = self.historyPagePopUp )
        self.tarikhcheSefareshatBtn.place(x = 419 , y = 190)
        self.tarikhcheSefareshatBtn.bind('<Enter>',lambda event : self.hoverBtn(img41,'pics/HistoryBtn-hover.png'))
        self.tarikhcheSefareshatBtn.bind('<Leave>',lambda event : self.hoverBtn(img41,'pics/HistoryBtn.png'))

        self.main_lbl.place(x = 5 , y = 0)

    def loginPage(self, event = None):
        loginpage.state('withdraw')
        loginpage.title('ورود به پنل کاربری')
        loginpage.geometry('852x588+250+20')
        self.login_main_lbl = Label(loginpage , width = 852 , height = 588 , bg = 'white')
        self.login_main_lbl.place(x = 0 , y = 0)
        self.login_lbl = Label(loginpage , width = 815 , height = 550 , bg = 'white' , image = img1 )
        self.login_lbl.place(x = 15, y = 15)

        self.username_ent = Entry(loginpage , width = 27 , font = ('B Nazanin' , 11), bg = 'white' ,border=0 )
        self.username_ent.place(x = 528 , y = 166)
        self.username_ent.focus()

        self.username_ent.bind('<Return>', lambda event : self.password_ent.focus())

        self.password_ent = Entry(loginpage , show = '*', width = 27 , font = ('B Nazanin' , 11), bg = 'white', border=0 )
        self.password_ent.place(x = 528 , y = 265)

        self.password_ent.bind('<Return>', lambda event : self.login_btn.focus())
        self.cheshm = Button(loginpage , width = 35, image = img15 , bg = '#ffffff' , activebackground='#ffffff' , borderwidth = 0 , command = self.hide)
        self.cheshm.place(x = 476, y = 260)
        self.cheshm.bind('<Button-1>',self.hide)
        self.login_btn = Button(loginpage , bg = 'white' , width = 211 , height = 65 , image = img10 ,activebackground= '#ffffff', borderwidth = 0 , command= self.checkIdAndPass)
        self.login_btn.place( x = 528 , y = 378)

        self.login_btn.bind('<Enter>',lambda event : self.hoverBtn(img10,'pics/login-btn-hover.png'))
        self.login_btn.bind('<Leave>',lambda event : self.hoverBtn(img10,'pics/login-btn.png'))


    def checkIdAndPass(self):
        con = sql.connect('mydb.db')
        cur = con.cursor()
        row = cur.execute('SELECT * FROM Register')
        lst = list(row)
        if self.username_ent.get() == lst[0][0] and self.password_ent.get() == lst[0][2] :
            loginpage.state('withdrawn')
            root.state('normal')
        else :
            messagebox.showerror('error','مجددا تلاش کنید. نام کاربری یا رمز عبور ثبت نشده است')

    def registerPage(self, event = None):
        self.registerpage = registerpage
        registerpage.title('ثبتنام')
        self.registerpage.state('withdraw')

        self.registerpage.geometry('852x588+250+20')
        self.register_lbl = Label(self.registerpage , width = 815 , height = 550 , bg = 'white' , image = img3 )
        self.register_lbl.place(x = 15, y = 15)

        self.name_ent = Entry(self.registerpage , width = 25 , font = ('B Nazanin' , 11), bg = 'white', border = 0, justify= 'right' )
        self.name_ent.place(x = 602, y = 180)
        self.name_ent.focus()
        self.name_ent.bind('<Return>', lambda event : self.last_ent.focus())


        self.last_ent = Entry(self.registerpage , width = 25 , font = ('B Nazanin' , 11), bg = 'white', border = 0, justify= 'right' )
        self.last_ent.place(x = 380, y = 180)
        self.last_ent.bind('<Return>', lambda event : self.email_ent.focus())
        

        self.email_ent = Entry(self.registerpage , width = 41 , font = ('B Nazanin' , 11), bg = 'white', border = 0, justify= 'right' )
        self.email_ent.place(x = 380, y = 251)
        self.email_ent.bind('<Return>', lambda event : self.pass_ent.focus())

        self.pass_ent = Entry(self.registerpage , width = 25 , font = ('B Nazanin' , 11), bg = 'white', border = 0, justify= 'right' )
        self.pass_ent.place(x = 605, y = 347)
        self.pass_ent.bind('<Return>', lambda event : self.re_pass_ent.focus())


        self.re_pass_ent = Entry(self.registerpage , width = 25 , font = ('B Nazanin' , 11), bg = 'white', border = 0, justify= 'right' )
        self.re_pass_ent.place(x = 376, y = 347)

        self.re_pass_ent.bind('<Return>', lambda event : self.register_btn.focus())


        self.register_btn = Button(self.registerpage , bg = 'white' , width = 211 , height = 65 , image = img11 ,activebackground= '#ffffff', borderwidth = 0 , command= self.TableRegister)
        self.register_btn.place( x = 487 , y = 442)
        self.register_btn.bind('<Enter>',lambda event : self.hoverBtn(img11,'pics/register-btn-hover.png'))
        self.register_btn.bind('<Leave>',lambda event : self.hoverBtn(img11,'pics/register-btn.png'))

        # self.register_btn.bind('<Return>', self.register_sub)


    def TableRegister(self):
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.command='''CREATE TABLE IF NOT EXISTS Register (nam TEXT,
                                                             lastName TEXT,
                                                             password TEXT,
                                                             repassword TEXT, 
                                                             email TEXT)'''
        self.cur.execute(self.command)

        self.data = (self.name_ent.get(),
                    self.last_ent.get(),
                    self.pass_ent.get(),
                    self.re_pass_ent.get(),
                    self.email_ent.get())
        self.cur.execute('''INSERT INTO Register (nam,lastName,password,repassword,email) VALUES (?,?,?,?,?)''',self.data)
        self.con.commit()
        self.con.close()
        messagebox.showinfo('ثبتنام', '!مشخصات شما با موفقیت ثبت شد')

    def checkRegisterTable(self):
        self.con = sql.connect('mydb.db')
        self.cur = self.con.cursor()
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
        self.tables = self.cur.fetchall()
        if len(self.tables) == 0:
            registerpage.state('normal')
            print('registerpage')
        else:
            self.loginState()
            print('loginpage')
          
        self.con.close()

    def loginState(self):
        loginpage.state('normal')
        


    def ProductPage(self, event = None) :
        self.productpage = productpage
        productpage.title('ثبت کالا')
        productpage.geometry('1200x720+150+20')
        productpage.state('withdraw')
        self.product_main_lbl = Label(productpage , bg = 'white' , width = 1200, height = 720 )
        self.product_main_lbl.place( x = 0 , y = 0)

        self.product_lbl = Label(productpage , bg = 'white' , width = 1150 , height = 676 , image = img12)
        self.product_lbl.place(x = 25 , y = 25)

        self.e_nam_kala = Entry(productpage, width = 22 , font = ('B Nazanin' , 10), bg = 'white', border = 0 , justify ='right')
        self.e_nam_kala.place( x = 865 , y = 150)
        self.e_nam_kala.focus()
        self.e_nam_kala.bind('<Return>', lambda event : self.e_noe_kala.focus())

        self.noeKala_options = ['موتوری', 'خانگی']
        self.e_noe_kala = ttk.Combobox(productpage, state = 'readonly', value = self.noeKala_options , width = 15 , font = ('Segoe UI' , 11) , justify = 'right' )
        self.e_noe_kala.set('انتخاب کنید')
        self.e_noe_kala.place( x = 614, y = 149)

        self.e_noe_kala.bind('<Return>', lambda event : self.e_code_kala.focus())
        
        self.e_code_kala = Entry(productpage, width = 22 , font = ('B Nazanin' , 10), bg = 'white', border = 0 , justify ='right')
        self.e_code_kala.place( x = 385 , y = 150)
        
        self.e_code_kala.bind('<Return>', lambda event : self.e_group_kala.focus())
        

        self.groupKala_options = ['دریافتی', 'درخواستی']
        self.e_group_kala = ttk.Combobox(productpage,state = 'readonly', value = self.groupKala_options , width = 15 , font = ('Segoe UI' , 11) , justify = 'right' )
        self.e_group_kala.place( x = 93 , y = 149)
        self.e_group_kala.set('انتخاب کنید')

        self.e_group_kala.bind('<Return>', lambda event : self.e_tozihat.focus())


        self.e_tozihat = Entry(productpage, width = 78 , font = ('B Nazanin' , 10), bg = 'white', border = 0 , justify ='right')
        self.e_tozihat.place( x = 362 , y = 247)

        self.e_tozihat.bind('<Return>', lambda event : self.e_noqte.focus())

        
        self.e_noqte = Entry(productpage, width = 20 , font = ('B Nazanin' , 10), bg = 'white', border = 0 , justify ='right')
        self.e_noqte.place( x = 797, y = 303)


        self.e_search = Entry(productpage, width = 20 , font = ('B Nazanin' , 10), bg = 'white', border = 0 , justify ='right')
        self.e_search.place( x = 888, y = 356)
        self.search_btn = Button(productpage , bg = '#eeeeee' , width = 70, height = 38 , image = img23 ,activebackground= '#eeeeee', borderwidth = 0 , command= self.search )
        self.search_btn.place(x = 1020, y = 347) 

        self.e_noqte.bind('<Return>', lambda event : self.e_search.focus())


        self.select_img_btn = Button(productpage , bg = 'white' , width = 105 , height = 37 , image = img16 ,activebackground= '#ffffff', borderwidth = 0, command = self.select_image )
        self.select_img_btn.place(x =123 , y = 351) 
        self.select_img_btn.bind('<Enter>',lambda event : self.hoverBtn(img16,'pics/select-img-hover.png'))
        self.select_img_btn.bind('<Leave>',lambda event :  self.hoverBtn(img16,'pics/select-img.png'))

        self.sub_btn = Button(productpage , bg = 'white' , width = 147 , height = 40 , image = img13 ,activebackground= '#ffffff', borderwidth = 0 , command = self.AddKala_to_sql)
        self.sub_btn.place(x = 440 , y = 650) 
        self.sub_btn.bind('<Enter>',lambda event : self.hoverBtn(img13,'pics/sabt-btn-hover.png'))
        self.sub_btn.bind('<Leave>',lambda event : self.hoverBtn(img13,'pics/sabt-btn.png'))

        self.mainPage_btn = Button(productpage , bg = 'white' , width = 147 , height = 40 , image = img14 ,activebackground= '#ffffff', borderwidth = 0 , command = self.BackMenu)
        self.mainPage_btn.place(x = 603 , y = 650) 
        self.mainPage_btn.bind('<Enter>',lambda event : self.hoverBtn(img14,'pics/main-btn-hover.png'))
        self.mainPage_btn.bind('<Leave>',lambda event : self.hoverBtn(img14,'pics/main-btn.png'))



        self.delete_btn = Button(productpage , bg = '#eeeeee' , width = 147 , height = 38 , image = img20 ,activebackground= '#eeeeee', borderwidth = 0 ,  command = self.Remove)
        self.delete_btn.place(x = 420 , y = 602) 
        self.delete_btn.bind('<Enter>',lambda event : self.hoverBtn(img20,'pics/hazf-hover.png'))
        self.delete_btn.bind('<Leave>',lambda event : self.hoverBtn(img20,'pics/hazf.png'))


        self.delete_all_btn = Button(productpage , bg = '#eeeeee' , width =  90 , height = 38 , image = img18 ,activebackground= '#eeeeee', borderwidth = 0 , command = self.Remove_all)
        self.delete_all_btn.place(x = 550, y = 602)   
        self.delete_all_btn.bind('<Enter>',lambda event : self.hoverBtn(img18,'pics/hazf-hame-hover.png'))
        self.delete_all_btn.bind('<Leave>',lambda event : self.hoverBtn(img18,'pics/hazf-hame.png'))

        self.update_sub_btn = Button(productpage , bg = '#eeeeee' , width = 120, height = 38 , image = img22 ,activebackground= '#eeeeee', borderwidth = 0 , command = self.edit)
        self.update_sub_btn.place(x = 650, y = 602) 
        self.update_sub_btn.bind('<Enter>',lambda event : self.hoverBtn(img22,'pics/sub-update-hover.png'))
        self.update_sub_btn.bind('<Leave>',lambda event : self.hoverBtn(img22,'pics/sub-update.png'))

        self.show_image = Label(productpage, image = img17 , relief="flat", width = 100 , height= 95)
        self.show_image.place(x=125, y= 242)

        self.show_tree = ttk.Treeview(productpage ,  style="mystyle.Treeview", height = 6)
        self.show_tree['columns'] = ('noqte','category','id','Type','Name','row')

        self.show_tree.column('#0', width = 0  ,stretch = NO)
        self.show_tree.column('row', width = 60 , anchor = CENTER , minwidth = 60 )
        self.show_tree.column('id', width = 100 , anchor = CENTER , minwidth = 100 )
        self.show_tree.column('Name', width = 150 , anchor = CENTER , minwidth = 150 )
        self.show_tree.column('category' ,width = 150 , anchor = CENTER , minwidth = 150 )
        self.show_tree.column('noqte' ,width = 156 , anchor = CENTER, minwidth = 156 )
        self.show_tree.column('Type' ,width = 150 , anchor = CENTER, minwidth = 150  )
        self.show_tree.heading('#0', text = ' ' , anchor = CENTER)
        self.show_tree.heading('row', text = 'ردیف' , anchor = CENTER )
        self.show_tree.heading('id', text = 'کد کالا' , anchor = CENTER )
        self.show_tree.heading('Name', text = 'نام کالا' , anchor = CENTER )
        self.show_tree.heading('category', text = 'گروه کالا' , anchor = CENTER)
        self.show_tree.heading('noqte', text = ' نقطه خرید' , anchor = CENTER)
        self.show_tree.heading('Type'   , text = ' نوع کالا' , anchor = CENTER )
        style.theme_use("clam")
        style.configure("mystyle.Treeview.Heading",
                        background = '#A0A0A0',
                        font=('Segoe UI', 15,'bold'), 
                        relief = 'flat', bd=1
                        ) 
        style.map("mystyle.Treeview.Heading",
            background=[('active','#A0A0A0')])
        
        style.configure("mystyle.Treeview", highlightthickness=0, 
                                bd=0, font=('Segoe UI', 11),
                                background="#EEEEEE",
                                foreground="black",
                                rowheight = 21,
                                fieldbackground="#EEEEEE",   
                                )
        self.show_tree.place(x = 218 , y = 415)
        self.show_tree.bind('<ButtonRelease-1>', self.show_info)
        style.map("mystyle.Treeview",
            background=[('selected', '#727272')])
    
    def AddEmployeePage(self, event = None):
        self.employeepage = employeepage
        employeepage.title('ثبت کارمند')
        employeepage.geometry('1200x720+150+20')
        employeepage.state('withdraw')
        self.employee_main_lbl = Label(employeepage , bg = 'white' , width = 1200, height = 720 )
        self.employee_main_lbl.place( x = 0 , y = 0)
        
        self.employee_lbl = Label(employeepage , bg = 'white' , width = 1150 , height = 676 , image = img24)
        self.employee_lbl.place(x = 25 , y = 25)

        self.e_nam = Entry(employeepage, width = 22 , font = ('B Nazanin' , 10), bg = 'white', border = 0 , justify ='right')
        self.e_nam.place( x = 772 , y = 155)
        self.e_nam.focus()
        self.e_nam.bind('<Return>', lambda event : self.e_family.focus())

        self.e_family = Entry(employeepage, width = 22 , font = ('B Nazanin' , 10), bg = 'white', border = 0 , justify ='right')
        self.e_family.place( x = 772 , y = 202)#47
        self.e_family.bind('<Return>', lambda event : self.e_code_meli.focus())

        self.e_code_meli = Entry(employeepage, width = 22 , font = ('B Nazanin' , 10), bg = 'white', border = 0 , justify ='right')
        self.e_code_meli.place( x = 772 , y = 247)
        self.e_code_meli.bind('<Return>', lambda event : self.e_jensiat_combo.focus())

        self.e_jensiat_combo = ttk.Combobox(employeepage,background = 'white', width = 21 , font = ('B Nazanin' , 10),value = ['مرد' ,'زن'] ,state = 'readonly' , justify ='right')
        self.e_jensiat_combo.place( x = 767 , y = 293)
        self.e_jensiat_combo.bind('<Return>', lambda event : self.e_position_combo.focus())
        self.e_jensiat_combo.set('انتخاب کنید')
        

        self.e_position_combo = ttk.Combobox(employeepage,background = 'white', width = 21 , font = ('B Nazanin' , 10),value = ['کارمند', 'مدیر', 'فروشنده', 'سر کارگر'], state = 'readonly' , justify ='right')
        self.e_position_combo.set('انتخاب کنید')
        self.e_position_combo.place( x = 258, y = 161)
        
        self.show_image_employee = Label(employeepage, image = img17 , relief="flat",width = 100 , height= 95, bg = 'black')
        self.show_image_employee.place(x=139, y= 146)

        self.select_img_btn_employee = Button(employeepage , bg = '#A7A7A7' , width = 105 , height = 37 , image = img16 ,activebackground= '#A7A7A7', borderwidth = 0, command = self.select_image )
        self.select_img_btn_employee.place(x =139 , y = 265) 
        self.select_img_btn_employee.bind('<Enter>',lambda event : self.hoverBtn(img16,'pics/select-img-hover.png'))
        self.select_img_btn_employee.bind('<Leave>',lambda event :  self.hoverBtn(img16,'pics/select-img.png'))

        self.e_search_employee = Entry(employeepage, width = 20 , font = ('B Nazanin' , 10), bg = 'white', border = 0 , justify ='right')
        self.e_search_employee.place( x = 320, y = 220)
        self.e_position_combo.bind('<Return>', lambda event : self.e_search_employee.focus())

        self.search_btn_employee = Button(employeepage , bg = '#A7A7A7' , width = 70, height = 38 , image = img23 ,activebackground= '#A7A7A7', borderwidth = 0 , command= self.search_emp )
        self.search_btn_employee.place(x = 450, y = 212) 


        self.sub_btn = Button(employeepage , bg = 'white' , width = 147 , height = 40 , image = img13 ,activebackground= '#ffffff', borderwidth = 0 , command = self.Addemp_to_sql)
        self.sub_btn.place(x = 440 , y = 650) 
        self.sub_btn.bind('<Enter>',lambda event : self.hoverBtn(img13,'pics/sabt-btn-hover.png'))
        self.sub_btn.bind('<Leave>',lambda event : self.hoverBtn(img13,'pics/sabt-btn.png'))

        self.mainPage_btn = Button(employeepage , bg = 'white' , width = 147 , height = 40 , image = img14 ,activebackground= '#ffffff', borderwidth = 0 , command = self.BackMenu)
        self.mainPage_btn.place(x = 603 , y = 650) 
        self.mainPage_btn.bind('<Enter>',lambda event : self.hoverBtn(img14,'pics/main-btn-hover.png'))
        self.mainPage_btn.bind('<Leave>',lambda event : self.hoverBtn(img14,'pics/main-btn.png'))



        self.delete_btn = Button(employeepage , bg = '#eeeeee' , width = 147 , height = 38 , image = img20 ,activebackground= '#eeeeee', borderwidth = 0 ,  command = self.Remove_emp)
        self.delete_btn.place(x = 420 , y = 602) 
        self.delete_btn.bind('<Enter>',lambda event : self.hoverBtn(img20,'pics/hazf-hover.png'))
        self.delete_btn.bind('<Leave>',lambda event : self.hoverBtn(img20,'pics/hazf.png'))


        self.delete_all_btn = Button(employeepage , bg = '#eeeeee' , width =  90 , height = 38 , image = img18 ,activebackground= '#eeeeee', borderwidth = 0 , command = self.Remove_all_emp)
        self.delete_all_btn.place(x = 550, y = 602)   
        self.delete_all_btn.bind('<Enter>',lambda event : self.hoverBtn(img18,'pics/hazf-hame-hover.png'))
        self.delete_all_btn.bind('<Leave>',lambda event : self.hoverBtn(img18,'pics/hazf-hame.png'))

        self.update_sub_btn_emp = Button(employeepage , bg = '#eeeeee' , width = 120, height = 38 , image = img22 ,activebackground= '#eeeeee', borderwidth = 0 , command = self.edit_emp)
        self.update_sub_btn_emp.place(x = 650, y = 602) 
        self.update_sub_btn_emp.bind('<Enter>',lambda event : self.hoverBtn(img22,'pics/sub-update-hover.png'))
        self.update_sub_btn_emp.bind('<Leave>',lambda event : self.hoverBtn(img22,'pics/sub-update.png'))


        self.show_tree_employee = ttk.Treeview(employeepage ,  style="mystyle.Treeview", height = 6)
        self.show_tree_employee['columns'] = ('jobPosition','gender','id','lastname','Name','row')

        self.show_tree_employee.column('#0', width = 0  ,stretch = NO)
        self.show_tree_employee.column('row', width = 60 , anchor = CENTER , minwidth = 60 )
        self.show_tree_employee.column('Name', width = 150 , anchor = CENTER , minwidth = 150 )
        self.show_tree_employee.column('lastname' ,width = 150 , anchor = CENTER , minwidth = 150 )
        self.show_tree_employee.column('id', width = 100 , anchor = CENTER , minwidth = 100 )
        self.show_tree_employee.column('gender' ,width = 156 , anchor = CENTER, minwidth = 156 )
        self.show_tree_employee.column('jobPosition' ,width = 150 , anchor = CENTER, minwidth = 150  )
        self.show_tree_employee.heading('#0', text = ' ' , anchor = CENTER)
        self.show_tree_employee.heading('row', text = 'ردیف' , anchor = CENTER )
        self.show_tree_employee.heading('Name', text = 'نام' , anchor = CENTER )
        self.show_tree_employee.heading('lastname', text = 'نام خانوادگی' , anchor = CENTER)
        self.show_tree_employee.heading('id', text = 'کد ملی' , anchor = CENTER )
        self.show_tree_employee.heading('gender', text = 'جنسیت' , anchor = CENTER)
        self.show_tree_employee.heading('jobPosition'   , text = 'جایگاه شغلی' , anchor = CENTER )
        style.theme_use("clam")
        style.configure("mystyle.Treeview.Heading",
                        background = '#A0A0A0',
                        font=('Segoe UI', 15,'bold'), 
                        relief = 'flat', bd=1
                        ) 
        style.map("mystyle.Treeview.Heading",
            background=[('active','#A0A0A0')])
        
        style.configure("mystyle.Treeview", highlightthickness=0, 
                                bd=0, font=('Segoe UI', 11),
                                background="#EEEEEE",
                                foreground="black",
                                # rowheight = 20,
                                fieldbackground="#EEEEEE",   
                                )
        self.show_tree_employee.place(x = 218 , y = 415)
        self.show_tree_employee.bind('<ButtonRelease-1>', self.show_info_emp)
        style.map("mystyle.Treeview",
            background=[('selected', '#727272')])
        
    def mojodi_page(self):
        self.mojodipage = mojodipage
        mojodipage.title('موجودی کالاها')

        mojodipage.geometry('1200x720+150+20')
        mojodipage.state('withdraw')
        self.mojodipage_main_lbl = Label(mojodipage , bg = 'white' , width = 1200, height = 720 )
        self.mojodipage_main_lbl.place( x = 0 , y = 0)
        self.mojodipage_lbl = Label(mojodipage , bg = 'white' , width = 1150 , height = 676 , image = img25)
        self.mojodipage_lbl.place(x = 25 , y = 25)
        self.e_search_mojodi = Entry(mojodipage, width = 16 , font = ('B Nazanin' , 10), bg = 'white', border = 0 , justify ='right')
        self.e_search_mojodi.place( x = 1048, y = 158)
        self.search_btn_mojodi = Button(mojodipage , bg = '#F8F8F8' , width = 80, height = 38 , image = img26 ,activebackground= '#F8F8F8', borderwidth = 0 , command= self.search_stock )
        self.search_btn_mojodi.place(x = 1058, y = 200) 
        self.search_btn_mojodi.bind('<Enter>',lambda event : self.hoverBtn(img26,'pics/searchBtn-mojodi-hover.png'))
        self.search_btn_mojodi.bind('<Leave>',lambda event : self.hoverBtn(img26,'pics/searchBtn-mojodi.png'))

        self.deleteAll_btn_mojodi = Button(mojodipage , bg = '#F8F8F8' , width = 84, height = 38 , image = img18 ,activebackground= '#F8F8F8', borderwidth = 0  , command = self.Remove_all_stock  )
        self.deleteAll_btn_mojodi.place(x = 1055, y = 360) 
        self.deleteAll_btn_mojodi.bind('<Enter>',lambda event : self.hoverBtn(img18,'pics/hazf-hame-hover.png'))
        self.deleteAll_btn_mojodi.bind('<Leave>',lambda event : self.hoverBtn(img18,'pics/hazf-hame.png'))

        self.delete_btn_mojodi = Button(mojodipage , bg = '#F8F8F8' , width = 80, height = 38 , image = img20 ,activebackground= '#F8F8F8', borderwidth = 0 , command = self.Remove_stock )
        self.delete_btn_mojodi.place(x = 1058, y = 410) 
        self.delete_btn_mojodi.bind('<Enter>',lambda event : self.hoverBtn(img20,'pics/hazf-hover.png'))
        self.delete_btn_mojodi.bind('<Leave>',lambda event : self.hoverBtn(img20,'pics/hazf.png'))
        self.e_search_mojodi.focus()
        
        self.mainPage_btn = Button(mojodipage , bg = 'white' , width = 147 , height = 40 , image = img14 ,activebackground= '#ffffff', borderwidth = 0 , command = self.BackMenu)
        self.mainPage_btn.place(x = 527 , y = 655) 
        self.mainPage_btn.bind('<Enter>',lambda event : self.hoverBtn(img14,'pics/main-btn-hover.png'))
        self.mainPage_btn.bind('<Leave>',lambda event : self.hoverBtn(img14,'pics/main-btn.png'))
        
        self.show_tree_mojodipage = ttk.Treeview(mojodipage ,  style="Mystyle.Treeview", height = 20)
        self.show_tree_mojodipage.place(x = 98 , y = 99)

        self.show_tree_mojodipage['columns'] = ('noqte','number','category','id','Type','Name','row')

        self.show_tree_mojodipage.column('#0', width = 0  ,stretch = NO)
        self.show_tree_mojodipage.column('row', width = 60 , anchor = CENTER , minwidth = 60 )
        self.show_tree_mojodipage.column('id', width = 100 , anchor = CENTER , minwidth = 100 )
        self.show_tree_mojodipage.column('Name', width = 150 , anchor = CENTER , minwidth = 150 )
        self.show_tree_mojodipage.column('category' ,width = 150 , anchor = CENTER , minwidth = 150 )
        self.show_tree_mojodipage.column('noqte' ,width = 156 , anchor = CENTER, minwidth = 156 )
        self.show_tree_mojodipage.column('Type' ,width = 150 , anchor = CENTER, minwidth = 150  )
        self.show_tree_mojodipage.column('number' ,width = 150 , anchor = CENTER, minwidth = 150  )

        self.show_tree_mojodipage.heading('#0', text = ' ' , anchor = CENTER)
        self.show_tree_mojodipage.heading('row', text = 'ردیف' , anchor = CENTER )
        self.show_tree_mojodipage.heading('id', text = 'کد کالا' , anchor = CENTER )
        self.show_tree_mojodipage.heading('Name', text = 'نام کالا' , anchor = CENTER )
        self.show_tree_mojodipage.heading('category', text = 'گروه کالا' , anchor = CENTER)
        self.show_tree_mojodipage.heading('noqte', text = 'نقطه خرید' , anchor = CENTER)
        self.show_tree_mojodipage.heading('Type'   , text = ' نوع کالا' , anchor = CENTER )
        self.show_tree_mojodipage.heading('number' , text = 'تعداد', anchor = CENTER  )
        style.theme_use("clam")
        style.configure("Mystyle.Treeview.Heading",
                        background = '#A0A0A0',
                        font=('Segoe UI', 15,'bold'), 
                        relief = 'flat', bd=1
                        ) 
        style.map("Mystyle.Treeview.Heading",
            background=[('active','#A0A0A0')])
        
        style.configure("Mystyle.Treeview", highlightthickness=0, 
                                bd=0, font=('Segoe UI', 11),
                                background="#F8F8F8",
                                foreground="black",
                                rowheight = 25,
                                fieldbackground="#F8F8F8",   
                                )
        style.map("Mystyle.Treeview",
            background=[('selected', '#727272')])
        self.show_tree_mojodipage.bind('<Button-1>', self.test)
        self.show_tree_mojodipage.bind('<ButtonRelease-1>', self.test)
    def data_to_stock(self,event = None):
        self.lst_mojodi = []
        for item in self.show_tree_mojodipage.get_children():
            self.show_tree_mojodipage.delete(item)
        self.count = 0
        self.con = sql.connect('mydb.db')
        self.cur = self.con.cursor()
        row = self.cur.execute('''SELECT  * FROM Kala''')
        for i in row :
            self.lst_mojodi.append(i)
        for i in self.lst_mojodi:
            self.show_tree_mojodipage.insert(parent='',index='end',text='',
                                 values=(i[5],i[7],i[3],i[2],i[1],i[0],str(self.count+1)))
            self.count += 1

    def test(self, event =  None):
        self.stock_selected = self.show_tree_mojodipage.focus()
        self.stock_values = self.show_tree_mojodipage.item(self.stock_selected , "values")
        print(self.stock_values)

    def Remove_stock(self):
        delete_one = self.show_tree_mojodipage.selection()[0]
        self.show_tree_mojodipage.delete(delete_one)
        con = sql.connect('mydb.db')
        cur = con.cursor()
        cur.execute('''DELETE FROM Kala WHERE code ='''+ self.stock_values[3])
        con.commit()
        con.close()
        messagebox.showinfo('حذف آیتم', '!آیتم شما با موفقیت حذف شد')

    def Remove_all_stock (self) :
        for i in self.show_tree_mojodipage.get_children():
            self.show_tree_mojodipage.delete(i)
        con = sql.connect('mydb.db')
        cur = con.cursor()
        command = ''' DELETE FROM Kala '''
        cur.execute(command)    
        con.commit()
        messagebox.showinfo('حذف آیتم', '!تمامی آیتم های شما با موفقیت حذف شد')

    def search_stock(self,event = None):
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.search_get_mo=self.e_search_mojodi.get()
        self.count=0
        if self.search_get_mo !='':
            for i in self.show_tree_mojodipage.get_children():
                self.show_tree_mojodipage.delete(i)
            self.row=self.cur.execute('SELECT * FROM kala WHERE code="{}"'.format(self.search_get_mo))
            self.search_list=list(self.row)

            self.show_tree_mojodipage.insert(parent='',index='end',iid=self.count,text='',
                                values=(self.search_list[0][5],
                                        self.search_list[0][7],
                                        self.search_list[0][3],
                                        self.search_list[0][2],
                                        self.search_list[0][1],
                                        self.search_list[0][0],
                                        str(self.count+1)))
        else:
            self.lst_mojodi=[]
            self.show_tree_mojodipage.delete('0')
            self.data_to_stock()

    def sabtVorodPage(self): 
        sabtvorod.geometry('1200x720+150+20')
        sabtvorod.title('ثبت ورود کالا')
        sabtvorod.state('withdraw')
        self.sabtvorod_main_lbl = Label(sabtvorod , bg = 'white' , width = 1200, height = 720 )
        self.sabtvorod_main_lbl.place( x = 0 , y = 0)
        self.sabtvorod_lbl = Label(sabtvorod , bg = 'white' , width = 1150 , height = 676 , image = img27)
        self.sabtvorod_lbl.place(x = 25 , y = 25)
        
        self.e_search_codeMeli = Entry(sabtvorod, width = 22 , font = ('B Nazanin' , 10), bg = 'white', border = 0 , justify ='right')
        self.e_search_codeMeli.place( x = 698, y = 109)

        self.search_codeMeli_btn = Button(sabtvorod , bg = '#EEEEEE' , width = 65, height = 28 , image = img23 ,activebackground= '#EEEEEE', borderwidth = 0 , command= self.show_info_Karmand )
        self.search_codeMeli_btn.bind('<Enter>',lambda event : self.hoverBtn(img23,'pics/Search-btn-hover.png'))

        self.search_codeMeli_btn.bind('<Leave>',lambda event : self.hoverBtn(img23,'pics/Search-btn.png'))
        self.search_codeMeli_btn.place(x = 612, y = 107) 

        self.e_search_codeKala = Entry(sabtvorod, width = 22 , font = ('B Nazanin' , 10), bg = 'white', border = 0 , justify ='right')
        self.e_search_codeKala.place( x = 141, y = 109)
        self.search_codeKala_btn = Button(sabtvorod , bg = '#EEEEEE' , width = 65, height = 28 , image = img28 ,activebackground= '#EEEEEE', borderwidth = 0 , command= self.show_info_Kala )
        self.search_codeKala_btn.bind('<Enter>',lambda event : self.hoverBtn(img28,'pics/Search-btn-hover.png'))
        self.search_codeKala_btn.bind('<Leave>',lambda event : self.hoverBtn(img28,'pics/Search-btn1.png'))
        self.search_codeKala_btn.place(x = 60 , y = 107) 

        self.namlbl = Label(sabtvorod , bg = '#EEEEEE', width = 18 , height = 1, font = ('Segoe UI' , 13, 'bold'), text = '' , fg = 'black', justify = 'right')
        self.namlbl.place(x = 760 , y = 183)

        self.lastNamelbl = Label(sabtvorod , bg = '#EEEEEE', width = 18 , height = 1, font = ('Segoe UI' , 13 , 'bold'), text = '' , fg = 'black', justify = 'right')
        self.lastNamelbl.place(x = 760 , y = 225)
        
        self.codeMelilbl = Label(sabtvorod , bg = '#EEEEEE', width = 18 , height = 1, font = ('Segoe UI' , 13, 'bold'), text = '' , fg = 'black', justify = 'right')
        self.codeMelilbl.place(x = 760 , y = 267)
        
        self.genderlbl = Label(sabtvorod , bg = '#EEEEEE', width = 18 , height = 1, font = ('Segoe UI' , 13, 'bold'), text = '' , fg = 'black', justify = 'right')
        self.genderlbl.place(x = 760 , y = 308  )
        
        self.e_Get_num = Entry(sabtvorod, width = 19 , font = ('B Nazanin' , 10 , 'bold'), bg = 'white', border = 0 , justify ='right')
        self.e_Get_num.place( x = 369, y = 322)
        self.e_Get_num.focus()

        self.e_Get_codeSefaresh = Entry(sabtvorod, width = 19 , font = ('B Nazanin' , 10 , 'bold'), bg = 'white', border = 0 , justify ='right')
        self.e_Get_codeSefaresh.place( x = 369, y = 358)

        
        self.e_GetDate_sabtvorod = DateEntry(sabtvorod, width = 18 , font = ('B Nazanin' , 11), bg = 'white', border = 0 ,background='#495057',sforeground='#DEE2E6', justify ='right')
        self.e_GetDate_sabtvorod.place( x = 120, y = 353)

        self.show_img_Vorodi = Label(sabtvorod , image = img17 , relief="flat",width = 100 , height= 95, bg = 'black')
        self.show_img_Vorodi.place(x = 177, y = 199 )
#----------------------------------------------------------------
        self.namKalalbl = Label(sabtvorod , bg = '#EEEEEE', width = 18 , height = 1, font = ('Segoe UI' , 12, 'bold'), text = '' , fg = 'black', justify = 'right')
        self.namKalalbl.place(x = 345 , y = 181 )
        
        self.codeKalalbl = Label(sabtvorod , bg = '#EEEEEE', width = 18 , height = 1, font = ('Segoe UI' , 13, 'bold'), text = '' , fg = 'black', justify = 'right')
        self.codeKalalbl.place(x = 345 , y = 214  )

        self.groupKalalbl = Label(sabtvorod , bg = '#EEEEEE', width = 18 , height = 1, font = ('Segoe UI' , 13, 'bold'), text = '' , fg = 'black', justify = 'right')
        self.groupKalalbl.place(x = 345 , y = 249  )
        
        self.NoeKalalbl = Label(sabtvorod , bg = '#EEEEEE', width = 18 , height = 1, font = ('Segoe UI' , 13, 'bold'), text = '' , fg = 'black', justify = 'right')
        self.NoeKalalbl.place(x = 345 , y = 283  )

        self.sub_btn_vorodi = Button(sabtvorod , bg = 'white' , width = 147 , height = 40 , image = img13 ,activebackground= '#ffffff', borderwidth = 0 , command= self.update_record_number)
        self.sub_btn_vorodi.place(x = 440 , y = 650) 
        self.sub_btn_vorodi.bind('<Enter>',lambda event : self.hoverBtn(img13,'pics/sabt-btn-hover.png'))
        self.sub_btn_vorodi.bind('<Leave>',lambda event : self.hoverBtn(img13,'pics/sabt-btn.png'))

        self.mainPage_btn = Button(sabtvorod , bg = 'white' , width = 147 , height = 40 , image = img14 ,activebackground= '#ffffff', borderwidth = 0 , command = self.BackMenu)
        self.mainPage_btn.place(x = 603 , y = 650) 
        self.mainPage_btn.bind('<Enter>',lambda event : self.hoverBtn(img14,'pics/main-btn-hover.png'))
        self.mainPage_btn.bind('<Leave>',lambda event : self.hoverBtn(img14,'pics/main-btn.png'))

        self.show_tree_Vorodi = ttk.Treeview(sabtvorod ,  style="Mystyle.Treeview", height = 8)
        self.show_tree_Vorodi.place(x = 80 , y = 399)

        self.show_tree_Vorodi['columns'] = ('date','noqte','number','category','id','Type','Name','orderCode','row')

        self.show_tree_Vorodi.column('#0', width = 0  ,stretch = NO)
        self.show_tree_Vorodi.column('row', width = 60 , anchor = CENTER , minwidth = 60 )
        self.show_tree_Vorodi.column('id', width = 100 , anchor = CENTER , minwidth = 100 )
        self.show_tree_Vorodi.column('Name', width = 150 , anchor = CENTER , minwidth = 150 )
        self.show_tree_Vorodi.column('category' ,width = 150 , anchor = CENTER , minwidth = 150 )
        self.show_tree_Vorodi.column('noqte' ,width = 156 , anchor = CENTER, minwidth = 156 )
        self.show_tree_Vorodi.column('Type' ,width = 150 , anchor = CENTER, minwidth = 150  )
        self.show_tree_Vorodi.column('number' ,width = 100 , anchor = CENTER, minwidth = 100  )
        self.show_tree_Vorodi.column('orderCode' ,width = 110 , anchor = CENTER, minwidth = 110  )
        self.show_tree_Vorodi.column('date' ,width = 70 , anchor = CENTER, minwidth = 70  )

        self.show_tree_Vorodi.heading('#0', text = ' ' , anchor = CENTER)
        self.show_tree_Vorodi.heading('row', text = 'ردیف' , anchor = CENTER )
        self.show_tree_Vorodi.heading('id', text = 'کد کالا' , anchor = CENTER )
        self.show_tree_Vorodi.heading('Name', text = 'نام کالا' , anchor = CENTER )
        self.show_tree_Vorodi.heading('category', text = 'گروه کالا' , anchor = CENTER)
        self.show_tree_Vorodi.heading('noqte', text = 'نقطه خرید' , anchor = CENTER)
        self.show_tree_Vorodi.heading('Type'   , text = ' نوع کالا' , anchor = CENTER )
        self.show_tree_Vorodi.heading('number' , text = 'تعداد', anchor = CENTER  )
        self.show_tree_Vorodi.heading('orderCode' , text = 'کد سفارش', anchor = CENTER  )
        self.show_tree_Vorodi.heading('date' , text = 'تاریخ', anchor = CENTER  )
        style.theme_use("clam")
        style.configure("Mystyle.Treeview.Heading",
                        background = '#A0A0A0',
                        font=('Segoe UI', 15,'bold'), 
                        relief = 'flat', bd=1
                        ) 
        style.map("Mystyle.Treeview.Heading",
            background=[('active','#A0A0A0')])
        
        style.configure("Mystyle.Treeview", highlightthickness=0, 
                                bd=0, font=('Segoe UI', 11),
                                background="#F8F8F8",
                                foreground="black",
                                rowheight = 25,
                                fieldbackground="#F8F8F8",   
                                )
        style.map("Mystyle.Treeview",
            background=[('selected', '#727272')])
#----------------------------------------------------------------------------------       
    def reqKalaPage(self):
        reqkalapage.title('درخواست خرید')
        reqkalapage.state('withdraw')
        reqkalapage.geometry('1200x720+150+20')
        reqkalapage.configure(bg = 'white')
        self.reqkalapage_lbl = Label(reqkalapage , bg = 'white' , width = 1150 , height = 676 , image = img29)
        self.reqkalapage_lbl.place(x = 25 , y = 25)
        
        self.show_tree_reqkalapage = ttk.Treeview(reqkalapage ,  style="Mystyle.Treeview", height = 16)
        self.show_tree_reqkalapage.place(x = 145 , y = 200)

        self.show_tree_reqkalapage['columns'] = ('noqte','number','category','id','Type','Name','row')

        self.show_tree_reqkalapage.column('#0', width = 0  ,stretch = NO)
        self.show_tree_reqkalapage.column('row', width = 60 , anchor = CENTER , minwidth = 60 )
        self.show_tree_reqkalapage.column('id', width = 100 , anchor = CENTER , minwidth = 100 )
        self.show_tree_reqkalapage.column('Name', width = 150 , anchor = CENTER , minwidth = 150 )
        self.show_tree_reqkalapage.column('category' ,width = 150 , anchor = CENTER , minwidth = 150 )
        self.show_tree_reqkalapage.column('noqte' ,width = 156 , anchor = CENTER, minwidth = 156 )
        self.show_tree_reqkalapage.column('Type' ,width = 150 , anchor = CENTER, minwidth = 150  )
        self.show_tree_reqkalapage.column('number' ,width = 150 , anchor = CENTER, minwidth = 150  )

        self.show_tree_reqkalapage.heading('#0', text = ' ' , anchor = CENTER)
        self.show_tree_reqkalapage.heading('row', text = 'ردیف' , anchor = CENTER )
        self.show_tree_reqkalapage.heading('id', text = 'کد کالا' , anchor = CENTER )
        self.show_tree_reqkalapage.heading('Name', text = 'نام کالا' , anchor = CENTER )
        self.show_tree_reqkalapage.heading('category', text = 'گروه کالا' , anchor = CENTER)
        self.show_tree_reqkalapage.heading('noqte', text = 'نقطه خرید' , anchor = CENTER)
        self.show_tree_reqkalapage.heading('Type'   , text = ' نوع کالا' , anchor = CENTER )
        self.show_tree_reqkalapage.heading('number' , text = 'تعداد', anchor = CENTER  )
        style.theme_use("clam")
        style.configure("Mystyle.Treeview.Heading",
                        background = '#A0A0A0',
                        font=('Segoe UI', 15,'bold'), 
                        relief = 'flat', bd=1
                        ) 
        style.map("Mystyle.Treeview.Heading",
            background=[('active','#A0A0A0')])
        
        style.configure("Mystyle.Treeview", highlightthickness=0, 
                                bd=0, font=('Segoe UI', 11),
                                background="#F8F8F8",
                                foreground="black",
                                rowheight = 25,
                                fieldbackground="#F8F8F8",   
                                )
        style.map("Mystyle.Treeview",
            background=[('selected', '#727272')])
        self.show_tree_reqkalapage.bind('<Button-1>', self.test)
        self.show_tree_reqkalapage.bind('<ButtonRelease-1>', self.test)
        self.sefaresh_btn = Button(reqkalapage , bg = 'white' , width = 147 , height = 40 , image = img30 ,activebackground= '#ffffff', borderwidth = 0 , command= self.req_order)#
        self.sefaresh_btn.place(x = 440 , y = 650) 
        self.sefaresh_btn.bind('<Enter>',lambda event : self.hoverBtn(img30,'pics/sefaresh-btn-hover.png'))
        self.sefaresh_btn.bind('<Leave>',lambda event : self.hoverBtn(img30,'pics/sefaresh-btn.png'))

        self.mainPage_btn = Button(reqkalapage , bg = 'white' , width = 147 , height = 40 , image = img14 ,activebackground= '#ffffff', borderwidth = 0 , command = self.BackMenu)
        self.mainPage_btn.place(x = 603 , y = 650) 
        self.mainPage_btn.bind('<Enter>',lambda event : self.hoverBtn(img14,'pics/main-btn-hover.png'))
        self.mainPage_btn.bind('<Leave>',lambda event : self.hoverBtn(img14,'pics/main-btn.png'))

    def data_to_req_table(self) :
        self.req_lst = []
        for i in self.show_tree_reqkalapage.get_children():
            self.show_tree_reqkalapage.delete(i)
        self.req_count=0
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.row=self.cur.execute('SELECT * FROM Kala')
        for i in self.row :
            self.req_lst.append(i)
        for i in self.req_lst:
            if int(i[5]) > int(i[7]) :
                self.show_tree_reqkalapage.insert(parent='',index='end',iid=self.req_count,text='',
                values=(i[5],i[7],i[3],i[2],i[1],i[0],str(self.req_count+1)))
                self.req_count += 1
    # def purchase_select(self, event = None) :
    def req_order(self,event = None) :
        self.purchase_selected = self.show_tree_reqkalapage.focus()
        self.purchase_values = self.show_tree_reqkalapage.item(self.purchase_selected , "values")
        sabtvorod.state("withdraw")
        con = sql.connect('mydb.db')
        cur = con.cursor()
        self.import_product_data = cur.execute('SELECT * FROM Kala WHERE code="{}"'.format(self.purchase_values[3]))
        self.import_product_data = list(self.import_product_data)
        print(self.purchase_values[3])
        self.minimum_number = int(self.import_product_data[0][5]) - int(self.import_product_data[0][7])
        self.e_Get_num.insert(0,self.minimum_number)
        # self.pr_code_ent.insert(0,self.req_values[4])
        self.import_prduct_fill()
        if sabtvorod.state != ('normal') :
            reqkalapage.state('withdraw')
            sabtvorod.state('normal')

        con = sql.connect('mydb.db')
        cur = con.cursor()
        cur.execute("SELECT photo FROM Kala WHERE code = '{}'".format(self.purchase_values[3]))
        self.image_data = cur.fetchone()[0]
        self.product_img = Image.open(io.BytesIO(self.image_data))
        self.product_photo = ImageTk.PhotoImage(self.product_img)
        self.show_img_Vorodi = Label(sabtvorod , image=self.product_photo, width = 100 , height= 95)
        self.show_img_Vorodi.place(x = 177, y = 199 )


    def import_prduct_fill(self):
        GetNumKala = self.e_Get_num.get()
        GetCodeKala = self.purchase_values[3]
        con = sql.connect('mydb.db')
        cur = con.cursor()
        data = cur.execute('SELECT * FROM Kala WHERE code="{}"'.format(GetCodeKala))
        data = list(data)
        print(data)
        self.namKalalbl['text']= data[0][0]
        self.codeKalalbl['text']= data[0][2]
        self.groupKalalbl['text']= data[0][3]
        self.NoeKalalbl['text']= data[0][1]
        self.e_search_codeKala.insert(0,data[0][2])

    def SefareshKalaPage(self):
        sefareshkala.title('درخواست خروج')
        sefareshkala.state('withdraw')
        sefareshkala.geometry('1200x720+150+20')
        sefareshkala.configure(bg = 'white')
        self.sefareshkala_lbl = Label(sefareshkala , bg = 'white' , width = 1150 , height = 676 , image = img31)
        self.sefareshkala_lbl.place(x = 25 , y = 25)

        self.e_search_codeMeli_sefaresh = Entry(sefareshkala, width = 20 , font = ('B Nazanin' , 10), bg = 'white', border = 0 , justify ='right')
        self.e_search_codeMeli_sefaresh.place( x = 850, y = 224)

        self.search_codeMeli_btn = Button(sefareshkala , bg = '#EEEEEE' , width = 65, height = 28 , image = img23 ,activebackground= '#EEEEEE', borderwidth = 0 , command= self.show_info_Karmand_sefaresh )
        self.search_codeMeli_btn.bind('<Enter>',lambda event : self.hoverBtn(img23,'pics/Search-btn-hover.png'))
        self.search_codeMeli_btn.bind('<Leave>',lambda event : self.hoverBtn(img23,'pics/Search-btn.png'))
        self.search_codeMeli_btn.place(x = 770, y = 221)

        self.e_search_codeKala_sefaresh = Entry(sefareshkala, width = 20 , font = ('B Nazanin' , 10), bg = 'white', border = 0 , justify ='right')
        self.e_search_codeKala_sefaresh.place( x = 850, y = 381)

        self.search_codeKala_btn_sefaresh = Button(sefareshkala , bg = '#EEEEEE' , width = 65, height = 28 , image = img28 ,activebackground= '#EEEEEE', borderwidth = 0 , command= self.show_info_KalaSefaresh )
        self.search_codeKala_btn_sefaresh.bind('<Enter>',lambda event : self.hoverBtn(img28,'pics/search-btn-hover.png'))
        self.search_codeKala_btn_sefaresh.bind('<Leave>',lambda event : self.hoverBtn(img28,'pics/search-btn.png'))
        self.search_codeKala_btn_sefaresh.place(x = 770, y = 377)

        self.namlbl_sefaresh = Label(sefareshkala , bg = '#EEEEEE', width = 13 , height = 1, font = ('Segoe UI' , 13, 'bold'), text = 'saxsaxsaxa' , fg = '#6D6D6D', justify = 'right')
        self.namlbl_sefaresh.place(x = 389 , y = 140)

        self.lastlbl_sefaresh = Label(sefareshkala , bg = '#EEEEEE', width = 12    , height = 1, font = ('Segoe UI' , 13, 'bold'), text = 'saxsaxsaxa' , fg = '#6D6D6D', justify = 'right')
        self.lastlbl_sefaresh.place(x = 105 , y = 140)

        self.codeMelilbl_sefaresh = Label(sefareshkala , bg = '#EEEEEE', width = 13, height = 1, font = ('Segoe UI' , 13, 'bold'), text = 'saxsaxsaxa' , fg = '#6D6D6D', justify = 'right')
        self.codeMelilbl_sefaresh.place(x = 389 , y = 183)

        self.genderlbl_sefaresh = Label(sefareshkala , bg = '#EEEEEE', width = 12, height = 1, font = ('Segoe UI' , 13, 'bold'), text = 'saxsaxsaxa' , fg = '#6D6D6D', justify = 'right')
        self.genderlbl_sefaresh.place(x = 105, y = 183)
#--------------------------------------------------------------------
        self.namKalalbl_sefaresh = Label(sefareshkala , bg = '#EEEEEE', width = 12, height = 1, font = ('Segoe UI' , 13, 'bold'), text = 'saxsaxsaxa' , fg = '#6D6D6D', justify = 'right')
        self.namKalalbl_sefaresh.place(x = 395, y = 267)

        self.groupKalalbl_sefaresh = Label(sefareshkala , bg = '#EEEEEE', width = 12, height = 1, font = ('Segoe UI' , 13, 'bold'), text = 'saxsaxsaxa' , fg = '#6D6D6D', justify = 'right')
        self.groupKalalbl_sefaresh.place(x = 110, y = 267)

        self.codeKalalbl_sefaresh = Label(sefareshkala , bg = '#EEEEEE', width = 12, height = 1, font = ('Segoe UI' , 13, 'bold'), text = '' , fg = '#6D6D6D', justify = 'right')
        self.codeKalalbl_sefaresh.place(x = 395, y = 310)

        self.mojodilbl_sefaresh = Label(sefareshkala , bg = '#EEEEEE', width = 12, height = 1, font = ('Segoe UI' , 13, 'bold'), text = 'saxsaxsaxa' , fg = '#6D6D6D', justify = 'right')
        self.mojodilbl_sefaresh.place(x = 110, y = 310)

        self.noeKalalbl_sefaresh = Label(sefareshkala , bg = '#EEEEEE', width = 12, height = 1, font = ('Segoe UI' , 13, 'bold'), text = 'saxsaxsaxa' , fg = '#6D6D6D', justify = 'right')
        self.noeKalalbl_sefaresh.place(x = 395, y = 351)

        self.noqtelbl_sefaresh = Label(sefareshkala , bg = '#EEEEEE', width = 12, height = 1, font = ('Segoe UI' , 13, 'bold'), text = 'saxsaxsaxa' , fg = '#6D6D6D', justify = 'right')
        self.noqtelbl_sefaresh.place(x = 110, y = 351)


        self.e_GetNum_sefaresh = Entry(sefareshkala, width = 20 , font = ('B Nazanin' , 10), bg = 'white', border = 0 , justify ='right')
        self.e_GetNum_sefaresh.place( x = 400, y = 396)

        self.e_GetDate_sefaresh = DateEntry(sefareshkala, width = 17 , font = ('B Nazanin' , 11), bg = 'white', border = 0 ,background='#495057',sforeground='#DEE2E6', justify ='right')
        self.e_GetDate_sefaresh.place( x = 130, y = 395)

        self.show_tree_sefaresh = ttk.Treeview(sefareshkala ,  style="Mystyle.Treeview", height = 6)
        self.show_tree_sefaresh.place(x = 145 , y = 450)

        self.show_tree_sefaresh['columns'] = ('date','number','category','id','Type','Name','row')

        self.show_tree_sefaresh.column('#0', width = 0  ,stretch = NO)
        self.show_tree_sefaresh.column('row', width = 60 , anchor = CENTER , minwidth = 60 )
        self.show_tree_sefaresh.column('id', width = 100 , anchor = CENTER , minwidth = 100 )
        self.show_tree_sefaresh.column('Name', width = 150 , anchor = CENTER , minwidth = 150 )
        self.show_tree_sefaresh.column('category' ,width = 150 , anchor = CENTER , minwidth = 150 )
        self.show_tree_sefaresh.column('date' ,width = 156 , anchor = CENTER, minwidth = 156 )
        self.show_tree_sefaresh.column('Type' ,width = 150 , anchor = CENTER, minwidth = 150  )
        self.show_tree_sefaresh.column('number' ,width = 150 , anchor = CENTER, minwidth = 150  )

        self.show_tree_sefaresh.heading('#0', text = ' ' , anchor = CENTER)
        self.show_tree_sefaresh.heading('row', text = 'ردیف' , anchor = CENTER )
        self.show_tree_sefaresh.heading('id', text = 'کد کالا' , anchor = CENTER )
        self.show_tree_sefaresh.heading('Name', text = 'نام کالا' , anchor = CENTER )
        self.show_tree_sefaresh.heading('category', text = 'گروه کالا' , anchor = CENTER)
        self.show_tree_sefaresh.heading('date', text = 'تاریخ' , anchor = CENTER)
        self.show_tree_sefaresh.heading('Type'   , text = ' نوع کالا' , anchor = CENTER )
        self.show_tree_sefaresh.heading('number' , text = 'تعداد', anchor = CENTER  )
        style.theme_use("clam")
        style.configure("Mystyle.Treeview.Heading",
                        background = '#A0A0A0',
                        font=('Segoe UI', 15,'bold'), 
                        relief = 'flat', bd=1
                        ) 
        style.map("Mystyle.Treeview.Heading",
            background=[('active','#A0A0A0')])
        
        style.configure("Mystyle.Treeview", highlightthickness=0, 
                                bd=0, font=('Segoe UI', 11),
                                background="#F8F8F8",
                                foreground="black",
                                rowheight = 25,
                                fieldbackground="#F8F8F8",   
                                )
        style.map("Mystyle.Treeview",
            background=[('selected', '#727272')])
        self.show_tree_sefaresh.bind('<Button-1>', self.test)
        self.show_tree_sefaresh.bind('<ButtonRelease-1>', self.test)

        self.sefaresh_btn = Button(sefareshkala , bg = 'white' , width = 147 , height = 40 , image = img30 ,activebackground= '#ffffff', borderwidth = 0, command=self.AddSefaresh_to_sql )#
        self.sefaresh_btn.place(x = 527 , y = 650) 
        self.sefaresh_btn.bind('<Enter>',lambda event : self.hoverBtn(img30,'pics/sefaresh-btn-hover.png'))
        self.sefaresh_btn.bind('<Leave>',lambda event : self.hoverBtn(img30,'pics/sefaresh-btn.png'))

        self.mainPage_btn = Button(sefareshkala , bg = 'white' , width = 147 , height = 40 , image = img14 ,activebackground= '#ffffff', borderwidth = 0 , command = self.BackMenu)
        self.mainPage_btn.place(x = 709 , y = 650) 
        self.mainPage_btn.bind('<Enter>',lambda event : self.hoverBtn(img14,'pics/main-btn-hover.png'))
        self.mainPage_btn.bind('<Leave>',lambda event : self.hoverBtn(img14,'pics/main-btn.png'))

        self.sabtKhoroj_btn = Button(sefareshkala , bg = 'white' , width = 147 , height = 40 , image = img32 ,activebackground= '#ffffff', borderwidth = 0 , command = self.SabtKhoroj)
        self.sabtKhoroj_btn.place(x = 354 , y = 650) 
        self.sabtKhoroj_btn.bind('<Enter>',lambda event : self.hoverBtn(img32,'pics/khoroj-btn-hover.png'))
        self.sabtKhoroj_btn.bind('<Leave>',lambda event : self.hoverBtn(img32,'pics/khoroj-btn.png'))

     
    def SabtKhoroj(self):
        self.selected = self.show_tree_sefaresh.focus()
        self.values = self.show_tree_sefaresh.item(self.selected , "values")
        self.statusChanged = 'آماده تحویل'
        delete_one = self.show_tree_sefaresh.selection()[0]
        self.show_tree_sefaresh.delete(delete_one)
        con = sql.connect('mydb.db')
        cur = con.cursor()
        cur.execute('''UPDATE DarKhastKharid SET status = '{}' WHERE code ='{}' '''.format(self.statusChanged, self.values[3]))
        con.commit()
        con.close()

        for item in self.show_tree_sefaresh.get_children():
            self.show_tree_sefaresh.delete(item)

        self.lst =[] 
        self.data_to_Sefaresh()

        self.e_nam_kala.delete(0, END)
        self.e_code_kala.delete(0, END)
        self.e_tozihat.delete(0, END)
        self.e_noqte.delete(0, END)
        self.e_noe_kala.set('انتخاب کنید')
        self.e_group_kala.set('انتخاب کنید')
        messagebox.showinfo('خروج از انبار', '!آیتم شما با موفقیت از انبار خارج شد')
    def show_info_Karmand_sefaresh(self,event = None):
        codeMeliGetSefaresh = self.e_search_codeMeli_sefaresh.get()
        con = sql.connect('mydb.db')
        cur = con.cursor()
        data = cur.execute('SELECT * FROM SabtKarmand WHERE codeMeli="{}"'.format(codeMeliGetSefaresh))
        data = list(data)
        print(data)
        self.namlbl_sefaresh['text']= data[0][0]
        self.lastlbl_sefaresh['text']= data[0][1]
        self.codeMelilbl_sefaresh['text']= data[0][2]
        self.genderlbl_sefaresh['text']= data[0][3]

    def show_info_KalaSefaresh(self,event = None):
        GetCodeKalaSefaresh = self.e_search_codeKala_sefaresh.get()
        con = sql.connect('mydb.db')
        cur = con.cursor()
        data = cur.execute('SELECT * FROM Kala WHERE code="{}"'.format(GetCodeKalaSefaresh))
        data = list(data)
        print(data)
        self.namKalalbl_sefaresh['text']= data[0][0]
        self.codeKalalbl_sefaresh['text']= data[0][2]
        self.groupKalalbl_sefaresh['text']= data[0][3]
        self.noeKalalbl_sefaresh['text']= data[0][1]
        self.noqtelbl_sefaresh['text'] = data[0][5]
        self.mojodilbl_sefaresh['text'] = data[0][7]
        self.CodeSefareshGet = data[0][8]
    def AddSefaresh_to_sql(self):
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.command='''CREATE TABLE IF NOT EXISTS DarKhastKharid ( namKala TEXT,
                                                                    type TEXT ,
                                                                    code TEXT ,
                                                                    goro TEXT,
                                                                    noqte TEXT,
                                                                    number TEXT,
                                                                    namKarbar TEXT,
                                                                    codeMeli TEXT,
                                                                    lastName TEXT,
                                                                    gender TEXT,
                                                                    status TEXT,
                                                                    date TEXT, 
                                                                    CodeSefaresh TEXT)'''
        self.cur.execute(self.command)
        self.status = 'درحال بررسی'
        self.data = (self.namKalalbl_sefaresh['text'],
                    self.noeKalalbl_sefaresh['text'],
                    self.codeKalalbl_sefaresh['text'],
                    self.groupKalalbl_sefaresh['text'],
                    self.noqtelbl_sefaresh['text'] ,
                    self.e_GetNum_sefaresh.get(),  
                    self.namlbl_sefaresh['text'],
                    self.codeMelilbl_sefaresh['text'],
                    self.lastlbl_sefaresh['text'],
                    self.genderlbl_sefaresh['text'],
                    self.status,
                    self.e_GetDate_sefaresh.get(),
                    self.CodeSefareshGet)
        
        self.cur.execute('''INSERT INTO DarKhastKharid (namKala,type,code,goro,noqte,number,namKarbar,codeMeli,lastName,gender,status,date,CodeSefaresh) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)''',self.data)
        self.con.commit()
        self.numlist_product_sefaresh=len(self.show_tree_sefaresh.get_children())
        self.show_tree_sefaresh.insert(parent = '',
                                        index = 'end',
                                        text = 'parent',
                                        values = (self.e_GetDate_sefaresh.get(),
                                        self.e_GetNum_sefaresh.get(),
                                        self.groupKalalbl_sefaresh['text'],
                                        self.codeKalalbl_sefaresh['text'],
                                        self.noeKalalbl_sefaresh['text'],
                                        self.namKalalbl_sefaresh['text'],
                                        self.numlist_product_sefaresh+1))
        self.namKalalbl_sefaresh['text']= ''
        self.noeKalalbl_sefaresh['text']= ''
        self.codeKalalbl_sefaresh['text']= ''
        self.groupKalalbl_sefaresh['text']= ''
        self.noqtelbl_sefaresh['text']= ''
        self.namlbl_sefaresh['text']= ''
        self.codeMelilbl_sefaresh['text']= ''
        self.genderlbl['text']= ''
        self.e_GetNum_sefaresh.delete(0 , END)
        self.e_GetDate_sefaresh.delete(0 , END)
        self.e_search_codeMeli_sefaresh.delete(0, END)
        self.e_search_codeKala_sefaresh.delete(0, END)
        self.lastlbl_sefaresh['text'] = ''
        self.genderlbl_sefaresh['text'] = ''
        self.mojodilbl_sefaresh['text'] = ''
    def data_to_Sefaresh(self):
        self.status = 'درحال بررسی'
        self.count1 = 1
        self.con = sql.connect('mydb.db')
        self.cur = self.con.cursor()
        row = self.cur.execute('''SELECT * FROM DarKhastKharid WHERE status = "{}" '''.format(self.status))
        for i in row :
            self.lst_sefaresh.append(i)
        for i in self.lst_sefaresh:
            self.show_tree_sefaresh.insert(parent='',index='end',text='',
                                                                    values=(i[11],
                                                                            i[5],
                                                                            i[3],
                                                                            i[2],
                                                                            i[1],
                                                                            i[0],
                                                                            str(self.count1)))
            self.lst_sefaresh = []
            self.count1 += 1



    def exportProductPage(self):
        sabtKhoroj.title('ثبت خروج کالا')
        sabtKhoroj.state('withdraw')
        sabtKhoroj.geometry('1200x720+150+20')
        sabtKhoroj.configure(bg = 'white')
        self.exportkala_lbl = Label(sabtKhoroj , bg = 'white' , width = 1150 , height = 676 , image = img33)
        self.exportkala_lbl.place(x = 25 , y = 25)


        self.show_tree_export = ttk.Treeview(sabtKhoroj ,  style="Mystyle.Treeview", height = 19)
        self.show_tree_export.place(x = 145 , y = 100)

        self.show_tree_export['columns'] = ('date','number','category','id','Type','Name','row')

        self.show_tree_export.column('#0', width = 0  ,stretch = NO)
        self.show_tree_export.column('row', width = 60 , anchor = CENTER , minwidth = 60 )
        self.show_tree_export.column('id', width = 100 , anchor = CENTER , minwidth = 100 )
        self.show_tree_export.column('Name', width = 150 , anchor = CENTER , minwidth = 150 )
        self.show_tree_export.column('category' ,width = 150 , anchor = CENTER , minwidth = 150 )
        self.show_tree_export.column('date' ,width = 156 , anchor = CENTER, minwidth = 156 )
        self.show_tree_export.column('Type' ,width = 150 , anchor = CENTER, minwidth = 150  )
        self.show_tree_export.column('number' ,width = 150 , anchor = CENTER, minwidth = 150  )

        self.show_tree_export.heading('#0', text = ' ' , anchor = CENTER)
        self.show_tree_export.heading('row', text = 'ردیف' , anchor = CENTER )
        self.show_tree_export.heading('id', text = 'کد کالا' , anchor = CENTER )
        self.show_tree_export.heading('Name', text = 'نام کالا' , anchor = CENTER )
        self.show_tree_export.heading('category', text = 'گروه کالا' , anchor = CENTER)
        self.show_tree_export.heading('date', text = 'تاریخ' , anchor = CENTER)
        self.show_tree_export.heading('Type'   , text = ' نوع کالا' , anchor = CENTER )
        self.show_tree_export.heading('number' , text = 'تعداد', anchor = CENTER  )
        style.theme_use("clam")
        style.configure("Mystyle.Treeview.Heading",
                        background = '#A0A0A0',
                        font=('Segoe UI', 15,'bold'), 
                        relief = 'flat', bd=1
                        ) 
        style.map("Mystyle.Treeview.Heading",
            background=[('active','#A0A0A0')])
        
        style.configure("Mystyle.Treeview", highlightthickness=0, 
                                bd=0, font=('Segoe UI', 11),
                                background="#F8F8F8",
                                foreground="black",
                                rowheight = 25,
                                fieldbackground="#F8F8F8",   
                                )
        style.map("Mystyle.Treeview",
            background=[('selected', '#727272')])
        self.show_tree_export.bind('<Button-1>', self.test)
        self.show_tree_export.bind('<ButtonRelease-1>', self.test)

        self.export_btn = Button(sabtKhoroj , bg = 'white' , width = 147 , height = 40 , image = img34 ,activebackground= '#ffffff', borderwidth = 0 , command = self.export_product)#
        self.export_btn.place(x = 445, y = 650) 
        self.export_btn.bind('<Enter>',lambda event : self.hoverBtn(img34,'pics/export-btn-hover.png'))
        self.export_btn.bind('<Leave>',lambda event : self.hoverBtn(img34,'pics/export-btn.png'))

        self.mainPage_btn = Button(sabtKhoroj , bg = 'white' , width = 147 , height = 40 , image = img14 ,activebackground= '#ffffff', borderwidth = 0 , command = self.BackMenu)
        self.mainPage_btn.place(x = 607 , y = 650) 
        self.mainPage_btn.bind('<Enter>',lambda event : self.hoverBtn(img14,'pics/main-btn-hover.png'))
        self.mainPage_btn.bind('<Leave>',lambda event : self.hoverBtn(img14,'pics/main-btn.png'))
    def data_to_list_export(self):
        self.lst_export = []
        for i in self.show_tree_export.get_children():
            self.show_tree_export.delete(i)
        self.status_ex = 'آماده تحویل'
        self.count1 = 1
        self.con = sql.connect('mydb.db')
        self.cur = self.con.cursor()
        row = self.cur.execute('''SELECT * FROM DarKhastKharid WHERE status = "{}" '''.format(self.status_ex))
        for i in row :
            self.lst_export.append(i)
        for i in self.lst_export:
            self.show_tree_export.insert(parent='',index='end',text='',
                                                                    values=(i[11],
                                                                            i[5],
                                                                            i[3],
                                                                            i[2],
                                                                            i[1],
                                                                            i[0],
                                                                            str(self.count1)))
            self.lst_export = []
            self.count1 += 1
    def export_product(self):
        self.selected = self.show_tree_export.focus()
        self.values = self.show_tree_export.item(self.selected , "values")

        self.con = sql.connect('mydb.db')
        self.cur = self.con.cursor()
        mojodiKala = self.cur.execute('''SELECT mojodi FROM Kala WHERE code = '{}' '''.format(self.values[3])) 
        mojodiKala = list(mojodiKala)
        print(mojodiKala)
        tedadDarkhast = self.cur.execute('''SELECT number FROM DarKhastKharid WHERE code = '{}' '''.format(self.values[3]))
        tedadDarkhast = list(tedadDarkhast)
        print(tedadDarkhast)
        self.mojodiKalaAsli = int(mojodiKala[0][0]) - int(tedadDarkhast[0][0])
        print(self.mojodiKalaAsli)
        mojodiKala = self.cur.execute('''UPDATE Kala SET mojodi = '{}' WHERE code = '{}' '''.format(self.mojodiKalaAsli,self.values[3])) 
        delete_one = self.show_tree_export.selection()[0]
        self.status_changed = 'خارج شده'
        self.show_tree_export.delete(delete_one)
        self.cur.execute('''UPDATE DarKhastKharid SET status = '{}' WHERE code = '{}' '''.format(self.status_changed,self.values[3]))
        self.con.commit()
        
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        detail = self.cur.execute('SELECT * FROM DarKhastKharid WHERE code="{}"'.format(self.values[3]))
        detail = list(detail)
        print(detail)

        self.statusVorodi = 'کالا خارج شده'
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        mojodi = self.cur.execute('SELECT mojodi FROM Kala WHERE code="{}"'.format(self.values[3]))
        mojodi = list(mojodi)
        print(mojodi)
        command='''CREATE TABLE IF NOT EXISTS History (     namKala TEXT,
                                                            typeKala TEXT ,
                                                            codeKala TEXT ,
                                                            goroKala TEXT,
                                                            number TEXT,
                                                            CodeSefaresh TEXT,
                                                            dateSefaresh TEXT,
                                                            namKarbar TEXT,
                                                            lastKarbar TEXT,
                                                            codeMeliKarbar TEXT,
                                                            Gender TEXT,
                                                            status TEXT,
                                                            mojodi TEXT)'''
        self.cur.execute(command)
        data = (detail[0][0],detail[0][1],detail[0][2],detail[0][3],detail[0][5],detail[0][12], detail[0][11], detail[0][6],detail[0][8],detail[0][7],detail[0][9], self.statusVorodi, mojodi[0][0])
        self.cur.execute('''INSERT INTO History (namKala,typeKala,codeKala,goroKala,number,CodeSefaresh,dateSefaresh, namKarbar,lastKarbar , codeMeliKarbar , Gender, status , mojodi) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)''',data)
        self.con.commit()
        self.con.close()

        # tedadDarkhast1 = int(tedadDarkhast)
#------------------------historyPage-------------------------------------

    def historyPage(self):
        history.title('ثبت خروج کالا')
        history.state('withdraw')
        history.geometry('1200x720+150+20')
        history.configure(bg = 'white')
        self.history_lbl = Label(history , bg = 'white' , width = 1150 , height = 676 , image = img36)
        self.history_lbl.place(x = 25 , y =25)

        self.openBill = Button(history, width = 157 , bg = 'white', height  = 40 , image = img39 , activebackground= '#ffffff', borderwidth = 0 , command = self.openQabzPage)
        self.openBill.place(x = 353 , y = 640)
        self.openBill.bind('<Enter>',lambda event : self.hoverBtn(img39,'pics/qabz-btn-hover.png'))
        self.openBill.bind('<Leave>',lambda event : self.hoverBtn(img39,'pics/qabz-btn.png'))

        self.openChart = Button(history, width = 157 , bg = 'white', height  = 40 , image = img40 , activebackground= '#ffffff', borderwidth = 0 , command = self.matplotPage)
        self.openChart.place(x = 526 , y = 640)
        self.openChart.bind('<Enter>',lambda event : self.hoverBtn(img40,'pics/chart-btn-hover.png'))
        self.openChart.bind('<Leave>',lambda event : self.hoverBtn(img40,'pics/chart-btn.png'))


        self.Menu_historyPage = Button(history, bg = 'white' , width = 147 , height = 40 , image = img14 ,activebackground= '#ffffff', borderwidth = 0 , command = self.BackMenu)
        self.Menu_historyPage.place(x = 699 , y = 640)
        self.Menu_historyPage.bind('<Enter>',lambda event : self.hoverBtn(img14,'pics/main-btn-hover.png'))
        self.Menu_historyPage.bind('<Leave>',lambda event : self.hoverBtn(img14,'pics/main-btn.png'))

        self.show_tree_history = ttk.Treeview(history ,  style="MystyleHistory.Treeview", height = 19)
        self.show_tree_history.place(x = 39, y = 100)

        self.show_tree_history['columns'] = ('date','status','noqte','number','codeMeli','lastName','nameKarbar','category','Type','Name','id','codeSefaresh','row')

        self.show_tree_history.column('#0', width = 0  ,stretch = NO)
        self.show_tree_history.column('row', width = 60 , anchor = CENTER , minwidth = 60 )
        self.show_tree_history.column('id', width = 65 , anchor = CENTER , minwidth = 65 )
        self.show_tree_history.column('Name', width = 100 , anchor = CENTER , minwidth = 100 )
        self.show_tree_history.column('category' ,width = 100 , anchor = CENTER , minwidth = 100 )
        self.show_tree_history.column('date' ,width = 65 , anchor = CENTER, minwidth = 65 )
        self.show_tree_history.column('Type' ,width = 75 , anchor = CENTER, minwidth = 75  )
        self.show_tree_history.column('number' ,width = 65 , anchor = CENTER, minwidth = 65  )
        self.show_tree_history.column('status' ,width = 100 , anchor = CENTER, minwidth = 100  )
        self.show_tree_history.column('noqte' ,width = 100 , anchor = CENTER, minwidth = 100  )
        self.show_tree_history.column('codeMeli' ,width = 100 , anchor = CENTER, minwidth = 100  )
        self.show_tree_history.column('nameKarbar' ,width = 70 , anchor = CENTER, minwidth = 70  )
        self.show_tree_history.column('codeSefaresh' ,width = 100 , anchor = CENTER, minwidth = 100  )
        self.show_tree_history.column('lastName' ,width = 122 , anchor = CENTER, minwidth = 122  )

        self.show_tree_history.heading('#0', text = ' ' , anchor = CENTER)
        self.show_tree_history.heading('row', text = 'ردیف' , anchor = CENTER )
        self.show_tree_history.heading('id', text = 'کد کالا' , anchor = CENTER )
        self.show_tree_history.heading('Name', text = 'نام کالا' , anchor = CENTER )
        self.show_tree_history.heading('category', text = 'گروه کالا' , anchor = CENTER)
        self.show_tree_history.heading('date', text = 'تاریخ' , anchor = CENTER)
        self.show_tree_history.heading('Type'   , text = ' نوع کالا' , anchor = CENTER )
        self.show_tree_history.heading('number' , text = 'تعداد', anchor = CENTER  )
        self.show_tree_history.heading('status' , text = 'وضعیت', anchor = CENTER  )
        self.show_tree_history.heading('noqte' , text = 'نقطه خرید', anchor = CENTER  )
        self.show_tree_history.heading('codeMeli' , text = 'کد ملی', anchor = CENTER  )
        self.show_tree_history.heading('nameKarbar' , text = 'نام', anchor = CENTER  )
        self.show_tree_history.heading('lastName' , text = 'نام خانوادگی', anchor = CENTER  )
        self.show_tree_history.heading('codeSefaresh' , text = 'کد سفارش', anchor = CENTER  )
        style.theme_use("clam")
        style.configure("MystyleHistory.Treeview.Heading",
                        background = '#A0A0A0',
                        font=('Segoe UI', 14,'bold'), 
                        relief = 'flat', bd=1
                        ) 
        style.map("MystyleHistory.Treeview.Heading",
            background=[('active','#A0A0A0')])
        
        style.configure("MystyleHistory.Treeview", highlightthickness=0, 
                                bd=0, font=('Segoe UI', 11),
                                background="#F8F8F8",
                                foreground="black",
                                rowheight = 25,
                                fieldbackground="#F8F8F8",   
                                )
        style.map("MystyleHistory.Treeview",
            background=[('selected', '#727272')])
        self.show_tree_history.bind('<Button-1>', self.selectItemForMatplotlib)
        self.show_tree_history.bind('<ButtonRelease-1>', self.selectItemForMatplotlib)

    def data_to_list_history(self):
        self.lst_history = []
        for i in self.show_tree_history.get_children():
            self.show_tree_history.delete(i)
        self.count3 = 1
        self.con = sql.connect('mydb.db')
        self.cur = self.con.cursor()
        row = self.cur.execute('''SELECT * FROM DarKhastKharid ''')
        self.lst_history = []
        for i in row :
            self.lst_history.append(i)
        for i in self.lst_history:
            self.show_tree_history.insert(parent='',index='end',text='',
                                                                    values=(i[11],
                                                                            i[10],
                                                                            i[4],
                                                                            i[5],
                                                                            i[7],
                                                                            i[8],
                                                                            i[6],
                                                                            i[3],
                                                                            i[1],
                                                                            i[0],
                                                                            i[2],
                                                                            i[12],
                                                                            str(self.count3)))
            self.lst_history = []
            self.count3 += 1


    # def getCodeKala(self):
    #     self.selected = self.show_tree_history.focus()
    #     self.values = self.show_tree_history.item(self.selected, "values")
            
    #----------------------historyPage-------------------------------------
   
    #----------------------historyPage-------------------------------------
    def qabzPage(self):
        Qabz.title('صدور قبض')
        Qabz.state('withdraw')
        Qabz.geometry('1200x720+300+150')
        Qabz.configure(bg = 'white')
        self.Qabz_lbl = Label(Qabz , bg = 'white' , width = 1150 , height = 676 , image = img37)
        self.Qabz_lbl.place(x = 25 , y = 25)

        self.namKalaQabz = Label(Qabz , bg = 'white', width = 16, height = 1, font = ('Segoe UI' , 13, 'bold'), text = '' , fg = '#6D6D6D', justify = 'right')
        self.namKalaQabz.place(x = 800, y = 202)

        self.codeKalaQabz = Label(Qabz , bg = 'white', width = 16, height = 1, font = ('Segoe UI' , 13, 'bold'), text = '' , fg = '#6D6D6D', justify = 'right')
        self.codeKalaQabz.place(x =  800, y = 266)

        self.codeSefareshQabz = Label(Qabz , bg = 'white', width = 16, height = 1, font = ('Segoe UI' , 13, 'bold'), text = '' , fg = '#6D6D6D', justify = 'right')
        self.codeSefareshQabz.place(x =  800, y = 335)

        self.statusQabz = Label(Qabz , bg = 'white', width = 16, height = 1, font = ('Segoe UI' , 13, 'bold'), text = '' , fg = '#6D6D6D', justify = 'right')
        self.statusQabz.place(x =  800, y = 400)

        self.namKarbarQabz = Label(Qabz , bg = 'white', width = 16, height = 1, font = ('Segoe UI' , 13, 'bold'), text = '' , fg = '#6D6D6D', justify = 'right')
        self.namKarbarQabz.place(x = 200, y = 202)

        self.codeMeliQabz = Label(Qabz , bg = 'white', width = 16, height = 1, font = ('Segoe UI' , 13, 'bold'), text = '' , fg = '#6D6D6D', justify = 'right')
        self.codeMeliQabz.place(x = 200, y = 266)

        self.numberQabz = Label(Qabz , bg = 'white', width = 16, height = 1, font = ('Segoe UI' , 13, 'bold'), text = '' , fg = '#6D6D6D', justify = 'right')
        self.numberQabz.place(x = 200, y = 335)

        self.DateQabz = Label(Qabz , bg = 'white', width = 16, height = 1, font = ('Segoe UI' , 13, 'bold'), text = '' , fg = '#6D6D6D', justify = 'right')
        self.DateQabz.place(x = 200, y = 400)

        self.Menu_QabzPage = Button(Qabz, bg = 'white' , width = 147 , height = 40 , image = img14 ,activebackground= '#ffffff', borderwidth = 0 , command = self.BackMenu)
        self.Menu_QabzPage.place(x = 527 , y = 640)

    def openQabzPage(self):
        Qabz.state('normal')
        Qabz.geometry('1200x720+150+20')
        history.state('withdraw')
        self.selected = self.show_tree_history.focus()
        self.values = self.show_tree_history.item(self.selected , "values")
        con = sql.connect('mydb.db')
        cur = con.cursor()
        data = cur.execute('SELECT * FROM DarKhastKharid WHERE CodeSefaresh="{}"'.format(self.values[11]))
        data = list(data)
        print(data)







        self.namKalaQabz['text']= data[0][0]
        self.codeKalaQabz['text']= data[0][2]
        self.codeSefareshQabz['text']= data[0][12]
        self.namKarbarQabz['text']= data[0][6]
        self.codeMeliQabz['text'] = data[0][7]
        self.numberQabz['text'] = data[0][5]
        self.statusQabz['text'] = data[0][10]
        self.DateQabz['text'] = data[0][11]        
    #----------------------matplotlibPage-------------------------------------
    def selectItemForMatplotlib(self, event = None):
        self.selected = self.show_tree_history.focus()
        self.values = self.show_tree_history.item(self.selected , "values")
    def matplotPage(self,event=None):
        self.ChartY=[]
        self.ChartX=[]
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        row1 = self.cur.execute('SELECT dateSefaresh FROM History WHERE codeKala = "{}"'.format(self.values[10]))
        row1 =list(row1)
        row2 = self.cur.execute('SELECT mojodi FROM History  WHERE codeKala = "{}" ORDER BY number'.format(self.values[10]))
        row2 =list(row2)
        # row2.sort()
        print(row2)
        # print(row)
        for i in row1:
                self.ChartY.append(i[0])
        for i in row2 :
                self.ChartX.append(i[0])
        fig = plt.figure(figsize  = (6,6))
        plt.plot(self.ChartY,self.ChartX , color = 'b' ,
            linewidth = 1 , 
            linestyle = '--' , 
            marker = 'o',
            markersize = 8 , 
            markerfacecolor = 'lightblue',
            markeredgecolor = 'brown',
            markeredgewidth = 1
        )
        plt.grid(which = 'both' ,color = 'grey' ,linestyle = '-.' ,linewidth = 0.5)
        plt.show()
        self.frm  = LabelFrame(self , text = 'Plot' , padx = 5 , pady = 10)
        self.frm.place(x = 50 , y = 0)
        bar = FigureCanvasTkAgg(fig,self.frm)
        bar.get_tk_widget().pack(side = LEFT , fill = BOTH)

#--------------------------------------------------------------------
    def show_info_Karmand(self,event = None):
        codeMeliGet = self.e_search_codeMeli.get()
        con = sql.connect('mydb.db')
        cur = con.cursor()
        data = cur.execute('SELECT * FROM SabtKarmand WHERE codeMeli="{}"'.format(codeMeliGet))
        data = list(data)
        print(data)
        self.namlbl['text']= data[0][0]
        self.lastNamelbl['text']= data[0][1]
        self.codeMelilbl['text']= data[0][2]
        self.genderlbl['text']= data[0][3]
        
    def show_info_Kala(self,event = None):
        GetCodeKala = self.e_search_codeKala.get()
        con = sql.connect('mydb.db')
        cur = con.cursor()
        data = cur.execute('SELECT * FROM Kala WHERE code="{}"'.format(GetCodeKala))
        data = list(data)
        print(data)
        self.namKalalbl['text']= data[0][0]
        self.codeKalalbl['text']=data[0][2]
        self.groupKalalbl['text']=data[0][3]
        self.NoeKalalbl['text']=data[0][1]
        self.noqte = data[0][5]
        
        con = sql.connect('mydb.db')
        cur = con.cursor()
        cur.execute("SELECT photo FROM Kala WHERE code = '{}'".format(GetCodeKala))
        self.image_data = cur.fetchone()[0]
        self.product_img = Image.open(io.BytesIO(self.image_data))
        self.product_photo = ImageTk.PhotoImage(self.product_img)
        self.show_img_Vorodi = Label(sabtvorod , image=self.product_photo, width = 100 , height= 95)
        self.show_img_Vorodi.place(x = 177, y = 199 )

    def update_record_number(self):
        GetCodeKala = self.e_search_codeKala.get()
        GetNumKala = self.e_Get_num.get()
        GetCodeSefaresh = self.e_Get_codeSefaresh.get()
        GetDateSefaresh = self.e_GetDate_sabtvorod.get()
        self.con = sql.connect('mydb.db')
        self.cur = self.con.cursor()
        update_mojodi = self.cur.execute('SELECT mojodi FROM Kala WHERE code ="{}"'.format(GetCodeKala))
        update_mojodi = list(update_mojodi)
        new_mojodi = int(update_mojodi[0][0]) + int(GetNumKala)

        command = ' UPDATE Kala SET mojodi = "{}", CodeSefaresh = "{}", dateSefaresh = "{}"   WHERE code="{}" '.format(new_mojodi,GetCodeSefaresh,GetDateSefaresh,GetCodeKala)
        self.cur.execute(command)
        self.con.commit()
        self.con.close()
        self.con = sql.connect('mydb.db')
        self.cur = self.con.cursor()
        row = self.cur.execute('''SELECT  * FROM Kala WHERE code = "{}"'''.format(GetCodeKala))
        for i in row :
            self.lst_vorodi.append(i)
        for i in self.lst_vorodi:
            self.show_tree_Vorodi.insert(parent='',index='end',text='',
                                                                    values=(i[9],
                                                                            i[5],
                                                                            i[7],
                                                                            i[3],
                                                                            i[2],
                                                                            i[1],
                                                                            i[0],
                                                                            i[8],
                                                                            str(self.count2+1)))
            self.lst_vorodi = []
            self.count2 += 1
        # con.commit()
        self.con.close()

        self.statusVorodi = 'کالا وارد شد'
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        mojodi = self.cur.execute('SELECT mojodi FROM Kala WHERE code="{}"'.format(GetCodeKala))
        mojodi = list(mojodi)
        print(mojodi)
        command='''CREATE TABLE IF NOT EXISTS History (     namKala TEXT,
                                                            typeKala TEXT ,
                                                            codeKala TEXT ,
                                                            goroKala TEXT,
                                                            number TEXT,
                                                            CodeSefaresh TEXT,
                                                            dateSefaresh TEXT,
                                                            namKarbar TEXT,
                                                            lastKarbar TEXT,
                                                            codeMeliKarbar TEXT,
                                                            Gender TEXT,
                                                            status TEXT,
                                                            mojodi TEXT)'''
        self.cur.execute(command)
        data = (self.namKalalbl['text'],self.NoeKalalbl['text'],self.codeKalalbl['text']
        ,self.groupKalalbl['text'],GetNumKala,GetCodeSefaresh, GetDateSefaresh, self.namlbl['text'],self.lastNamelbl['text'],self.codeMelilbl['text'],self.genderlbl['text'], self.statusVorodi, mojodi[0][0])
        self.cur.execute('''INSERT INTO History (namKala,typeKala,codeKala,goroKala,number,CodeSefaresh,dateSefaresh, namKarbar,lastKarbar , codeMeliKarbar , Gender, status , mojodi) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)''',data)
        self.con.commit()
        self.con.close()

        self.namKalalbl['text']= ''
        self.codeKalalbl['text']= ''
        self.groupKalalbl['text']= ''
        self.NoeKalalbl['text']= ''
        self.namlbl['text']= ''
        self.lastNamelbl['text']= ''
        self.codeMelilbl['text']= ''
        self.genderlbl['text']= ''
        self.e_Get_num.delete(0 , END)
        self.e_search_codeKala.delete(0, END)
        self.e_search_codeMeli.delete(0, END)
        self.e_Get_codeSefaresh.delete(0, END)
        self.e_GetDate_sabtvorod.delete(0, END)
#-------------------------add-product-Page-funcs--------------------

    def update_record(self):
        self.selected =  self.show_tree.focus()
        self.show_tree.item(self.selected ,values = (self.e_nam_kala.get(),
                                                        self.e_noe_kala.get(),
                                                        self.e_code_kala.get(),
                                                        self.e_group_kala.get(),
                                                        self.e_tozihat.get(),
                                                        self.e_noqte.get()))
        self.e_nam_kala.delete(0, END)
        self.e_noe_kala.delete(0, END)
        self.e_code_kala.delete(0, END)
        self.e_group_kala.delete(0, END)
        self.e_tozihat.delete(0, END)
        self.e_noqte.delete(0, END)

    def sql_search(self,id1):
        con = sql.connect('mydb.db')
        cur = con.cursor()
        row = cur.execute('SELECT * FROM kala WHERE code="{}"'.format(id1))
        return list(row)

    def show_info(self,event = None) :
        self.e_noe_kala.set("یک گزینه را انتخاب کنید")
        self.e_group_kala.set("یک گزینه را انتخاب کنید")
        self.e_code_kala.delete(0,END)
        self.e_nam_kala.delete(0,END)
        self.e_noqte.delete(0,END)
        self.e_tozihat.delete(0,END)
    
        self.selected = self.show_tree.focus()
        self.values = self.show_tree.item(self.selected , "values")

        con = sql.connect('mydb.db')
        cur = con.cursor()
        cur.execute("SELECT photo FROM Kala WHERE code = '{}'".format(self.values[2]))
        self.image_data = cur.fetchone()[0]
        self.product_img = Image.open(io.BytesIO(self.image_data))
        self.product_photo = ImageTk.PhotoImage(self.product_img)
        self.show_image = Label(productpage , image=self.product_photo, width = 100 , height= 95)
        self.show_image.place(x=125, y= 242)

        self.valuelst = self.sql_search(self.values[2])
        self.e_nam_kala.insert(0,self.valuelst[0][0])
        self.e_noe_kala.set(self.valuelst[0][1])
        self.e_code_kala.insert(0,self.valuelst[0][2])
        self.e_group_kala.set(self.valuelst[0][3])
        self.e_noqte.insert(0,self.valuelst[0][5])
        self.e_tozihat.insert(0,self.valuelst[0][4])
    def edit(self,event = None):
        self.nam_kala = self.e_nam_kala.get()
        self.noe_kala = self.e_noe_kala.get()
        self.code_kala = self.e_code_kala.get()
        self.group_kala = self.e_group_kala.get()
        self.tozihat = self.e_tozihat.get()
        self.noqteKharid = self.e_noqte.get()
        
        self.sql_update(self.values[2],self.nam_kala,self.noe_kala,self.code_kala,self.group_kala,self.tozihat,self.noqteKharid)

        self.show_tree.item(self.selected ,values = (self.noqteKharid,self.group_kala,self.code_kala,self.noe_kala,self.nam_kala,self.values[5]))
        messagebox.showinfo('ویرایش' , 'مشخصات با موفقیت ویرایش شدند')
    def sql_update(self,id1,name1,noe_kala1,code1,group1,tozih1,noqte1):
        con = sql.connect('mydb.db')
        cur = con.cursor()

        command = ' UPDATE kala SET code = "{}" , nam = "{}", type = "{}", goro = "{}", tozih = "{}",noqte = "{}" WHERE code="{}" '.format(code1,name1,noe_kala1,group1,tozih1,noqte1,id1)
        cur.execute(command)
        con.commit()

        self.e_nam_kala.delete(0, END)
        self.e_code_kala.delete(0, END)
        self.e_tozihat.delete(0, END)
        self.e_noqte.delete(0, END)
        self.e_noe_kala.set('انتخاب کنید')
        self.e_group_kala.set('انتخاب کنید')
        
    def Remove(self):
        delete_one = self.show_tree.selection()[0]
        self.show_tree.delete(delete_one)
        con = sql.connect('mydb.db')
        cur = con.cursor()
        cur.execute('''DELETE FROM Kala WHERE code ='''+ self.e_code_kala.get())
        con.commit()
        con.close()
        self.show_image['image'] = img17
        for item in self.show_tree.get_children():
            self.show_tree.delete(item)

        self.lst =[] 
        self.data_to_list()

        self.e_nam_kala.delete(0, END)
        self.e_code_kala.delete(0, END)
        self.e_tozihat.delete(0, END)
        self.e_noqte.delete(0, END)
        self.e_noe_kala.set('انتخاب کنید')
        self.e_group_kala.set('انتخاب کنید')
        self.show_image['image'] = img17
        messagebox.showinfo('حذف آیتم', '!آیتم شما با موفقیت حذف شد')

    def Remove_all (self) :
        for i in self.show_tree.get_children():
            self.show_tree.delete(i)
        con = sql.connect('mydb.db')
        cur = con.cursor()
        command = ''' DELETE FROM Kala '''
        cur.execute(command)    
        con.commit()
        messagebox.showinfo('حذف آیتم', '!تمامی آیتم های شما با موفقیت حذف شد')
        self.e_nam_kala.delete(0, END)
        self.e_code_kala.delete(0, END)
        self.e_tozihat.delete(0, END)
        self.e_noqte.delete(0, END)
        self.e_noe_kala.set('انتخاب کنید')
        self.e_group_kala.set('انتخاب کنید')

    def data_to_list(self,event = None):
        self.lst = []
        self.count = 0
        for item in self.show_tree.get_children():
            self.show_tree.delete(item)
            print(item)
        # self.e_nam_kala.delete(0,END)
        # self.e_code_kala.delete(0,END)
        # self.e_tozihat.delete(0,END)
        # self.e_noqte.delete(0,END)
        # self.e_search.delete(0,END)
        # self.e_noe_kala.set("یک گزینه را انتخاب کنید")
        # self.e_group_kala.set("یک گزینه را انتخاب کنید")
        self.con = sql.connect('mydb.db')
        self.cur = self.con.cursor()
        row = self.cur.execute('''SELECT  * FROM Kala''')
        for i in row :
            self.lst.append(i)
        for i in self.lst:
            self.show_tree.insert(parent='',index='end',text='',
                                 values=(i[5],i[3],i[2],i[1],i[0],str(self.count+1)))
            self.count += 1


    def AddKala_to_sql(self):
        self.nam_kala = self.e_nam_kala.get()
        self.noe_kala = self.e_noe_kala.get()
        self.code_kala = self.e_code_kala.get()
        self.group_kala = self.e_group_kala.get()
        self.tozihat = self.e_tozihat.get()
        self.noqteKharid = self.e_noqte.get()
        self.photo_read = self.convert_to_binary_data(self.img_name)
        self.numlist_product=len(self.show_tree.get_children())
        self.show_tree.insert(parent = '',
                             index = 'end',
                             text = 'parent',
                             values = (self.noqteKharid,
                                        self.group_kala,
                                        self.code_kala,
                                        self.noe_kala,
                                        self.nam_kala,
                                        self.numlist_product+1))
        self.e_nam_kala.delete(0, END)
        self.e_code_kala.delete(0, END)
        self.e_tozihat.delete(0, END)
        self.e_noqte.delete(0, END)
        self.e_noe_kala.set('انتخاب کنید')
        self.e_group_kala.set('انتخاب کنید')
        
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.command='''CREATE TABLE IF NOT EXISTS Kala (   nam TEXT,
                                                            type TEXT ,
                                                            code TEXT ,
                                                            goro TEXT,
                                                            tozih TEXT,
                                                            noqte TEXT,
                                                            photo BLOB,
                                                            mojodi TEXT,
                                                            CodeSefaresh TEXT,
                                                            dateSefaresh TEXT)'''
        self.cur.execute(self.command)
        self.data = (self.nam_kala,self.noe_kala,self.code_kala,self.group_kala,self.tozihat,self.noqteKharid, self.photo_read, 0, 0 , 0)
        self.cur.execute('''INSERT INTO Kala (nam,type,code,goro,tozih,noqte,photo,mojodi,CodeSefaresh,dateSefaresh) VALUES (?,?,?,?,?,?,?,?,?,?)''',self.data)
        self.con.commit()
        img17['file'] = 'pics/resid.png'
        self.e_nam_kala.focus()
        self.data_to_list()
        messagebox.showinfo('اضافه شد' , 'کالا به لیست انبار اضافه شد')

    def search(self,event = None):
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.search_get=self.e_search.get()
        self.count=0
        if self.search_get !='':
            for i in self.show_tree.get_children():
                self.show_tree.delete(i)
            self.row=self.cur.execute('SELECT * FROM kala WHERE code="{}"'.format(self.search_get))
            self.search_list=list(self.row)

            self.show_tree.insert(parent='',index='end',iid=self.count,text='',
                                values=(self.search_list[0][5],
                                        self.search_list[0][3],
                                        self.search_list[0][2],
                                        self.search_list[0][1],
                                        self.search_list[0][0],
                                        str(self.count+1)))
        else:
            self.lst=[]
            self.show_tree.delete('0')
            self.data_to_list()
            self.show_image['image'] = img17

#-------------------------employee-Page-funcs--------------------
    def Addemp_to_sql(self):
        self.nam = self.e_nam.get()
        self.family = self.e_family.get()
        self.code_meli = self.e_code_meli.get()
        self.jensiat = self.e_jensiat_combo.get()
        self.position = self.e_position_combo.get()
        self.photo_read_emp = self.convert_to_binary_data(self.img_name)

        self.numlist=len(self.show_tree_employee.get_children())
        
        self.show_tree_employee.insert(parent = '',
                             index = 'end',
                             text = 'parent',
                             values = (self.position,
                                        self.jensiat,
                                        self.code_meli,
                                        self.family,
                                        self.nam,
                                        self.numlist+1))
        self.e_nam.delete(0, END)
        self.e_family.delete(0, END)
        self.e_code_meli.delete(0, END)
        self.e_jensiat_combo.set('انتخاب کنید')
        self.e_position_combo.set('انتخاب کنید')
        
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.command='''CREATE TABLE IF NOT EXISTS SabtKarmand (nam TEXT,
                                                            family TEXT ,
                                                            codeMeli TEXT ,
                                                            jensiat TEXT,
                                                            position TEXT,
                                                            photo BLOB)'''
        self.cur.execute(self.command)
        self.data_emp = (self.nam,self.family,self.code_meli,self.jensiat,self.position,self.photo_read_emp)
        self.cur.execute('''INSERT INTO SabtKarmand (nam,family,codeMeli,jensiat,position,photo) VALUES (?,?,?,?,?,?)''',self.data_emp)
        self.con.commit()
        
        img17['file'] = 'pics/resid.png'
        self.e_nam.focus()




    def search_emp(self,event = None):
        self.con=sql.connect('mydb.db')
        self.cur=self.con.cursor()
        self.search_get_emp=self.e_search_employee.get()
        self.count_emp=0
        if self.search_get_emp != '':
            for i in self.show_tree_employee.get_children():
                self.show_tree_employee.delete(i)
            self.row=self.cur.execute('SELECT * FROM SabtKarmand WHERE codeMeli="{}"'.format(self.search_get_emp))
            self.search_list_emp=list(self.row)
            
            self.show_tree_employee.insert(parent='',index='end',iid=self.count_emp,text='',
                                values=(self.search_list_emp[0][4],
                                        self.search_list_emp[0][3],
                                        self.search_list_emp[0][2],
                                        self.search_list_emp[0][1],
                                        self.search_list_emp[0][0],
                                        str(self.count_emp+1)))
        else:
            self.lst_emp=[]
            self.show_tree_employee.delete('0')
            self.data_to_list_emp()
    def Remove_emp(self):
        delete_one = self.show_tree_employee.selection()[0]
        self.show_tree_employee.delete(delete_one)
        con = sql.connect('mydb.db')
        cur = con.cursor()
        cur.execute('''DELETE FROM SabtKarmand WHERE codeMeli ='''+ self.e_code_meli.get())
        con.commit()
        con.close()


        for item in self.show_tree_employee.get_children():
            self.show_tree_employee.delete(item)

        self.lst_emp =[]
        
        self.data_to_list_emp()

        self.e_nam.delete(0, END)
        self.e_family.delete(0, END)
        self.e_code_meli.delete(0, END)
        self.e_jensiat_combo.set('انتخاب کنید')
        self.e_position_combo.set('انتخاب کنید')
        self.show_image_employee['image'] = img17
        messagebox.showinfo('حذف آیتم', '!آیتم شما با موفقیت حذف شد')

    def Remove_all_emp(self):
        for i in self.show_tree_employee.get_children():
            self.show_tree_employee.delete(i)
        con = sql.connect('mydb.db')
        cur = con.cursor()
        command = ''' DELETE FROM SabtKarmand '''
        cur.execute(command)    
        con.commit()
        messagebox.showinfo('حذف آیتم', '!تمامی آیتم های شما با موفقیت حذف شد')
        self.e_nam.delete(0, END)
        self.e_family.delete(0, END)
        self.e_code_meli.delete(0, END)
        self.e_jensiat_combo.set('انتخاب کنید')
        self.e_position_combo.set('انتخاب کنید')
        self.show_image_employee['image'] = img17
        self.e_nam.focus()
    def edit_emp(self):
        self.nam = self.e_nam.get()
        self.family = self.e_family.get()
        self.code_meli = self.e_code_meli.get()
        self.jensiat = self.e_jensiat_combo.get()
        self.position = self.e_position_combo.get()
        
        self.sql_update_emp(self.values[2],self.nam,self.family,self.code_meli,self.jensiat,self.position)

        self.show_tree_employee.item(self.selected ,values = (self.position,self.jensiat,self.code_meli,self.family,self.nam,self.values[5]))
        messagebox.showinfo('ویرایش' , 'مشخصات با موفقیت ویرایش شدند')

    def sql_update_emp(self,id1,name1,family1,code1,jensiat1,position1):
        con = sql.connect('mydb.db')
        cur = con.cursor()
        command = ' UPDATE SabtKarmand SET codeMeli = "{}" , nam = "{}", family = "{}", jensiat = "{}", position = "{}" WHERE codeMeli ="{}" '.format(code1,name1,family1,jensiat1,position1,id1)
        cur.execute(command)
        con.commit()

    def show_info_emp(self,event = None) :
        self.e_nam.delete(0, END)
        self.e_family.delete(0, END)
        self.e_code_meli.delete(0, END)
        self.e_jensiat_combo.set('انتخاب کنید')
        self.e_position_combo.set('انتخاب کنید')
    
        self.selected = self.show_tree_employee.focus()
        self.values = self.show_tree_employee.item(self.selected , "values")
        # print(self.values[2])
        self.valuelst = self.sql_search_emp(self.values[2])
        self.e_nam.insert(0,self.valuelst[0][0])
        self.e_family.insert(0,self.valuelst[0][1])
        self.e_code_meli.insert(0,self.valuelst[0][2])
        self.e_jensiat_combo.set(self.valuelst[0][3])
        self.e_position_combo.set(self.valuelst[0][4])
        # self.show_image_employee['image'] = self.photo_read_emp
        con = sql.connect('mydb.db')
        cur = con.cursor()
        cur.execute("SELECT photo FROM SabtKarmand WHERE codeMeli = '{}'".format(self.values[2]))
        self.image_data = cur.fetchone()[0]
        self.product_img = Image.open(io.BytesIO(self.image_data))
        self.product_photo = ImageTk.PhotoImage(self.product_img)
        self.show_image_employee = Label(employeepage , image=self.product_photo, width = 100 , height= 95)
        self.show_image_employee.place(x=139, y= 146)


    def data_to_list_emp(self,event = None):
        self.count_emp = 1
        self.con = sql.connect('mydb.db')
        self.cur = self.con.cursor()
        row = self.cur.execute('''SELECT * FROM SabtKarmand''')
        for i in row :
            self.lst_emp.append(i)
        for i in self.lst_emp:
            self.show_tree_employee.insert(parent='',index='end',iid=self.count_emp,text='',
                                 values=(i[4],i[3],i[2],i[1],i[0],str(self.count_emp)))
            self.count_emp += 1
    
    def sql_search_emp(self,id1):
        con = sql.connect('mydb.db')
        cur = con.cursor()
        row = cur.execute('SELECT * FROM SabtKarmand WHERE codeMeli="{}"'.format(id1))
        return list(row)

    def hoverBtn(self,img,url):
        img['file'] = url

#------------------Global-funcs----------------------
    def select_image(self,event = None) :
        self.img_name = filedialog.askopenfilename()
        img17['file'] = self.img_name

    def convert_to_binary_data(self, filename):
        with open (filename , 'rb') as f:
            blobdata = f.read()
        return blobdata

#------------------nav-funcs----------------------
    def historyPagePopUp(self,event = None):
        if history.state != 'normal':
            root.state('withdraw')
            history.state('normal')
            self.data_to_list_history()
    def exportProductPopUp(self,event = None):
        if sabtKhoroj.state != 'normal':
            root.state('withdraw')
            sabtKhoroj.state('normal')
            self.data_to_list_export()
    def DarkhastKharid(self,event = None):
        if reqkalapage.state != ('normal') :
            root.state('withdraw')
            reqkalapage.state('normal')
            self.data_to_req_table()
    def sabtvorodKala(self,event = None):
        if sabtvorod.state != ('normal') :
            root.state('withdraw')
            sabtvorod.state('normal')
            self.update_record_number()
    def sabtKalaPage(self, event = None):
        if self.productpage.state != ('normal') :
            root.state('withdraw')
            self.productpage.state('normal')
            self.data_to_list()

    def sabtKarmandPage(self):
        if self.employeepage.state != ('normal') :
            root.state('withdraw')
            self.employeepage.state('normal')
            self.data_to_list_emp()

    def MojodiPage(self):
        if self.mojodipage.state != ('normal') :
            root.state('withdraw')
            self.mojodipage.state('normal')
            self.data_to_stock()

    def darKhastKhoroj(self,event = None):
        if sefareshkala.state != ('normal') :
            root.state('withdraw')
            sefareshkala.state('normal')
            self.data_to_Sefaresh()
    def BackMenu(self , event = None):
        if  root.state != 'normal':
            root.state('normal')
            productpage.state('withdraw')
            self.e_noe_kala.set("یک گزینه را انتخاب کنید")
            self.e_group_kala.set("یک گزینه را انتخاب کنید")
            self.e_code_kala.delete(0,END)
            self.e_nam_kala.delete(0,END)
            self.e_noqte.delete(0,END)
            self.e_tozihat.delete(0,END)
            self.show_image['image'] = img17
        if  root.state != 'normal':
            root.state('normal')
            mojodipage.state('withdraw')
        if root.state != 'normal':
            root.state('normal')
            employeepage.state('withdraw')
            self.e_nam.delete(0, END)
            self.e_family.delete(0, END)
            self.e_code_meli.delete(0, END)
            self.e_jensiat_combo.set('انتخاب کنید')
            self.e_position_combo.set('انتخاب کنید')
            self.show_image_employee['image'] = img17
        if root.state != 'normal':
            root.state('normal')
            sabtvorod.state('withdraw')
            self.e_search_codeMeli.delete(0, END)
            self.e_search_codeKala.delete(0, END)
            self.e_Get_num.delete(0, END)
            self.e_Get_codeSefaresh.delete(0, END)
            self.namlbl['text']=  ''
            self.lastNamelbl['text']=  ''
            self.codeMelilbl['text']=  ''
            self.genderlbl['text']=  ''
            self.namKalalbl['text']=  ''
            self.codeKalalbl['text']= ''
            self.groupKalalbl['text']= ''
            self.NoeKalalbl['text']= ''
            self.noqte =  ''
            self.show_img_Vorodi['image'] = img17
            self.e_search_codeMeli.focus()
        if root.state != 'normal':
            root.state('normal')
            reqkalapage.state('withdraw')
        if root.state != 'normal':
            root.state('normal')
            sefareshkala.state('withdraw')
        if root.state != 'normal':
            root.state('normal')
            sabtKhoroj.state('withdraw')
        if root.state != 'normal':
            root.state('normal')
            history.state('withdraw')
        if root.state != 'normal':
            root.state('normal')
            Qabz.state('withdraw')
    def hide(self, event = None):
        if self.password_ent['show'] == '*':
            self.password_ent['show'] = ''
            img15['file'] = 'pics/cheshm-baz.png'
        elif self.password_ent['show'] == '' :
            img15['file'] = 'pics/cheshm-baste.png'
            self.password_ent['show'] = '*'
app = app(root)
root.mainloop()
