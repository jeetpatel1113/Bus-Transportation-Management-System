# Bus Modules
import random
import pymysql
import math
conn=pymysql.connect(host='localhost',user='root',passwd='root',db='sjd')
Cursor=conn.cursor()

def Booking(bus,seat):
    bno=random.choice(bus)
    seatno=random.randrange(1,seat+1)

##    l='select available from bus where busno = '+str(bno)+';'
##    Cursor.execute(l)
##    data=Cursor.fetchall()
##    print(data)
##    if data[0][0]=='Y' :
##        pass

    sql='select seatno from customer where busno = '+str(bno)+';'
    Cursor.execute(sql)
    data=Cursor.fetchall()
    Seat=[]
    for i in range(len(data)) :
      Seat.append(data[i][0])  
    if seatno not in Seat :
        return seatno,bno

def Payment(a,d,ch,opt) :
    d1={'Purva Gam, Navsari':-23, 'Sarthana National Park, Surat':-15, 'Patrakar Colony, Surat':0, 'Someshwar Junction, Surat':5, 'Motilal Chowk, Gandhinagar':30, 'Shantiniketan Colony, Ahmedabad':37}
    if a in d1 :
      if d in d1 :
         km=math.sqrt((d1[d]-d1[a])**2)

    if ch==1 and opt==1 :
        pay=100
    elif ch==1 and opt==2 :
        pay=250
    elif ch==2 and opt==1 :
        pay=310
    elif ch==2 and opt==2 :
        pay=320
    elif ch==3 and opt==1 :
        pay=375
    elif ch==3 and opt==2 :
        pay=340

    Pay=pay*km

    return Pay
