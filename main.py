import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import tkinter.font as tkFont

from tkinter import *
import mysql.connector
import hashlib
import random
import string
from functions import *


class win_controler:
    def __init__(self, root):
        self.root = root
        self.win = LogIn_Window(root, self)

    def goToRegWin(self):
        self.win.destroy_all()
        self.win = Register_Window(self.root, self)

    def goToLogWin(self):
        self.win.destroy_all()
        self.win = LogIn_Window(self.root, self)

    def goToAdminWin(self):
        self.win.destroy_all()
        self.win = Admin_Window(self.root, self)

    def goToStudentWin(self, userId):
        self.win.destroy_all()
        self.win = Student_Window(self.root, self, userId)

    def goToSearchWin(self):
        self.win.destroy_all()
        self.win = Search_Window(self.root, self)


class Window:
    def __init__(self, root):
        self.elements = []
        self.root = root
        root.protocol("WM_DELETE_WINDOW", self.closeApp)

    def destroy_all(self):
        for el in self.elements:
            el.destroy()

    def closeApp(self):
        if messagebox.askokcancel("Quit?", "Stvarno zelite da iskljucite?"):
            root.destroy()
            return True
        return False


class LogIn_Window(Window):

    def __init__(self, root, controler):
        self.controler = controler
        Window.__init__(self, root)
        # setting title
        self.root.config(menu=0)
        root.title("Agencije")
        # setting window size
        width = 643
        height = 446
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        # btn1 = Button(root, text="Encrypted file", bg="#808080", command=addPath1)

        self.entry_username = tk.Entry(root, fg="#333333", justify="center")
        self.entry_username.place(x=250, y=90, width=147, height=30)

        self.entry_password = tk.Entry(root, fg="#333333", justify="center", show="*")
        self.entry_password.place(x=250, y=180, width=147, height=30)

        self.lbl_username = tk.Label(root, fg="#333333", justify="center", text="Korisnicko ime")
        self.lbl_username.place(x=250, y=50, width=113, height=37)

        self.lbl_password = tk.Label(root, fg="#333333", justify="center", text="Lozinka")
        self.lbl_password.place(x=230, y=150, width=108, height=30)

        self.btn_login = tk.Button(root, bg="#efefef", fg="#000000", justify="center", text="Prijavi se!")
        self.btn_login.place(x=260, y=270, width=128, height=30)
        self.btn_login["command"] = self.login

        self.lbl_text1 = tk.Label(root, fg="#333333", justify="center", text="Nemas nalog?")
        self.lbl_text1.place(x=240, y=310, width=168, height=30)

        self.btn_switch_page = tk.Button(root, bg="#efefef", fg="#000000", justify="center", text="Registruj se")
        self.btn_switch_page.place(x=280, y=340, width=88, height=30)
        self.btn_switch_page["command"] = self.switchToReg

        self.elements.append(self.entry_username)
        self.elements.append(self.entry_password)
        self.elements.append(self.lbl_username)
        self.elements.append(self.lbl_password)
        self.elements.append(self.btn_login)
        self.elements.append(self.lbl_text1)
        self.elements.append(self.btn_switch_page)

    def login(self):
        entry_pwd = self.entry_password.get()
        con = mysql.connector.connect(host="localhost", user="root", password="", database="marketing_agencies")
        csr = con.cursor()
        sql = "select salt,password, userType, userId from users where username='" + self.entry_username.get() + "'"
        csr.execute(sql)
        rez = csr.fetchall()
        if len(rez) == 0:
            messagebox.showwarning(title="Upozorenje!", message="Korisnik sa tim korisnickim imenom ne postoji!")
            con.close()
        else:
            salt = rez[0][0]
            hash_value = rez[0][1]
            if hashlib.sha256((entry_pwd + salt).encode()).hexdigest() == hash_value:
                messagebox.showinfo(title="Uspesno!", message="Prijavljivanje uspesno izvrseno!")
                # prebaci se na user interfejs
                if rez[0][2] == 3:
                    self.controler.goToAdminWin()
                elif rez[0][2] == 2:
                    messagebox.showinfo(title="Obavestenje", message="Vas nalog jos uvek nije odobren")
                elif rez[0][2] == 1:
                    self.controler.goToStudentWin(rez[0][3])


            else:
                messagebox.showwarning(title="Upozorenje!", message="Pogresna lozinka!")

    def switchToReg(self):
        self.controler.goToRegWin()


class Register_Window(Window):
    def __init__(self, root, controler):
        Window.__init__(self, root)
        self.controler = controler
        self.root.config(menu=0)
        # setting title
        root.title("Agencije")
        # setting window size
        width = 643
        height = 445
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.entry_name = tk.Entry(root, fg="#333333", justify="center")
        self.entry_name.place(x=180, y=60, width=122, height=30)
        self.elements.append(self.entry_name)

        self.entry_surname = tk.Entry(root, fg="#333333", justify="center")
        self.entry_surname.place(x=310, y=60, width=122, height=30)
        self.elements.append(self.entry_surname)

        self.entry_username = tk.Entry(root, fg="#333333", justify="center")
        self.entry_username.place(x=180, y=120, width=250, height=30)
        self.elements.append(self.entry_username)

        self.entry_password = tk.Entry(root, fg="#333333", justify="center", show="*")
        self.entry_password.place(x=180, y=180, width=122, height=30)
        self.elements.append(self.entry_password)

        self.entry_password2 = tk.Entry(root, fg="#333333", justify="center", show="*")
        self.entry_password2.place(x=310, y=180, width=122, height=30)
        self.elements.append(self.entry_password2)

        self.btn_register = tk.Button(root, bg="#efefef", fg="#000000", justify="center", text="Registruj se")
        self.btn_register.place(x=230, y=240, width=151, height=30)
        self.btn_register["command"] = self.register
        self.elements.append(self.btn_register)

        self.btn_switch = tk.Button(root, bg="#efefef", fg="#000000", justify="center", text="Prijavi se")
        self.btn_switch.place(x=270, y=330, width=70, height=25)
        self.btn_switch["command"] = self.switchToLog
        self.elements.append(self.btn_switch)

        self.lbl_text1 = tk.Label(root, fg="#333333", justify="center", text="Imas nalog?")
        self.lbl_text1.place(x=260, y=290, width=90, height=30)
        self.elements.append(self.lbl_text1)

        self.lbl_name = tk.Label(root, fg="#333333", justify="center", text="Ime")
        self.lbl_name.place(x=160, y=30, width=82, height=30)
        self.elements.append(self.lbl_name)

        self.lbl_surname = tk.Label(root, fg="#333333", justify="center", text="Prezime")
        self.lbl_surname.place(x=300, y=30, width=70, height=25)
        self.elements.append(self.lbl_surname)

        self.lbl_username = tk.Label(root, fg="#333333", justify="center", text="Korisnicko ime")
        self.lbl_username.place(x=170, y=90, width=123, height=30)
        self.elements.append(self.lbl_username)

        self.lbl_password1 = tk.Label(root, fg="#333333", justify="center", text="Lozinka")
        self.lbl_password1.place(x=160, y=150, width=95, height=30)
        self.elements.append(self.lbl_password1)

        self.lbl_password2 = tk.Label(root, fg="#333333", justify="center", text="Ponovo unesi lozinku")
        self.lbl_password2.place(x=300, y=150, width=139, height=30)
        self.elements.append(self.lbl_password2)

    def register(self):
        # messagebox.showwarning(title="Warning!", message="Add encrypted file first!")
        if self.entry_password.get() != self.entry_password2.get():
            messagebox.showerror(title="Greska!", message="Unete lozinke se ne podudaraju!")
            return
        if len(self.entry_password.get()) < 6:
            messagebox.showerror(title="Greska!", message="Lozinka mora imati bar 6 karaktera!")
            return
        # potencijalno promeniti u regularan izraz
        for letter in self.entry_name.get():
            if letter.upper() not in "QWERTYUIOPASDFGHJKLZXCVBNM":
                messagebox.showerror(title="Greska!", message="Ime i prezime moraju biti slova!")
        for letter in self.entry_surname.get():
            if letter.upper() not in "QWERTYUIOPASDFGHJKLZXCVBNM":
                messagebox.showerror(title="Greska!", message="Ime i prezime moraju biti slova!")

        # provera da li username postoji u bazi
        con = mysql.connector.connect(host="localhost", user="root", password="", database="marketing_agencies")
        csr = con.cursor()
        sql = "select count(username) from users where username='" + self.entry_username.get() + "'"
        csr.execute(sql)
        rez = csr.fetchone()
        if rez[0] != 0:
            messagebox.showwarning(title="Upozorenje!", message="Korisnik sa tim korisnickim imenom vec postoji!")
            con.close()
            return

        salt = generate_salt()
        pwd = self.entry_password.get()
        concat = pwd + salt
        hash_pwd = hashlib.sha256(concat.encode()).hexdigest()
        sql = "insert into users values (null, '" + self.entry_name.get() + "', '" + self.entry_surname.get() + "',  2, '" + \
              hash_pwd + "', '" + salt + "', '" + self.entry_username.get().lower() + "')"
        print(sql)
        csr.execute(sql)
        con.close()
        messagebox.showinfo(title="Uspesno!", message="Registracija uspesno izvrsena!")
        self.switchToLog()

    def switchToLog(self):
        self.controler.goToLogWin()


class Admin_Window(Window):
    def __init__(self, root, controler):
        self.controler = controler
        Window.__init__(self, root)
        # setting title
        root.title("Agencije - Admin")
        # setting window size
        width = 643
        height = 445
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.labelUserId = tk.Label(root, fg="#333333", justify="center", text="Unesite ID korisnika :")
        self.labelUserId.place(x=150, y=110, width=120, height=30)
        self.elements.append(self.labelUserId)

        self.inputId = tk.Entry(root, fg="#333333", justify="center")
        self.inputId.place(x=150, y=160, width=259, height=30)
        self.elements.append(self.inputId)

        self.removeBtn = tk.Button(root, bg="#efefef", fg="#000000", justify="center", text="Ukloni")
        self.removeBtn.place(x=310, y=230, width=80, height=30)
        self.removeBtn["command"] = self.removeUser
        self.elements.append(self.removeBtn)

        self.promoteBtn = tk.Button(root, bg="#efefef", fg="#000000", justify="center", text="Unapredi")
        self.promoteBtn.place(x=170, y=230, width=80, height=30)
        self.promoteBtn["command"] = self.promoteUser
        self.elements.append(self.promoteBtn)

        self.logOutBtn = tk.Button(root, bg="#efefef", fg="#000000", justify="center", text="Odjavi se")
        self.logOutBtn.place(x=240, y=310, width=80, height=30)
        self.logOutBtn["command"] = self.logOut
        self.elements.append(self.logOutBtn)

    def removeUser(self):
        userId = self.inputId.get()
        # removeUser(userId)
        self.controler.goToAdminWin()
        messagebox.showinfo(title="Uspeli ste", message="Korisnik uspesno izbrisan")

    def promoteUser(self):
        userId = self.inputId.get()
        addUser(userId)
        self.controler.goToAdminWin()
        messagebox.showinfo(title="Uspeli ste", message="Korisniku je omogucen pristup")

    def logOut(self):
        self.controler.goToLogWin()


class Student_Window(Window):

    def __init__(self, root, controler, userId):
        self.controler=controler
        self.userId = userId
        super().__init__(root)

        def logOut():
            self.controler.goToLogWin()

        def search():
            self.controler.goToSearchWin()

        self.labelAgencije = tk.Label(root)
        ft = tkFont.Font(family='Times', size=23)
        self.labelAgencije["font"] = ft
        self.labelAgencije["fg"] = "#333333"
        self.labelAgencije["justify"] = "center"
        self.labelAgencije["text"] = "AGENCIJE"
        self.labelAgencije.place(x=80, y=370, width=150, height=25)
        self.elements.append(self.labelAgencije)

        self.labelKlijenti = tk.Label(root)
        self.labelKlijenti["font"] = ft
        self.labelKlijenti["fg"] = "#333333"
        self.labelKlijenti["justify"] = "center"
        self.labelKlijenti["text"] = "KLIJENTI"
        self.labelKlijenti.place(x=400, y=370, width=150, height=25)
        self.elements.append(self.labelKlijenti)

        cols = ('id', 'Ime', 'Zaposlenih', 'Postcode')
        self.listBox = ttk.Treeview(root, columns=cols, show='headings', height=15)
        verscrlbar = ttk.Scrollbar(root, orient="vertical", command=self.listBox.yview)
        # verscrlbar.grid(row=1, column=0, columnspan=1, sticky="E")
        self.listBox.configure(xscrollcommand=verscrlbar.set)

        self.listBox.column("id", width=50, anchor='center')
        self.listBox.column("Ime", width=100, anchor='center')
        self.listBox.column("Zaposlenih", width=100, anchor='center')
        self.listBox.column("Postcode", width=100, anchor='center')

        for col in cols:
            self.listBox.heading(col, text=col)
            self.listBox.grid(row=1, column=0, columnspan=2)
            self.listBox.place(x=10, y=20)

        agencies = loadAgencies()
        for agency in agencies:
            self.listBox.insert("", "end", values=(agency[0], agency[1], agency[2], agency[3]))
        self.listBox.bind('<Double-Button-1>', lambda event: self.showAgency(event, agencies))
        self.elements.append(self.listBox)

        cols2 = ('id', 'Ime')
        self.listBox2 = ttk.Treeview(root, columns=cols2, show='headings', height=15)
        verscrlbar2 = ttk.Scrollbar(root, orient="vertical", command=self.listBox2.yview)
        # verscrlbar.grid(row=1, column=0, columnspan=1, sticky="E")
        self.listBox2.configure(xscrollcommand=verscrlbar2.set)

        self.listBox2.column("id", width=50, anchor='center')
        self.listBox2.column("Ime", width=100, anchor='center')

        for col2 in cols2:
            self.listBox2.heading(col2, text=col2)
            self.listBox2.grid(row=1, column=0, columnspan=2)
            self.listBox2.place(x=400, y=20)

        clients = loadClients()
        for client in clients:
            self.listBox2.insert("", "end", values=(client[0], client[2]))
        #self.listBox.bind('<Double-Button-1>', lambda event: self.showAgency(event, agencies))
        self.elements.append(self.listBox2)

        self.btnOdjava = tk.Button(root, bg="#f0f0f0", fg="#000000", justify="center", text="Odjava")
        self.btnOdjava.place(x=560, y=100, width=76, height=30)
        self.btnOdjava["command"] = logOut
        self.elements.append(self.btnOdjava)

        self.btnPretraga = tk.Button(root, bg="#f0f0f0", fg="#000000", justify="center", text="Pretraga")
        self.btnPretraga.place(x=560, y=60, width=76, height=30)
        self.btnPretraga["command"] = search
        self.elements.append(self.btnPretraga)

    def showAgency(self, event, agencies):
        # id reda na koji je kliknut mis
        rowId = self.listBox.selection()[0]
        select = self.listBox.set(rowId)
        print(select["id"])

        Window.destroy_all(self)

        self.labelRadnici = tk.Label(root)
        ft = tkFont.Font(family='Times', size=23)
        self.labelRadnici["font"] = ft
        self.labelRadnici["fg"] = "#333333"
        self.labelRadnici["justify"] = "center"
        self.labelRadnici["text"] = "ZAPOSLENI"
        self.labelRadnici.place(x=100, y=370, width=180, height=25)
        self.elements.append(self.labelRadnici)

        self.labelIME = tk.Label(root)
        self.labelIME["font"] = ft
        self.labelIME["fg"] = "#333333"
        self.labelIME["justify"] = "center"
        self.labelIME["text"] = "IME AGENCIJE"
        self.labelIME.place(x=430, y=120, width=180, height=25)
        self.elements.append(self.labelIME)

        self.labelGRAD = tk.Label(root)
        self.labelGRAD["font"] = ft
        self.labelGRAD["fg"] = "#333333"
        self.labelGRAD["justify"] = "center"
        self.labelGRAD["text"] = "IME GRADA"
        self.labelGRAD.place(x=430, y=200, width=180, height=25)
        self.elements.append(self.labelGRAD)

        #Dodati stranicu koja ispisuje sve
        cols = ('id', 'Ime', 'Prezime', 'Adresa')
        self.listBox = ttk.Treeview(root, columns=cols, show='headings', height=15)
        verscrlbar = ttk.Scrollbar(root, orient="vertical", command=self.listBox.yview)
        # verscrlbar.grid(row=1, column=0, columnspan=1, sticky="E")
        self.listBox.configure(xscrollcommand=verscrlbar.set)

        self.listBox.column("id", width=50, anchor='center')
        self.listBox.column("Ime", width=100, anchor='center')
        self.listBox.column("Prezime", width=100, anchor='center')
        self.listBox.column("Adresa", width=100, anchor='center')

        for col in cols:
            self.listBox.heading(col, text=col)
            self.listBox.grid(row=1, column=0, columnspan=2)
            self.listBox.place(x=10, y=20)

        workers = loadWorkers(select["id"])
        for worker in workers:
            self.listBox.insert("", "end", values=(worker[0], worker[1], worker[2], worker[4]))
        self.listBox.bind('<Double-Button-1>', lambda event: self.showWorker(event, workers))
        self.elements.append(self.listBox)
        ime=getCompany(select["id"])
        self.labelIME.config(text=str(ime[0][0]))
        grad = returnCity(select['id'])
        self.labelGRAD.config(text=str(grad[0][0]))

    def showWorker(self,event, workers):
        rowId = self.listBox.selection()[0]
        select = self.listBox.set(rowId)
        print(select["id"])
        Window.destroy_all(self)

        #
        self.label1 = tk.Label(root, fg="#333333", justify="center", text="Ime: ")
        self.label1.place(x=40, y=70, width=70, height=25)
        self.elements.append(self.label1)

        self.labelName = tk.Label(root, fg="#333333", justify="center", text="1null ")
        self.labelName.place(x=110, y=70, width=99, height=30)
        self.elements.append(self.labelName)

        self.label2 = tk.Label(root, fg="#333333", justify="center", text="Prezime: ")
        self.label2.place(x=40, y=120, width=70, height=25)
        self.elements.append(self.label2)

        self.labelSurname = tk.Label(root, fg="#333333", justify="center", text="2null ")
        self.labelSurname.place(x=120, y=120, width=75, height=30)
        self.elements.append(self.labelSurname)

        self.label3 = tk.Label(root, fg="#333333", justify="center", text="Pol: ")
        self.label3.place(x=30, y=160, width=70, height=25)
        self.elements.append(self.label3)

        self.labelGender = tk.Label(root, fg="#333333", justify="center", text="3null ")
        self.labelGender.place(x=120, y=160, width=70, height=25)
        self.elements.append(self.labelGender)

        self.label4 = tk.Label(root, fg="#333333", justify="center", text="Adresa: ")
        self.label4.place(x=280, y=70, width=70, height=25)
        self.elements.append(self.label4)

        self.labelAdress = tk.Label(root, fg="#333333", justify="center", text="4null ")
        self.labelAdress.place(x=370, y=70, width=143, height=30)
        self.elements.append(self.labelAdress)

        self.label5 = tk.Label(root, fg="#333333", justify="center", text="Zaposlen u: ")
        self.label5.place(x=290, y=110, width=70, height=25)
        self.elements.append(self.label5)

        self.labelCompany = tk.Label(root, fg="#333333", justify="center", text="5null ")
        self.labelCompany.place(x=380, y=110, width=123, height=30)
        self.elements.append(self.labelCompany)

        self.label6 = tk.Label(root, fg="#333333", justify="center", text="ID radnika: ")
        self.label6.place(x=270, y=150, width=89, height=30)
        self.elements.append(self.label6)

        self.labelExamine = tk.Label(root, fg="#333333", justify="center", text="6null ")
        self.labelExamine.place(x=380, y=150, width=111, height=30)
        self.elements.append(self.labelExamine)

        self.btnBack = tk.Button(root, bg="#efefef", fg="#000000", justify="center", text="Nazad")
        self.btnBack.place(x=450, y=400, width=102, height=37)
        self.btnBack["command"] = self.povratak
        self.elements.append(self.btnBack)

        self.labelHeading = tk.Label(root)
        ft = tkFont.Font(family='Times', size=23)
        self.labelHeading["font"] = ft
        self.labelHeading["fg"] = "#333333"
        self.labelHeading["justify"] = "center"
        self.labelHeading["text"] = "LICNA KARTA RADNIKA"
        self.labelHeading["relief"] = "flat"
        self.labelHeading.place(x=110, y=0, width=376, height=74)
        self.elements.append(self.labelHeading)

        worker = showWorker(select["id"])
        self.labelName.config(text=str(worker[0][1]))
        self.labelSurname.config(text=str(worker[0][2]))
        self.labelGender.config(text=str(worker[0][3]))
        self.labelAdress.config(text=str(worker[0][4]))
        company_name= getCompany(worker[0][5])
        self.labelCompany.config(text=str(company_name[0][0]))
        self.labelExamine.config(text=str(worker[0][0]))



    def povratak(self):
        self.controler.goToLogWin()
        self.controler.goToStudentWin(2)

class Search_Window(Window):
    def __init__(self, root, controler):
        self.controler = controler
        Window.__init__(self, root)
        # setting title
        root.title("Agencije - Pretraga")
        # setting window size
        width = 643
        height = 445
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.labelUserId = tk.Label(root, fg="#333333", justify="center", text="Pretrazite korisnika po imenu:")
        self.labelUserId.place(x=420, y=110, width=180, height=30)
        self.elements.append(self.labelUserId)

        self.inputId = tk.Entry(root, fg="#333333", justify="center")
        self.inputId.place(x=400, y=160, width=259, height=30)
        self.elements.append(self.inputId)

        self.btnSearch = tk.Button(root, bg="#efefef", fg="#000000", justify="center", text="Pretrazi")
        self.btnSearch.place(x=480, y=230, width=80, height=30)
        self.btnSearch["command"] = self.searchByName
        self.elements.append(self.btnSearch)

        self.logOutBtn = tk.Button(root, bg="#efefef", fg="#000000", justify="center", text="Vrati se")
        self.logOutBtn.place(x=480, y=310, width=80, height=30)
        self.logOutBtn["command"] = self.logOut
        self.elements.append(self.logOutBtn)

        # Dodati stranicu koja ispisuje sve
        cols = ('id', 'Ime', 'Prezime', 'Kompanija')
        self.listBox = ttk.Treeview(root, columns=cols, show='headings', height=15)
        verscrlbar = ttk.Scrollbar(root, orient="vertical", command=self.listBox.yview)
        # verscrlbar.grid(row=1, column=0, columnspan=1, sticky="E")
        self.listBox.configure(xscrollcommand=verscrlbar.set)

        self.listBox.column("id", width=50, anchor='center')
        self.listBox.column("Ime", width=100, anchor='center')
        self.listBox.column("Prezime", width=100, anchor='center')
        self.listBox.column("Kompanija", width=100, anchor='center')

        for col in cols:
            self.listBox.heading(col, text=col)
            self.listBox.grid(row=1, column=0, columnspan=2)
            self.listBox.place(x=10, y=20)


    def searchByName(self):
        userName = self.inputId.get()
        if self.inputId.get() == '':
            messagebox.showinfo(title="Paznja!", message="Unesite tekst u polje za pretragu.")
        else:
            self.listBox.destroy()

            cols = ('id', 'Ime', 'Prezime', 'Kompanija')
            self.listBox = ttk.Treeview(root, columns=cols, show='headings', height=15)
            verscrlbar = ttk.Scrollbar(root, orient="vertical", command=self.listBox.yview)
            self.listBox.configure(xscrollcommand=verscrlbar.set)

            self.listBox.column("id", width=50, anchor='center')
            self.listBox.column("Ime", width=100, anchor='center')
            self.listBox.column("Prezime", width=100, anchor='center')
            self.listBox.column("Kompanija", width=100, anchor='center')

            for col in cols:
                self.listBox.heading(col, text=col)
                self.listBox.grid(row=1, column=0, columnspan=2)
                self.listBox.place(x=10, y=20)

            rez = nameSearch(userName)

            print(rez)
            for worker in rez:
                self.listBox.insert("", "end", values=(worker[0], worker[1], worker[2], worker[4]))
            self.elements.append(self.listBox)

    def logOut(self):
        self.controler.goToStudentWin(2)

if __name__ == "__main__":
    root = tk.Tk()
    controler = win_controler(root)
    root.mainloop()
