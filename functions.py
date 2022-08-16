import mysql.connector
import random
import string
import tkinter as tk
from tkinter import filedialog


def generate_salt():
    ran = "".join(random.choices(string.ascii_uppercase + string.digits, k=8))
    return ran

def addUser(userId):
    con = mysql.connector.connect(host="localhost", user="root", password="", database="marketing_agencies")
    csr = con.cursor()
    sql = "update users set userType=1 where userId=" + userId
    csr.execute(sql)
    con.commit()

def loadAgencies():
    con = mysql.connector.connect(host="localhost", user="root", password="", database="marketing_agencies")
    csr = con.cursor()
    sql = "select * from marketing_agency"
    csr.execute(sql)
    rez = csr.fetchall()
    return rez

def loadWorkers(id):
    con = mysql.connector.connect(host="localhost", user="root", password="", database="marketing_agencies")
    csr = con.cursor()
    sql = "select * from worker where agency_id =" + str(id)
    csr.execute(sql)
    rez = csr.fetchall()
    return rez

def showWorker(id):
    print(id)
    con = mysql.connector.connect(host="localhost", user="root", password="", database="marketing_agencies")
    csr = con.cursor()
    sql = "select * from worker where worker_id =" + str(id)
    csr.execute(sql)
    rez = csr.fetchall()
    return rez

def getCompany(id):
    print(id)
    con = mysql.connector.connect(host="localhost", user="root", password="", database="marketing_agencies")
    csr = con.cursor()
    sql = "select agency_name from marketing_agency where agency_id =" + str(id)
    csr.execute(sql)
    rez = csr.fetchall()
    return rez

def loadClients():
    con = mysql.connector.connect(host="localhost", user="root", password="", database="marketing_agencies")
    csr = con.cursor()
    sql = "select * from clients"
    csr.execute(sql)
    rez = csr.fetchall()
    return rez

def nameSearch(name):
    con = mysql.connector.connect(host="localhost", user="root", password="", database="marketing_agencies")
    csr = con.cursor()
    sql = "select * from worker where worker_name like '%" + name + "%'"
    csr.execute(sql)
    rez = csr.fetchall()
    return rez

def returnPostCode(id):
    con = mysql.connector.connect(host="localhost", user="root", password="", database="marketing_agencies")
    csr = con.cursor()
    sql = "select city_postCode from marketing_agency where agency_id =" + str(id)
    csr.execute(sql)
    rez = csr.fetchall()
    return rez

def returnCity(id):
    con = mysql.connector.connect(host="localhost", user="root", password="", database="marketing_agencies")
    csr = con.cursor()
    postcode = returnPostCode(id)
    sql = "select city_name from city where post_code =" + str(postcode[0][0])
    csr.execute(sql)
    rez = csr.fetchall()
    retu
