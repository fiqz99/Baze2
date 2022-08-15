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
    sql = "select * from workers where agency_id =" + str(id)
    csr.execute(sql)
    rez = csr.fetchall()
    return rez
