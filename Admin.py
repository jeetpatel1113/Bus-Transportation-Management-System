# Admin Modules
import Buses
import datetime as dt
import pymysql
from tabulate import tabulate as tb
conn=pymysql.connect(host='localhost',user='root',passwd='root',db='sjd')
Cursor=conn.cursor()

#1.
def password():
       passw=input('\nPassword : ')
       if passw == 'sjd729909':
              pass
       elif passw == 'sjd9979200':
              pass
       else:
              print ("Incorrect Password !!")
              print ("Please Try Again")
              return password()

#2.
def MainMenu():
       print("\n ================================")
       print("| 三  M A I N  M E N U           |")
       print(" --------------------------------")
       print("| 1. Employees                   |")
       print("| 2. Buses                       |")
       print("| 3. Customers                   |")
       print("| 4. Report Menu                 |")
       print("| 5. All Data                    |")
       print("| 6. Instructions for Data Setup |")
       print("| 7. Exit                        |")
       print(" ================================")

#3.
def Employee():
       print('\nOK ! WHAT YOU WANT TO OPERATE FROM THE FOLLOWING ?')
       print('1. Add Employee')
       print('2. Update Employee')
       print('3. Show all Employee List')
       print('4. Search Employee Details')
       print('5. Delete Employee')
       print('6. Exit')


#3.1.
def AddEmp():
       fp=open('datainmysql.txt','a')
       ename=input('Name : ')
       job=input('Employment : ')
       if job == 'Travel Consultant' :
              comm=int(input('Commission (per head) :'))
              sal=0
       else :
              comm=0
              sal=int(input('Salary : '))
       hiredate=dt.date.today()
       deptno=int(input('Department No. :'))
       phoneno=int(input('Phone No. : '))
       while len(str(phoneno)) != 10 :
              print('Wrong Input !!')
              phoneno=int(input('Phone No. : '))
       sql="insert into employee values (NULL, '"+str(ename.title())+"', '"+str(job.title())+"', '"+str(hiredate)+"', "+str(sal)+", "+str(comm)+", "+str(deptno)+", '"+str(phoneno)+"');"
       Cursor.execute(sql)
       fp.write(sql+'\n')
       conn.commit()
       print("RECORD SAVED SUCCESSFULLY !!")

#3.2.
def UpdateEmp():
       print('\n<><><><><><><><><><><><><><><><><>')
       print('| 三 U P D A T E   O P T I O N S |')
       print('<><><><><><><><><><><><><><><><><>')
       print('| 1. Name                        |')
       print('| 2. Job                         |')
       print('| 3. Commission (per head)       |')
       print('| 4. Salary                      |')
       print('| 5. Department No.              |')
       print('| 6. Phone No.                   |')
       print('<><><><><><><><><><><><><><><><><>')

       op=input('\nUpdate Option (You can take more than one option with space): ')
       op=op.split(' ')
       ename=input('Employee Name : ')
       for i in op :
                           
              if i=='1' :
                     name=input('New Employee Name :')
                     sql="update employee set ename='"+str(name.title())+"' where ename='"+str(ename)+"';"

              elif i=='2' :
                     job=input('New Employment :')
                     sql="update employee set job='"+str(job.title())+"' where ename='"+str(ename)+"';"
                     Cursor.execute(sql)
                     conn.commit()

              elif i=='3' :
                     comm=int(input('New Commission Payment:'))
                     sql="update employee set comm="+str(comm)+" where ename='"+str(ename)+"';"
                           
              elif i=='4' :
                     sal=int(input('New Salary :'))
                     sql="update employee set salary="+str(sal)+" where ename='"+str(ename)+"';"
                           
              elif i=='5' :
                     deptno=int(input('New Department No. :'))
                     sql="update employee set deptno="+str(deptno)+" where ename='"+str(ename)+"';"
                           
              elif i=='6' :
                     phoneno=int(input('Phone No. :'))
                     sql="update employee set phoneno='"+str(phoneno)+"' where ename='"+str(ename)+"';"

              Cursor.execute(sql)
              conn.commit()       

       print("RECORD UPDATED SUCCESSFULLY !!")  

#3.3.
def ShowEmp():
       sql='select * from employee;'
       Cursor.execute(sql)
       data=Cursor.fetchall()
       h=['EMPNO','ENAME','JOB','HIREDATE','SALARY','COMM','DEPTNO','PHONENO']
       print(tb(data,headers=h,tablefmt='psql'))
       sql='select count(*) from employee;'
       Cursor.execute(sql)
       data=Cursor.fetchall()
       print('Number of Datas :',data[0][0])

#3.4.
def SearchEmp() :
       print('\n<><><><><><><><><><><><><><><><><>')
       print('| 三 S E A R C H   O P T I O N S |')
       print('<><><><><><><><><><><><><><><><><>')
       print('| 1. Employee No.                |')
       print('| 2. Employee Name               |')
       print('| 3. Job                         |')
       print('| 4. Commission (per head)       |')
       print('| 5. Salary                      |')
       print('| 6. Department No.              |')
       print('| 7. Phone No.                   |')
       print('<><><><><><><><><><><><><><><><><>')
       ch=int(input('\nSearch Option : '))

       sql=''

       if ch==1:
                opt3=int(input('OK ! Want to do \n1. Exact Search or \n2. Incremental Search or \n3. Search for a Series of Employees ?\n'))

                if opt3==1 :
                    empno=int(input('Employee No.: '))
                    sql='select * from employee where empno ='+str(empno)+' ;'
                    
                elif opt3==2:
                    num=int(input('Enter any digit of the Employee No. you are calling up :\n'))
                    sql="select * from employee where empno like '%"+str(num)+"%' ;"

                elif opt3==3 :
                    eno1=int(input('Employee No. from where you want to start : '))
                    ask=input('Want to enter the Employee No. till which you want : [Y/N] \n')
                    if ask=='Y' or ask=='y' :
                        eno2=int(input('Enter :'))
                        sql='select * from employee where empno between '+str(eno1)+' and '+str(eno2)+' ;'
                    else :
                        sql='select * from employee where empno >='+str(eno1)+' ;'    

       elif ch==2:
                opt4=int(input('OK ! Want to do \n1. Exact Search or \n2. Incremental Search ?\n'))

                if opt4==1 :
                    ename=input('Employee Name :')
                    sql="select * from employee where ename ='"+str(ename.title())+"' ;"
                    
                elif opt4==2:
                    rdn=input('Enter any alphabet or any group of alphabets in correct order of the Employee Name you are calling up :\n')
                    sql="select * from employee where ename like '%"+str(rdn)+"%' ;"

       elif  ch==3 :
                opt5=int(input('OK ! Want to do \n1. Exact Search or \n2. Incremental Search ?\n'))

                if opt5==1 :
                    job=input('Employment :')
                    sql="select * from employee where job ='"+str(job.title())+"' ;"

                elif opt5==2:
                    rdj=input('Enter any alphabet or any group of alphabets in correct order of the Employment you are calling up : ')
                    sql="select * from employee where job like '%"+str(rdj)+"%' ;"
                
       elif  ch==4 :
                opt6=int(input('OK ! Want to do \n1. Exact Search or \n2. Search for a Series of Employees ?\n'))

                if opt6==1 :
                    comm=float(input('Commission (per head) : '))
                    sql='select * from employee where comm ='+str(comm)+' ;'

                elif opt6==2 :
                    ask=int(input('Want to search for \n1. for all employees who are taking commission \n2. Particular employees '))
                    if ask==1 :
                        sql='select * from employee where comm is not null ;'

                    elif ask==2 :
                        comm1=float(input('Amount of Commission from where you want to start : '))
                        ask1=input('Want to enter the Amount of Commission till which you want : [Y/N] \n')
                        if ask=='Y' or ask=='y' :
                             comm2=int(input('Enter :'))
                             sql13='select * from employee where comm between '+str(comm1)+' and '+str(comm2)+' ;'
                        else :
                           sql='select * from employee where comm >='+str(comm1)+' ;'

       elif  ch==5 :
                opt7=int(input('OK ! Want to do \n1. Exact Search or \n2. Search for a Series of Employees ?\n'))

                if opt7==1 :
                    sal=float(input('Salary of that Employee : '))
                    sql='select * from employee where salary ='+str(sal)+' ;'

                elif opt7==2 :
                    ask=int(input('Want to search for \n1. for all employees who are taking salary \n2. Particular employees \n'))
                    if ask==1 :
                        sql='select * from employee where salary is not null ;'

                    elif ask==2 :
                        sal1=float(input('Amount of Salary from where you want to start : '))
                        ask1=input('Want to enter the Amount of Salary till which you want : [Y/N] \n')
                        if ask=='Y' or ask=='y' :
                             sal2=float(input('Enter :'))
                             sql='select * from employee where salary between '+str(sal1)+' and '+str(sal2)+' ;'
                        else :
                           sql='select * from employee where salary >='+str(sal1)+' ;'

       elif  ch==6 :
                opt8=int(input('OK ! Want to do \n1. Exact Search or \n2. Search for a Series of Employees ?\n'))

                if opt8==1 :
                    dept=int(input('Department No.: '))
                    sql='select * from employee where deptno ='+str(dept)+' ;'

                elif opt8==2 :
                    ask=int(input('Want to search for \n1. for all employees who are taking salary \n2. Particular employees\n '))
                    if ask==1 :
                        sql='select * from employee where deptno is not null ;'

                    elif ask==2 :
                        dept1=float(input('Department No. from where you want to start : '))
                        ask1=input('Want to enter the Department No. till which you want : [Y/N] \n')
                        if ask=='Y' or ask=='y' :
                             dept2=float(input('Enter :'))
                             sql='select * from employee where deptno between '+str(dept1)+' and '+str(dept2)+' ;'
                        else :
                           sql='select * from employee where deptno >='+str(dept1)+' ;'
                        
       elif  ch==7 :
                opt9=int(input('OK ! Want to do \n1. Exact Search or \n2. Incremental Search ?\n'))

                if opt9==1 :
                    pno=input('Phone No. :')
                    sql="select * from employee where phoneno ='"+str(pno)+"' ;"
                    

                elif opt9==2:
                    rdpn=input('Enter any alphabet or any group of alphabets in correct order of the Employment you are calling up : ')
                    sql="select * from employee where phoneno like '%"+str(rdpn)+"%' ;"
                    
       Cursor.execute(sql)
       data=Cursor.fetchall()
       h=['EMPNO','ENAME','JOB','HIREDATE','SALARY','COMM','DEPTNO','PHONENO']
       print(tb(data,headers=h,tablefmt='psql'))

#3.5.
def DelEmp() :
       ask=int(input('Want to delete by \n1.Name or \n2. Employee No. ?\n'))
       if ask==1 :
              name=input("Employee Name : ")
              sql="delete from employee where ename='"+str(name)+"' ;"
       elif ask==2 :
              eno=int(input('Employee No.: '))
              sql='delete from employee where empno='+str(eno)+' ;'
       Cursor.execute(sql)
       conn.commit()
       print('RECORD DELETED SUCCESSFULLY !!')

#4.
def Bus():
    print('OK ! WHAT YOU WANT TO OPERATE FROM THE FOLLOWING ?')
    print('1. Add New Bus Details')
    print('2. Update Bus Details')
    print('3. Show Bus Details')
    print('4. Search Bus Details')
    print('5. Delete Bus Details')
    print('6. Exit')
#4.1.
def AddBus():
       fp=open('datainmysql.txt','a')
       licenceno=input('Licence No. : ')
       doi=dt.date.today()
       cost=int(input('Price :'))
       bustype=input('Bus Type :')
       ask=input('Any Driver ? (Y/N)')
       if ask=='Y' or ask=='y' :
              d=input('Driver Name : ')
              t=input('Tour Guide : ')
              sql="insert into bus values (NULL, '"+str(licenceno)+"', '"+str(doi)+"', "+str(cost)+", '"+str(bustype)+"', '"+str(d)+"', '"+str(t)+"', 'Y');"
       else :
              sql="insert into bus values (NULL, '"+str(licenceno)+"', '"+str(doi)+"', "+str(cost)+", '"+str(bustype)+"', 'NA', 'NA', 'N');"
       fp.write(sql+'\n')
       Cursor.execute(sql)
       conn.commit()
       print("RECORD SAVED SUCCESSFULLY !!")

#4.2.
def UpdateBus() :
       print('\n<><><><><><><><><><><><><><><><><>')
       print('| 三 U P D A T E   O P T I O N S |')
       print('<><><><><><><><><><><><><><><><><>')
       print('| 1. Bus No.                     |')
       print('| 2. Licence No.                 |')
       print('| 3. Date of Issue               |')
       print('| 4. Price                       |')
       print('| 5. Bus Type                    |')
       print('| 6. Current Driver              |')
       print('| 7. Current Tour Guide          |')
       print('| 8. Current Availability        |')
       print('<><><><><><><><><><><><><><><><><>\n')
       op=input('Update Option (You can take more than one option with space): ')
       op=op.split(' ')
       busno=int(input('Bus No : '))
       for i in op :
              if i=='1' :
                     bno=int(input('New Bus No. :'))
                     sql="update bus set busno="+str(bno)+" where busno='"+str(busno)+"';"
                           
              elif i=='2' :
                     lno=input('New Licence No. :')
                     sql="update bus set licenceno='"+str(lno)+"' where busno='"+str(busno)+"';"

              elif i=='3' :
                     doi=input('Date of Issuing : ')
                     sql="update bus set doi='"+str(doi)+"' where busno='"+str(busno)+"';"       

              elif i=='4' :
                     price=int(input('New Price :'))
                     sql="update bus set price="+str(price)+" where busno='"+str(busno)+"';"

              elif i=='5' :
                     bt=input('Bus Type :')
                     sql="update bus set bustype='"+str(bt)+"' where busno='"+str(busno)+"';"

              elif i=='6' :
                     d=input('Driver Name : ')
                     sql="update bus set driver='"+str(d)+"' where busno='"+str(busno)+"';"

              elif i=='7' :
                     t=input('Tour Guide : ')
                     sql="update bus set tourguide='"+str(t)+"' where busno='"+str(busno)+"';"

              elif i=='8' :
                     aval=input('Available (Y/N) : ')
                     sql="update bus set available='"+str(aval)+"' where busno='"+str(busno)+"';"

              Cursor.execute(sql)
              conn.commit()       

       print("RECORD UPDATED SUCCESSFULLY !!")

#4.3.
def ShowBus():
       sql='select * from bus; '
       Cursor.execute(sql)
       data=Cursor.fetchall()
       h=['BUSNO','LICENCENO','DOI','PRICE','BUSTYPE','DRIVER','TOURGUIDE','AVAILABLE']
       print(tb(data,headers=h,tablefmt='psql'))
       sql='select count(*) from bus;'
       Cursor.execute(sql)
       data=Cursor.fetchall()
       print('Number of Datas :',data[0][0])

#4.4.
def SearchBus() :
       print('\n<><><><><><><><><><><><><><><><><>')
       print('| 三 S E A R C H   O P T I O N S |')
       print('<><><><><><><><><><><><><><><><><>')
       print('| 1. Bus No.                     |')
       print('| 2. Licence No.                 |')
       print('| 3. Date of Issuing             |')
       print('| 4. Price                       |')
       print('| 5. Bus Type                    |')
       print('| 6. Availability                |')
       print('<><><><><><><><><><><><><><><><><>\n')
       ch=int(input('Search Option : '))
       sql=''
       if ch==1:
                opt3=int(input('OK ! Want to do \n1. Exact Search or \n2. Incremental Search or \n3. Search for a Series of Buses ?\n'))

                if opt3==1 :
                    busno=int(input('Bus No.: '))
                    sql='select * from bus where busno ='+str(busno)+' ;'
                    

                elif opt3==2:
                    num=int(input('Enter any digit of the Bus No. you are calling up : '))
                    sql="select * from bus where busno like '%"+str(num)+"%' ;"                   

                elif opt3==3 :
                    bno1=int(input('Bus No. from where you want to start : '))
                    ask=input('Want to enter the Bus No. till which you want : [Y/N] \n')
                    if ask=='Y' or ask=='y' :
                        bno2=int(input('Enter : '))
                        sql='select * from bus where busno between '+str(bno1)+' and '+str(bno2)+' ;'
                        
                    else :
                        sql='select * from bus where busno >='+str(bno1)+' ;'
                    
       elif  ch==2 :
                opt5=int(input('OK ! Want to do \n1. Exact Search or \n2. Incremental Search ?\n'))

                if opt5==1 :
                    lno=input('Licence No. : ')
                    sql="select * from bus where licenceno ='"+str(lno)+"' ;"                           

                elif opt5==2:
                    rdl=input('Enter any character or any group of characters in correct order of the Licence No. you are calling up : ')
                    sql="select * from bus where licenceno like '%"+str(rdl)+"%' ;"

       elif  ch==3 :
                opt6=int(input('OK ! Want to do \n1. Exact Search or \n2. Incremental Search ?\n'))

                if opt6==1 :
                    doi=input('Date of Issuing (YYYY-MM-DD): ')
                    sql="select * from bus where doi ='"+str(doi)+"' ;"                           

                elif opt6==2:
                    rdd=input('Enter any character or any group of characters in correct order of the Date of Issuing you are calling up : ')
                    sql="select * from bus where doi like '%"+str(rdd)+"%' ;"
                
       elif  ch==4 :
                opt7=int(input('OK ! Want to do \n1. Exact Search or \n2. Incremental Search or \n3. Search for a Series of Buses ?\n'))

                if opt7==1 :
                    cost=int(input('Price : '))
                    sql='select * from bus where price ='+str(cost)+' ;'       

                elif opt7==2:
                    num=int(input('Enter any digit of the price you are calling up : '))
                    sql="select * from bus where price like '%"+str(num)+"%' ;"
                   
                elif opt7==3 :
                    cost1=int(input('Price from where you want to start : '))
                    ask=input('Want to enter the Price till which you want : [Y/N] \n')
                    if ask=='Y' or ask=='y' :
                        cost2=int(input('Enter : '))
                        sql='select * from bus where price between '+str(cost1)+' and '+str(cost2)+' ;'
                    else :
                        sql='select * from bus where price >='+str(cost1)+' ;'                    

       elif  ch==5 :
                opt8=int(input('OK ! Want to do \n1. Exact Search or \n2. Incremental Search ?\n'))

                if opt8==1 :
                    bt=input('Bus Type : ')
                    sql="select * from bus where bustype ='"+str(bt)+"' ;"
                    
                elif opt8==2:
                    rdbt=input('Enter any alphabet or any group of alphabets in correct order of the Bus Type you are calling up : ')
                    sql="select * from bus where bustype like '%"+str(rdbt)+"%' ;"

       elif  ch==6 :
                opt9=int(input('OK ! Want to search for \n1.Available Buses \n2. Not available buses ?\n'))

                if opt9==1 :
                    sql="select * from bus where available = 'Y' ;"

                if opt9==2 :
                    sql="select * from bus where available = 'N' ;"
                    
       Cursor.execute(sql)
       data=Cursor.fetchall()
       h=['BUSNO','LICENCENO','DOI','PRICE','BUSTYPE','DRIVER','TOURGUIDE','AVAILABLE']
       print(tb(data,headers=h,tablefmt='psql'))

#4.5.
def DelBus() :
       ask=int(input('Want to delete by \n1. Bus No. or \n2. Licence No. ?'))

       if ask==1 :
              bno=int(input('Bus No. : '))
              sql='delete from bus where busno='+str(bno)+' ;'
       elif ask==2 :
              lno=input('Licence No. : ')
              sql="delete from bus where licenceno='"+str(lno)+"' ;"

       Cursor.execute(sql)
       conn.commit()

       print('RECORD DELETED SUCCESSFULLY !!')

#5.
def Customer() :
    print('OK ! WHAT YOU WANT TO OPERATE FROM THE FOLLOWING ?')
    print('1. Add Customer')
    print('2. Show all Customer List')
    print('3. Search Customer Details')
    print('4. Delete Customer')
    print('5. Exit')

#5.1.
def AddCust() :
    fp=open('datainmysql.txt','a')
    s=input('\nSource (City) : ')
    d=input('Destination (City) : ')
    doj=input('Journey Date (YYYY-MM-DD) : ')
    board=input('Boarding (Bus Stop) : ')
    drop=input('Dropping (Bus Stop) : ')
    arrival=board.title()+', '+s.title()
    dest=drop.title()+', '+d.title()

    ch=int(input('OK! WHICH TYPE OF BUS YOU PREFER FOR TRAVEL ? \n1. Seater Bus \n2. Sleeper Bus \n3. Both in One Bus \n'))
    if ch==1 :
        print('1. 2+2 Seater Bus')
        print('2. 2+1 Seater Bus')
        opt=int(input('Enter Your Choice : '))

        if opt==1 :
            print('\n〇 〇     〇')
            print('-----  -----')
            print('03 04  01 02')
            print('07 08  05 06')
            print('11 12  09 10')
            print('15 16  13 14')
            print('19 20  17 18')
            print('23 24  21 22')
            print('27 28  25 26')
            print('31 32  29 30')
            print('35 36  33 34')
            print('39 40  37 38')
            print('43 44  41 42')
            print('47 48  45 46')
            print('51 52  49 50')
            print('55 56  53 54')
            print('-----  -----\n')

            seat_bus_1=[101,102,103,104]
            seat=54
            seatno,bno=Buses.Booking(seat_bus_1,seat)

        elif opt==2 :
            print('\n〇      〇')
            print('--   -----')
            print('03   01 02')
            print('06   04 05')
            print('09   07 08')
            print('12   10 11')
            print('15   13 14')
            print('18   16 17')
            print('21   19 20')
            print('24   22 23')
            print('27   25 26')
            print('30   28 29')
            print('33   31 32')
            print('36   34 35')
            print('39   37 38')
            print('42   40 41')
            print('--   -----\n')

            seat_bus_2=[105,106,107,108]
            seat=42
            seatno,bno=Buses.Booking(seat_bus_2,seat)

    if ch==2 :
        print('1. 2+1+1 Sleeper Bus')
        print('2. 2+1 Sleeper Bus')
        opt=int(input('Enter Your Choice : '))

        if opt==1 :
            print('\n〇 〇      〇')
            print('--  --  -----')
            print('03  04  01 02')
            print('07  08  05 06')
            print('11  12  09 10')
            print('15  16  13 14')
            print('19  20  17 18')
            print('23  24  21 22')
            print('27  28  25 26')
            print('31  32  29 30')
            print('--  --  -----')

            sleep_bus_1=[109,110,111,112]
            seat=32
            seatno,bno=Buses.Booking(sleep_bus_1,seat)

        elif opt==2 :
            print('\n〇      〇')
            print('--   -----')
            print('03   01 02')
            print('06   04 05')
            print('09   07 08')
            print('12   10 11')
            print('15   13 14')
            print('--   -----')

            sleep_bus_2=[113,114,115,116]
            seat=15
            seatno,bno=Buses.Booking(sleep_bus_2,seat)

    elif ch==3 :
       print('1. Long Bus')
       print('2. Average Bus')
       opt=int(input('Enter Your Choice : '))    
       if opt==1 :
            print('\n〇      〇')
            print('--   -----')
            print('03   01 02')
            print('06   04 05')
            print('09   07 08')
            print('12   10 11')
            print('15   13 14')
            print('18   16 17')
            print('21   19 20')
            print('24   22 23')
            print('27   25 26')
            print('30   28 29')
            print('33   31 32')
            print('36   34 35')
            print('39   37 38')
            print('42   40 41')
            print('--   -----')
        
            sleep_seat_bus_1=[117,118,119,120]
            seat=42
            seatno,bno=Buses.Booking(sleep_seat_bus_1,seat)

       elif opt==2 :
            print('\n〇      〇')
            print('--   -----')
            print('03   01 02')
            print('06   04 05')
            print('09   07 08')
            print('12   10 11')
            print('15   13 14')
            print('18   16 17')
            print('21   19 20')
            print('24   22 23')
            print('27   25 26')
            print('30   28 29')
            print('--   -----')
        
            sleep_seat_bus_2=[121,122,123,124]
            seat=30
            seatno,bno=Buses.Booking(sleep_seat_bus_2,seat)

    print('Your bus number is',bno)
    print('Your seat number is',seatno)

    payment=Buses.Payment(arrival,dest,ch,opt)
    print('Your seat costs Rs.',payment)

    print('\nCONTACT INFORMATION')
    print('-------------------')
    pno=int(input('Phone No.: '))
    while len(str(pno)) != 10 :
        print('Wrong Input !!')
        pno=int(input('Phone No. : '))
        
    print('\nPASSENGER INFORMATION')
    print('---------------------')
    name=input('Name : ')
    gen=input('Gender : \n1. Male   2.Female\n')
    if gen==1 :
        gen='M'
    elif gen==2 :
        gen='F'
    age=int(input('Age : '))

    sql="insert into customer values (NULL, '"+str(name.title())+"', '"+str(gen.title())+"', "+str(age)+", '"+str(arrival)+"', '"+str(dest)+"', "+str(payment)+", "+str(bno)+", "+str(seatno)+", '"+str(pno)+"', '"+str(doj)+"');"
    Cursor.execute(sql)
    fp.write(sql+'\n')
    print('RECORD SAVED SUCCESSFULLY !!')
    conn.commit()
    fp.close()

#5.2.
def ShowCust():
       sql='select * from customer;'
       Cursor.execute(sql)
       data=Cursor.fetchall()
       h=['CUSTID','CNAME','GENDER','AGE','ARRIVAL','DESTINATION','PAYMENT','BUSNO','SEATNO','PHONENO','DOT']
       print(tb(data,headers=h,tablefmt='psql'))
       sql='select count(*) from customer;'
       Cursor.execute(sql)
       data=Cursor.fetchall()
       print('Number of Datas :',data[0][0])

#5.3.
def SearchCust() :
       print('\n<><><><><><><><><><><><><><><><><>')
       print('| 三 S E A R C H   O P T I O N S |')
       print('<><><><><><><><><><><><><><><><><>')
       print('| 1. Customer Name               |')
       print('| 2. Gender                      |')
       print('| 3. Age                         |')
       print('| 4. Source                      |')
       print('| 5. Destination                 |')
       print('| 6. Payment                     |')
       print('| 7. Bus Number                  |')
       print('| 8. Seat Number                 |')
       print('| 9. Phone Number                |')
       print('| 10.Date of Travelling          |')
       print('<><><><><><><><><><><><><><><><><>')
       ch=int(input('\nSearch Option : '))

       sql=''

       if ch==1:
                opt3=int(input('OK ! Want to do \n1. Exact Search or \n2. Incremental Search ?\n'))

                if opt3==1 :
                    cname=input('Customer Name :')
                    sql="select * from customer where cname ='"+str(cname.title())+"' ;"
                    
                elif opt3==2:
                    rdn=input('Enter any alphabet or any group of alphabets in correct order of the Customer Name you are calling up :\n')
                    sql="select * from customer where cname like '%"+str(rdn)+"%' ;"

       elif ch==2:
              opt4=int(input('OK ! Choose one from the following to search :  \n1. Male or \n2. Female\n'))

              if opt4==1 :
                     sql="select * from customer where gender = 'M';"
              elif opt4==2 :
                     sql="select * from customer where gender = 'F';"


       elif ch==3:
                opt5=int(input('OK ! Want to do \n1. Exact Search or \n2. Search for a Series of Customers ?\n'))

                if opt5==1 :
                    age=int(input('Age: '))
                    sql='select * from customer where age ='+str(age)+' ;'

                elif opt5==2 :
                    age1=int(input('Age from where you want to start : '))
                    ask=input('Want to enter the age till which you want : [Y/N] \n')
                    if ask=='Y' or ask=='y' :
                        age2=int(input('Enter :'))
                        sql='select * from customer where age between '+str(age1)+' and '+str(age2)+' ;'
                    else :
                        sql='select * from customer where age >='+str(age1)+' ;'    

       elif  ch==4 :
                opt6=int(input('OK ! Want to do \n1. Exact Search or \n2. Incremental Search ?\n'))

                if opt6==1 :
                    source=input('Source : ')
                    sql="select * from customer where arrival ='"+str(source.title())+"' ;"

                elif opt6==2:
                    rds=input('Enter any alphabet or any group of alphabets in correct order of the Source you are calling up : ')
                    sql="select * from customer where arrival like '%"+str(rds)+"%' ;"

       elif  ch==5 :
                opt7=int(input('OK ! Want to do \n1. Exact Search or \n2. Incremental Search ?\n'))

                if opt7==1 :
                    dest=input('Destination : ')
                    sql="select * from customer where destination ='"+str(dest.title())+"' ;"

                elif opt7==2:
                    rdd=input('Enter any alphabet or any group of alphabets in correct order of the Destination you are calling up : ')
                    sql="select * from customer where destination like '%"+str(rdd)+"%' ;"

       elif  ch==6 :
                opt8=int(input('OK ! Want to do \n1. Exact Search or \n2. Search for a Series of Customers ?\n'))

                if opt8==1 :
                    pay=float(input('Payment made by that Customer : '))
                    sql='select * from customer where payment ='+str(pay)+' ;'

                elif opt8==2 :
                    pay1=float(input('Amount of Payment from where you want to start : '))
                    ask=input('Want to enter the Amount of Commission till which you want : [Y/N] \n')
                    if ask=='Y' or ask=='y' :
                           pay2=float(input('Enter :'))
                           sql='select * from customer where payment between '+str(pay1)+' and '+str(pay2)+' ;'
                    else :
                           sql='select * from customer where payment >='+str(pay1)+' ;'

       elif ch==7 :
                opt9=int(input('OK ! Want to do \n1. Exact Search or \n2. Search for a Series of Customers ?\n'))

                if opt9==1 :
                    bno=int(input('Bus Number : '))
                    sql='select * from customer where busno ='+str(bno)+' ;'

                elif opt9==2 :
                    bno1=int(input('Bus Number from where you want to start : '))
                    ask=input('Want to enter the Bus Number till which you want : [Y/N] \n')
                    if ask=='Y' or ask=='y' :
                        bno2=int(input('Enter :'))
                        sql='select * from customer where busno between '+str(bno1)+' and '+str(bno2)+' ;'
                    else :
                        sql='select * from customer where busno >='+str(bno1)+' ;'

       elif ch==8 :
                opt10=int(input('OK ! Want to do \n1. Exact Search or \n2. Search for a Series of Customers ?\n'))

                if opt10==1 :
                    sno=int(input('Seat Number : '))
                    sql='select * from customer where seatno ='+str(sno)+' ;'

                elif opt10==2 :
                    sno1=int(input('Seat Number from where you want to start : '))
                    ask=input('Want to enter the Seat Number till which you want : [Y/N] \n')
                    if ask=='Y' or ask=='y' :
                        sno2=int(input('Enter :'))
                        sql='select * from customer where seatno between '+str(sno1)+' and '+str(sno2)+' ;'
                    else :
                        sql='select * from customer where seatno >='+str(sno1)+' ;'

       elif  ch==9 :
                opt11=int(input('OK ! Want to do \n1. Exact Search or \n2. Incremental Search ?\n'))

                if opt11==1 :
                    pno=input('Phone No. :')
                    sql="select * from customer where phoneno ='"+str(pno)+"' ;"
                    

                elif opt11==2:
                    rdpn=input('Enter any alphabet or any group of alphabets in correct order you are calling up : ')
                    sql="select * from customer where phoneno like '%"+str(rdpn)+"%' ;"

       elif  ch==10 :
                opt12=int(input('OK ! Want to do \n1. Exact Search or \n2. Incremental Search ?\n'))

                if opt12==1 :
                    dot=input('Date of Travelling (YYYY-MM-DD): ')
                    sql="select * from customer where dot ='"+str(dot)+"' ;"                           

                elif opt12==2:
                    rdd=input('Enter any character or any group of characters in correct order of the Date of Travelling you are calling up : ')
                    sql="select * from customer where dot like '%"+str(rdd)+"%' ;"
                    
       Cursor.execute(sql)
       data=Cursor.fetchall()
       h=['CUSTID','CNAME','GENDER','AGE','ARRIVAL','DESTINATION','PAYMENT','BUSNO','SEATNO','PHONENO','DOT']
       print(tb(data,headers=h,tablefmt='psql'))

#5.4.
def DelCust() :
       ask=int(input('Want to delete by \n1.Name or \n2. Customer ID ?\n'))
       if ask==1 :
              name=input("Customer Name : ")
              sql="delete from customer where cname='"+str(name)+"' ;"
       elif ask==2 :
              cid=int(input('Customer ID : '))
              sql='delete from customer where cid='+str(cid)+' ;'

       Cursor.execute(sql)
       conn.commit()

       print('RECORD DELETED SUCCESSFULLY !!')
