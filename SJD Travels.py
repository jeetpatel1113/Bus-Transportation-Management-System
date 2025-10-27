#----------------------
# Shri Jeet Das Travels
#----------------------
import Admin
import datetime as d
import pymysql
from tabulate import tabulate as tb
conn=pymysql.connect(host='localhost',user='root',passwd='root',db='sjd')
Cursor=conn.cursor()
print()
print('\t\t\t\t\t\t           WELCOME')
print('\t\t\t\t\t\t              to')
print('\t\t\t\t\t\t  SHRI JEET DAS Travels Care')
print('\t\t\t\t\t\t ----------------------------')
print()

Ask=int(input('WHO ARE YOU FROM THE FOLLOWING ?\n1.Admin\t\t2.User\n'))
if Ask==1 :
  pass
elif Ask==2 :
  Admin.AddCust()

Admin.password()
while True :
  Admin.MainMenu()

  opt1=int(input("\nENTER YOUR CHOICE : "))

  if opt1==1 :
    while True :
      Admin.Employee()
    
      opt2=int(input())
        
      if opt2==1 :
        while True :
          Admin.AddEmp()
          ask=input('\nDo you want to enter more records ? (Y/N):')
          if ask=='n' or ask=='N' :
            break

      elif opt2==2 :
        while True :
          Admin.UpdateEmp()
          ask=input('\nWant to Continue with Updating (Y/N):')
          if ask=='n' or ask=='N' :
            break
             
      elif opt2==3 :
        Admin.ShowEmp()

      elif opt2==4 :
        while True :
          Admin.SearchEmp()
          ask=input('\nWant to search more records ? (Y/N):')
          if ask=='n' or ask=='N' :
            break
         
      elif opt2==5 :
        while True :
          Admin.DelEmp()
          ask=input('\nWant to delete more records ? (Y/N):')
          if ask=='n' or ask=='N' :
            break

      elif opt2==6 :
        break

  elif opt1==2 :
    while True :
      Admin.Bus()

      opt2=int(input())
        
      if opt2==1 :
        while True :
          Admin.AddBus()
          ask=input('\nDo you want to enter more records ? (Y/N):')
          if ask=='n' or ask=='N' :
            break

      elif opt2==2 :
        while True :
          Admin.UpdateBus()
          ask=input('\nWant to Continue with Updating (Y/N):')
          if ask=='n' or ask=='N' :
            break

      elif opt2==3 :
        Admin.ShowBus()

      elif opt2==4 :
        while True :
          Admin.SearchBus()
          ask=input('\nWant to search more records ? (Y/N):')
          if ask=='n' or ask=='N' :
            break
                           
      elif opt2==5 :
        while True :
          Admin.DelBus()
          ask=input('\nWant to delete more records ? (Y/N):')
          if ask=='n' or ask=='N' :
            break

      elif opt2==6 :
        break

  
  elif opt1==3 :
    while True :
      Admin.Customer()
    
      opt2=int(input())
        
      if opt2==1 :
        while True :
          Admin.AddCust()
          ask=input('\nDo you want to enter more records ? (Y/N):')
          if ask=='n' or ask=='N' :
              break
                      
      elif opt2==2 :
        Admin.ShowCust()             

      elif opt2==3 :
        while True : 
          Admin.SearchCust()
          ask=input('\nWant to search more records ? (Y/N):')
          if ask=='n' or ask=='N' :
            break
            
      elif opt2==4 :
        while True :
          Admin.DelCust()
          ask=input('\nWant to delete more records ? (Y/N):')
          if ask=='n' or ask=='N' :
            break

      elif opt2==5 :
        break

  elif opt1==4 :
    while True :
      print (" ============================================")
      print ("|             R E P O R T  M E N U           |")
      print ("|--------------------------------------------|")
      print ("| 1 - > Bus Registered                       |")
      print ("| 2 - > Customer Registered                  |")
      print ("| 3 - > Employee Working                     |")
##      print ("| 4 - > Temporarily Deleted Buses            |")
##      print ("| 5 - > Temporarily Deleted Employees        |")
##      print ("| 6 - > Temporarily Deleted Customers        |")
      print ("| 4 - > Exit                                 |")
      print (" ============================================")
      ch = input ("Enter your choice : ")
      if ch == '1' :
        print('\nBus Registered Report')
        Admin.ShowBus()
      elif ch == '2' :
        print('\nCustomer Registered Report')
        Admin.ShowCust()
      elif ch == '3' :
        print('\nEmployees Working Report')
        Admin.ShowEmp()
##      elif ch == '4' :
##        print()
##      elif ch == '5' :
##                                Deleted_Members()
##      elif ch == '6' :
##                                IFile1 = "Missue.dat"
##                                print ("\nMemberwise issued Register")
##                                TMno = input ("Enter member no.: ").upper()
##                                Memberwise_Issue(IFile1, TMno)
      elif ch == '4' :
                               break

  elif opt1==5 :
    print()
    fp=open('datainmysql.txt')
    s=fp.read()
    print(s)
    fp.close()

  elif opt1==6 :
    print()
    fp1=open('instructions.txt')
    s=fp1.read()
    print(s)
    fp1.close()

  elif opt1==7 :
    break
         
conn.close()
Cursor.close()
