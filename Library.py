import sys
import mysql.connector as conec
import pyttsx3
import time


voice = pyttsx3.init()
voices = voice.getProperty('voices')
voice.setProperty('voice', voices[1].id)
newVoiceRate = 155
voice.setProperty('rate',newVoiceRate)


mycon = conec.connect(host = 'localhost',user = 'root',password = 'answer123',database = 'hbedi')
if mycon.is_connected() == False:
    print("Error connecting in My Sql Database!")
cursor = mycon.cursor()
cursor.execute("Select * from Library")
result = cursor.fetchall()
mycon.commit()


          
class Library():
    def __init__(self,result):
        self.availablebooks = result
        self.name = ""
        self.Clas = 0
        self.section = ""
        self.days = 0

    def displayavailablebooks(self):
        voice.say("The books we have in Library are:")
        voice.runAndWait()
        print("The books we have in Library are:")
        for books in self.availablebooks:
            print(books)
    
    def lendbook(self):
                #table name - info and library
        voice.say("Please enter your name")
        voice.runAndWait()
        self.name=input("Please enter your name")
        
        voice.say("Please enter your class")
        voice.runAndWait()
        bridge_class = True
        while bridge_class:
            self.clas = int(input("Enter the class :"))
            if self.clas in [1,2,3,4,5,6,7,8,9,10,11,12]:
                bridge_class = False
            else:
                print ("Please Enter proper Class")
                bridge_class = True
        
        

        voice.say("Please enter your section")
        voice.runAndWait()
        """Method to Check Section and take input"""
        
        bridge_sec = True
        while bridge_sec:
            self.section = input("Enter the section:").lower()
            if self.section not in ["a","b","c","d","e","f","g","h","i","j","k"]:
                print ("Please Enter proper Section")
                bridge_sec = True
            else:
                bridge_sec = False

        voice.say("Enter for how many days you want to borrow")
        voice.runAndWait()

        bridge_day = True
        while bridge_day:
            self.days = int(input("Enter for how many days you want to borrow"))
            if self.days >= 30 or self.days==69:
                print("You can't borrow for more than 30 days!")
                print("Please Enter proper number of days")
                bridge_day = True
            else:
                bridge_day = False
        


        voice.say("Enter the name of the book you want to borrow: ")
        voice.runAndWait()
        self.book = input("Enter the name of the book you want to borrow: ")
        list1 = []
        list2=[]
        for i in self.availablebooks:
            for x in i:
                list1.append(x)
        


        print(list1)
        print(list2)
        
        if self.book in list1:
            mycursor = mycon.cursor()
            sql = "delete from Library where BookName = %s"
            mycursor.execute(sql,(self.book,))
            mycon.commit()

            mycursor1= mycon.cursor()
            sql1 = "insert into info(name,class,section,duration,book) values(%s,%s,%s,%s,%s)"
            val1 =(self.name,self.clas,self.section,self.days,self.book)
            mycursor1.execute(sql1,val1)
            mycon.commit()
            
            voice.say("You have borrowed it.")
            print("You have borrowed it.")

        else:
            voice.say("Sorry, this book is not available in the Library at the moment.")
            print("Sorry, this book is not available in the Library at the moment.")

    
        voice.runAndWait()


    def returnbook(self):
        voice.say("Enter the name of the book you want to return.")
        voice.runAndWait()
        print("Enter the name of the book you want to return.")
        
        count = 0
        for i in self.availablebooks:
            count += 1
            count = count + 1    
            self.book = input()
            mycursor = mycon.cursor()
            sql = "insert into Library(Sno,BookName) values(%s,%s)"
            val = (count,self.book)
            mycursor.execute(sql,val)
            mycon.commit()
            return self.book
            voice.say("saxasfully returned")
            voice.runAndWait()
            print("saxasfully returned")

    def borrow(self):
        print("The users who have borrowed the Books are as follows:- ")
        mycon = conec.connect(host = 'localhost',user = 'root',password = 'answer123',database = 'hbedi')
        cursor2 = mycon.cursor()
        cursor2.execute("Select * from info")
        result1 = cursor2.fetchall()
        mycon.commit()

        for borrows in result1:
            print(borrows)

    def del_book(self):
        self.book1 = input("Enter the book you want to remove: ")
        list1 = []
        for i in self.availablebooks:
            for x in i:
                list1.append(x)
        


        print(list1)
        if self.book1 in list1:
            mycursor = mycon.cursor()
            sql = "delete from Library where BookName = %s"
            mycursor.execute(sql,(self.book1,))
            mycon.commit()

    def new_book(self):
        voice.say("Enter the serial number and the name of the book you want to Add: ")
        voice.runAndWait()
        self.sno = int(input("Enter the serial number: "))
        self.book1 = input("Enter the name of the book you want to Add: ")
        mycursor = mycon.cursor()
        sql = "insert into Library(Sno,BookName) Values(%s,%s)"
        val = (self.sno,self.book1)
        mycursor.execute(sql,val)
        mycon.commit()
        voice.say("New Book added Successfully!")
        voice.runAndWait()
        print("New Book added Successfully!")
        

        
            
    
def main():



    
    while True:
        voice.say ("enter 1 for admin      enter 2 for user        enter 3 to exit ")
        voice.runAndWait()
        print("enter 1 for admin \nenter 2 for user\nenter 3 to exit")
        
        user_adm=int(input("Please enter your choice : "))
        if user_adm==1:
            voice.say("enter your username")
            voice.runAndWait()
            user=input("enter your username")
            voice.say("enter your password")
            voice.runAndWait()
            passw=input("enter your password")
            if user=='GameOnSpotYt' and passw=='onspot':
                 voice.say("you are on user - GameOnSpotYt")
                 voice.runAndWait()
                 print("you are on user - GameOnSpot")


                 voice.say("Welcome To Our Library!")
                 voice.runAndWait()
                 library = Library(result)
           
                 print ("_"*80)
                 print ("-"*80)
                 print ("\t \t \t \t=======LIBRARY MENU=======")
                 print("""
1. Display all available books
2. To check the borrowers
3. To add new books
4. To delete books 
5. Exit
              """)
                 choice = int(input("Enter your choice:"))
                 while True:
                     if choice == 1:
                         library.displayavailablebooks()
                         choice = int(input("Enter your choice:"))
                     
                     elif choice == 2:
                         library.borrow()
                         choice = int(input("Enter your choice:"))
                     elif choice==3:
                        library.new_book()
                        choice = int(input("Enter your choice:")) 



                         
                     elif choice == 4:
                         library.del_book()
                         chice= int(input("Enter your choice"))

                     
                         
                     elif choice == 5:
                         break

            else:
                 voice.say("please enter a valid username or password")
                 voice.runAndWait()
                 print("please enter a valid username or password")
        elif user_adm==2:
                voice.say("Welcome To Our Library!")
                voice.runAndWait()
                library = Library(result)
           
                print ("_"*300)
                print ("-"*300)
                print ("\t \t \t \t =======LIBRARY MENU=======")
                print("""
1. Display all available books
2. Request a book
3. To check the borrowers
4. Exit
              """)
                choice = int(input("Enter your choice:"))
                while True:
                    if choice == 1:
                        library.displayavailablebooks()
                        
                        print("""
1. Display all available books
2. Request a book
3. To check the borrowers
4. Exit
              """)
                        choice = int(input("Enter your choice:"))
                    elif choice == 2:
                        library.lendbook()
                        
                        print("""
1. Display all available books
2. Request a book
3. To check the borrowers
4. Exit
              """)
                        choice = int(input("Enter your choice:"))
                    elif choice == 3:
                        library.borrow()
                        
                        print("""
1. Display all available books
2. Request a book
3. To check the borrowers
4. Exit
              """)
                        choice = int(input("Enter your choice:"))
                    elif choice == 4:
                        break



        elif user_adm==3:
            voice.say("hi visits"*10)
            voice.runAndWait()
            print("\t \t \t \t \t____Terminatingggg____"*100)
            break


main()

    
