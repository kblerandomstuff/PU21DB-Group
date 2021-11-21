#@title Test input
import cx_Oracle
from datetime import datetime

def getallproduct():
  db_host = 'base.krs.ovh'
  port = 1521
  user = "krs"
  password="krs"
  sname="ORCLCDB.localdomain"
  dsnStr = cx_Oracle.makedsn(db_host, port, service_name=sname)
  conn = cx_Oracle.connect(user, password, dsn=dsnStr, encoding="UTF-8")
  cursor=conn.cursor()
  cursor.execute('select * from inv')
  l=list(cursor.fetchall())
  return l

def selectpid():
  p=getallproduct()
  m={}
  c=0
  for row in p:
    if row[1] not in m.values():
      m[c]=row[1]
      c=c+1
  for i in m:
    print(i,":",m[i])
  sm=int(input("select"))
  s={}
  c=0
  for row in p:
    if row[1]==m[sm] and row[2] not in s.values():
      s[c]=row[2]
      c=c+1
  for i in s:
    print(i,":",s[i])
  ss=int(input("select"))
  cl={}
  c=0
  for row in p:
    if row[1]==m[sm] and row[2]==s[ss] and row[3] not in cl.values():
      cl[c]=row[3]
      c=c+1
  for i in cl:
     print(i,":",cl[i])
  scl=int(input("select"))
  try:
    for row in p:
      if row[1]==m[sm] and row[2]==s[ss] and row[3]==cl[scl]:
        return row
      else:
        continue
  except all as error:
    print(error)


print(selectpid())