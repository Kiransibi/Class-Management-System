import os
import csv
import time
import getpass
sub=('English','Mathematics','Chemistry','Physics','Computer science')
class student:
    def __init__ (self):
            self.adno=0
            self.name="null"
            self.m = [0,0,0,0,0]
            self.total=0
	    self.grade="n"
    def inp(self):
             print "\n\n\tENTER THE DETAILS:\n"
             self.adno=input("\tENTER THE APPLICATION NUMBER   :")
             self.name=raw_input("\tENTER NAME                     :")
             print "\n\t\t\t  ENTER THE MARKS   "
             print "\n\t\t\t********************MARKS**************************"
             self.m[0]=input("\t\t\tENGLISH         : ")
             self.m[1]=input("\t\t\tMATHEMATICS     : ")
             self.m[2]=input("\t\t\tCHEMISTRY       : ")
             self.m[3]=input("\t\t\tPHYSICS         : ")
             self.m[4]=input("\t\t\tCOMPUTER SCIENCE: ")
	     self.total=self.m[0]+self.m[1]+self.m[2]+self.m[3]+self.m[4]
	     self.grade=gradecal(self.total)
    def out(self):
            print "\n\t\t\tADMISSION NUMBER:%d\n\t\t\tNAME :%s\n"  %(self.adno,self.name)
            print "\n\t\t\t\tMARKS \n"
	    print "\t\t\t****************************"
            for i in range(0,4):
               print "\t\t\t\t%s : %d\n" %(sub[i],self.m[i])
	    print "\n\n\t\t\t\tTOTAL :",self.total   
            print "\n\n\t\t\t\tGRADE :",self.grade
			   
    def infile(self):        
      with open('student.csv', 'a') as ipt:
         iptWriter = csv.writer(ipt)
         iptWriter.writerow([self.adno,self.name,self.m[0],self.m[1],self.m[2],self.m[3],self.m[4],self.total,self.grade])
      ipt.close()
#end of class student	  
	  
	  
	  
def marklist(a):
    print "\n\n\t\t\tADNO\t\t:",a[0]
    print "\t\t\tNAME\t\t:",a[1]
    print "\t\t**********************************************"
    print "\t\t\tENGLISH\t\t:",a[2]
    print "\t\t\tMATHEMATICS\t:",a[3]
    print "\t\t\tCHEMISTRY\t:",a[4]
    print "\t\t\tPHYSICS\t\t:",a[5]
    print "\t\t\tCOMPUTER SCIENCE:",a[6]
    print "\t\t\tTOTAL\t\t:",a[7]
    print "\t\t\tGRADE\t\t:",a[8]
    raw_input("\n\t\tENTER ANY KEY...") 
    


def classlist(a):
    print "\n\tADNO:",a[0],"\tNAME :",a[1],"_____________________________________________________________________________________________________________"
    print "\tENGLISH: ",a[2],"\tMATHEMATICS: ",a[3],"\tCHEMISTRY :",a[4],"\tPHYSICS :",a[5],"\tCOMPUTER SCIENCE :",a[6],"\tTOTAL :",a[7],"\tGRADE :",a[8]
     
	


def gradecal(x):
         if (x>=451 and x<=500):
                 return "A+"
         elif(x>=401 and x<=450):
                 return "A"
         elif(x>=351 and x<=400):
                 return "B+"                         
         elif(x>=301 and x<=350):
                 return "B"
         elif(x>=251 and x<=300):
                 return "C+"
         elif(x>=200 and x<=250):
                 return "C"
         else:
                return "F" 
def searchbyadno():
   ad=input("\n\t\tENTER THE ADMISSION NUMBER:")
   with open('student.csv', 'r') as ipt:
         iptReader=csv.reader(ipt)
         for row in iptReader:
             if len(row)!=0:
	               if row[0]==str(ad):
                             print "\n\n\t\t\t\tREPORT CARD"
			     marklist(row)	
def inpclasslist():
    os.system("cls")
    with open('student.csv', 'r') as ipt:
         iptReader=csv.reader(ipt)
	 print "\n\n\t\t\t\tCLASS REPORT CARD"
         for row in iptReader:
             if len(row)!=0:
	                classlist(row)	
def ranklist():
    os.system("cls")
    sl=[]
    A=[]
    with open('student.csv', 'r') as ipt:
         iptReader=csv.reader(ipt)
     		 
	 print "\n\n\t\t\t\tRANK LIST"
         for row in iptReader:
             if len(row)!=0:
                 sl=sl+[row]	
    A=sorted(sl,key=lambda x:int(x[7]),reverse=True)	
    for i in range(len(A)):
        classlist(A[i])
    raw_input("\n\n\t\t\t\tENTER ANY KEY ......")
def thank():
      os.system("cls")
      print "\n\n\n\n\n\tWE SHOW OUR SINCERE GRATITUDE" 
      time.sleep(1)
      print "\n\n\n\t\t\t\tTOWARDS  ALL OUR FRIENDS "
      time.sleep(1)
      print "\n\n\n\t\t\t\t\t\t\tIN SUPPORTING US THROUGH  THIS  VENTURE"
      time.sleep(3)
      os.system("cls")
      print "\n\n\n\n\n\n\n\t\t  WE  SPECIALLY  THANK  NIYA  MAA'M , "
      time.sleep(1)
      print "\n\n\n\n\t\t\t\t JAYAKRISHNA SIR"
      time.sleep(1)
      print "\n\n\n\t\t\t\t\tAND"
      time.sleep(1)
      print "\n\n\n\n\t\t\t\t\t ANSAMOL MAA'M  FOR  SUPPORTING  US"
      time.sleep(2)
      os.system("cls")
      time.sleep(0.3)
      print "\n\n\n"
      print"	        _/_/_/_/_/  _/                            _/            \n"
      time.sleep(0.3)
      print"	           _/      _/_/_/      _/_/_/  _/_/_/    _/  _/        \n"
      time.sleep(0.3)
      print"	           _/      _/    _/  _/    _/  _/    _/  _/_/           \n"
      time.sleep(0.3)
      print"	          _/      _/    _/  _/    _/  _/    _/  _/  _/          \n"
      time.sleep(0.3)
      print"	         _/      _/    _/    _/_/_/  _/    _/  _/    _/        \n"
      time.sleep(0.3)
      print" \n\n\n";	
      time.sleep(0.3)
      print"		         _/     _/                                       \n"          
      time.sleep(0.3)
      print"		          _/  _/    _/_/    _/    _/                     \n"
      time.sleep(0.3)
      print"		            _/    _/    _/  _/    _/                     \n"
      time.sleep(0.3)
      print"		            _/    _/    _/  _/    _/                     \n"
      time.sleep(0.3)
      print"		           _/      _/_/      _/_/_/                     "
      time.sleep(5)
	  
							 
						   


s=student()
for i in range(20):
 os.system("cls") 
 print "\n\t*************************************************************************\n"
 print "\t.................WELCOME TO LEKHYAM SCHOOL MANAGEMENT SYSTEM............."
 print "\n\t*************************************************************************\n\n"
 print "\t_________________________________________________________________________\n "
 print "\t\t\t\tLOGIN  MENU \n"
 print "\t_________________________________________________________________________\n "
 print "\n\n\t\t\t\t1:TEACHER LOGIN\n\t\t\t\t2:ADMIN LOGIN\n\t\t\t\t0:EXIT"
 ch=input("\n\t\t\t\tENTER YOUR CHOICE: ")
 if ch ==1:
   os.system("cls")
   print "\n\n\t*************************************************************************\n"
   print "\t..............................TEACHER LOGIN.............................."
   print "\n\t*************************************************************************\n\n"
   password=getpass.getpass("\n\n\n\t\t\t\t\tENTER THE PASSWORD  :")
   if password=="teacher":
    print "\n\n\n\n\t\t\t\t\tLOGIN SUCCESSFULL"
    time.sleep(1)
    for j in range(20):
     os.system("cls")
     print "\n\t*************************************************************************\n"
     print "\t..............................TEACHER LOGIN.............................."
     print "\n\t*************************************************************************\n\n"
     print "\t_______________________________________________________________________\n "
     print "\t\t\t\t\tMENU \n"
     print "\t_______________________________________________________________________\n "
     print "\n\t\t\tPlease select an option:"
     print "\n\n\t\t\t\t1.ENTRY\n\n\t\t\t\t2.VIEW STUDENT\n\n"
     print "\t\t\t\t3.VIEW CLASS \n\n\t\t\t\t4:RANKLIST\n\n\t\t\t\t0.Exit\n\n\t\t\t\t"
     ch=input("\n\n\t\t\t\tENTER YOUR CHOICE: ")
     if ch==1:
        os.system("cls")
        print "\n\t*************************************************************************\n"
        print   "\t..................................ENTRY.................................."
        print "\n\t*************************************************************************\n\n\n"
        s.inp()
        time.sleep(1)
        os.system("cls")
        print "\n\n\t\t\tENTERED  DETAILS"
        s.out()
        raw_input("\n\n\t\t\t\tENTER ANY KEY ......")
        s.infile()
     elif ch==2:
        os.system("cls")
        print "\n\t**************************************************************************\n"
        print  "\t...............................VIEW STUDENT..............................."
        print "\n\t**************************************************************************\n\n"
        print "\t\t______________________________________________________________________\n "
        print "\t\t______________________________________________________________________\n "
        searchbyadno()
     elif ch==3:
        os.system("cls")
        print "\n\t**************************************************************************\n"
        print  "\t...............................VIEW CLASS..............................."
        print "\n\t**************************************************************************\n\n"
        print "\t\t______________________________________________________________________\n "
        print "\t\t______________________________________________________________________\n "
        inpclasslist()
	raw_input("\n\t\tENTER ANY KEY...") 
        os.system("cls")    
     elif ch==4:
       os.system("cls")
       print "\n\t**************************************************************************\n"
       print  "\t...............................RANK LIST..............................."
       print "\n\t**************************************************************************\n\n"
       ranklist()
     elif ch==0:
       thank()
       exit() 
     else:
	    print "\n\n\n\n\t\t\t\t\t\tENTER A VALID OPTION" 
   else:
      os.system("cls")
      print"\n\n\n\n\n\n\t\t\t\t\t\tINVALID PASSWORD  !  LOGIN AGAIN"
      time.sleep(1)
 elif ch ==2:
  os.system("cls")   
  print "\n\n\t*************************************************************************\n"
  print "\t..............................ADMIN LOGIN.............................."
  print "\n\t*************************************************************************\n\n"
  password=getpass.getpass("\n\n\n\t\t\t\t\tENTER THE PASSWORD  :")
  if password=="admin":
    print "\n\n\n\n\t\t\t\t\tLOGIN SUCCESSFULL"
    time.sleep(1)
    for j in range(20):
     os.system("cls")
     print "\n\t*************************************************************************\n"
     print "\t...............................ADMIN LOGIN..............................."
     print "\n\t*************************************************************************\n\n"
     print "\t______________________________________________________________________\n "
     print "\t\t\t\t\tMENU \n"
     print "\t______________________________________________________________________\n "
     print "\n\t\t\tPlease select an option:"
     print "\n\n\t\t\t\t1.VIEW STUDENT\n\t\t\t\t2.VIEW CLASS\n\t\t\t\t3.RANK LIST\n\t\t\t\t0.Exit\n\n\t\t\t\t"
     ch=input("\n\n\t\t\t\tENTER YOUR CHOICE: ")
     if ch==1:
        os.system("cls")
        print "\n\t**************************************************************************\n"
        print  "\t...............................VIEW STUDENT..............................."
        print "\n\t**************************************************************************\n\n"
        print "\t______________________________________________________________________\n "
        print "\t______________________________________________________________________\n "
        searchbyadno()
        raw_input("\n\t\t\tENTER ANY KEY.....")
        os.system("cls")
     elif ch==2:
        os.system("cls")
        print "\n\t**************************************************************************\n"
        print  "\t...............................VIEW CLASS..............................."
        print "\n\t**************************************************************************\n\n"
        print "\t\t______________________________________________________________________\n "
        print "\t\t______________________________________________________________________\n "
        inpclasslist()
	raw_input("\n\t\tENTER ANY KEY...") 
     elif ch==3:
       os.system("cls")
       print "\n\t**************************************************************************\n"
       print  "\t...............................RANK LIST..............................."
       print "\n\t**************************************************************************\n\n"
       ranklist()   
     elif ch==0:
       thank()
       exit()
     else:
	    print "ENTER A VALID OPTION"  
  else:
      os.system("cls")
      print"\n\n\n\n\n\n\t\t\t\t\t\tINVALID PASSWORD  !  LOGIN AGAIN"
      time.sleep(1)
 elif ch==0:
    thank()
    exit()
 else:
    print "\n\n\t\t\t\tENTER VALID CHOICE"
thank()
    






