# @title Main program { form-width: "30%" }

# import proper packages
import cx_Oracle
from datetime import datetime

db_host = 'base.krs.ovh'
port = 1521
user = "krs"
password = "krs"
sname = "ORCLCDB.localdomain"


# Database

def getallproduct():
    dsnStr = cx_Oracle.makedsn(db_host, port, service_name=sname)
    conn = cx_Oracle.connect(user, password, dsn=dsnStr, encoding="UTF-8")
    cursor = conn.cursor()
    cursor.execute('select * from inv')
    l = list(cursor.fetchall())
    return l


def getproduct(x):
    dsnStr = cx_Oracle.makedsn(db_host, port, service_name=sname)
    conn = cx_Oracle.connect(user, password, dsn=dsnStr, encoding="UTF-8")
    cursor = conn.cursor()
    cursor.execute('select * from inv where p_id=:id', x)
    l = list(cursor.fetchall())
    return l


def selectp():
    p = getallproduct()
    m = {}
    c = 0
    for row in p:
        if row[1] not in m.values():
            m[c] = row[1]
            c = c + 1
    for i in m:
        print(i, ":", m[i])
    sm = int(input("select"))
    s = {}
    c = 0
    for row in p:
        if row[1] == m[sm] and row[2] not in s.values():
            s[c] = row[2]
            c = c + 1
    for i in s:
        print(i, ":", s[i])
    ss = int(input("select"))
    cl = {}
    c = 0
    for row in p:
        if row[1] == m[sm] and row[2] == s[ss] and row[3] not in cl.values():
            cl[c] = row[3]
            c = c + 1
    for i in cl:
        print(i, ":", cl[i])
    scl = int(input("select"))
    try:
        for row in p:
            if row[1] == m[sm] and row[2] == s[ss] and row[3] == cl[scl]:
                return row
            else:
                continue
    except all as error:
        print(error)


def getalllog():
    dsnStr = cx_Oracle.makedsn(db_host, port, service_name=sname)
    conn = cx_Oracle.connect(user, password, dsn=dsnStr, encoding="UTF-8")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tlog")
    l = list(cursor.fetchall())
    return l


#def viewinv():


def addlog(t_type, id, no):
    dsnStr = cx_Oracle.makedsn(db_host, port, service_name=sname)
    conn = cx_Oracle.connect(user, password, dsn=dsnStr, encoding="UTF-8")
    cursor = conn.cursor()
    d = datetime.now()
    try:
        cursor.execute("INSERT INTO tlog VALUES(:t_time,:p_id,:t_type,:amount)", [d, id, t_type, no])
    except cx_Oracle.Error as error:
        print(error)
    conn.commit()


def takep():
    s = selectp()
    n = int(input("number:"))
    dsnStr = cx_Oracle.makedsn(db_host, port, service_name=sname)
    conn = cx_Oracle.connect(user, password, dsn=dsnStr, encoding="UTF-8")
    cursor = conn.cursor()
    p = getproduct(s[0])
    t = p[7] - n
    if t >= 0:
        cursor.execute("UPDATE inv SET amount=:t where p_id=:id", [int(t), s[0]])
        addlog("o", s[0], n)
    else:
        print("the number you get is larger than stock")


def menu():
    exit = False
    while exit != False:
        clear_output()
        print("Welcome")
        print("")
        print()
        c = input("choice")
        if c == 1:
            view()
        elif c == 2:
            add
        elif c == 3:
            taken
        elif c == 2:
            report
        elif c == 2:
            log
        elif c == 2:
            damage
        elif c == 2:
            exit
        else:
            print("error")
