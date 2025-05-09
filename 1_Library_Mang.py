import  sqlite3
import datetime

def library_mg_db_operations(q):
    con = sqlite3.connect("Library_management.db")
    con.execute(q)
    con.commit()
    con.close()

# Creating Tables using SQL Queries
def Create_all_tables():
    con = sqlite3.connect("Library_management.db")
    qrery1 = con.execute("""
                create table if not exists all_books
                (
                    book_num number(10),
                    book_name varchar(25),
                    book_author varchar(25),
                    book_publication varchar(25),
                    book_pub_date varchar(9),
                    book_price number(5)
                )
                """)
    qrery2 = con.execute("""
                create table if not exists all_student
                (
                    std_num number(10),
                    std_name varchar(25),
                    std_class varchar(25),
                    std_mob number(10),
                    std_email varchar(25)
                )
                """)
    qrery3 = con.execute("""
                create table if not exists all_book_issued
                (
                    enr_num number(10),
                    book_num number(10),
                    std_num number(10),
                    idate varchar(9),
                    rdate varchar(9)               
                )
                """)
    library_mg_db_operations(qrery1)
    print("Table : all_books created...")
    library_mg_db_operations(qrery2)
    print("Table : all_students created...")
    library_mg_db_operations(qrery3)
    print("Table : all_issued created...")
    print("All Tables Created...")

# Define the Date
def get_Date():
    tdate = datetime.date.today()
    date = str(tdate.day) + "/" + str(tdate.month) + "/" + str(tdate.year)
    return  date

# Define the Issue Book Function
def issue_book():
    # accept the details like 'book issue enrollment number,book enrollment number and student enrollment number and date
    book_enum = input("Enter Issue Enrollment Number :")
    book_num = input("Enter Book Enrollment Number :")
    std_num = int(input("Enter Student Enrollment Number :"))
    date = get_Date()
    # after the accept the details, this details save in the data base using insert query in all issued book table.
    qry = "insert into all_book_issued values ( {0}, {1},{2}, '{3}', '{4}')".format(book_enum,book_num,std_num,date,"NR")
    # calling the function and save the data
    library_mg_db_operations(qry)
    print("Book issued...")
    input()

# Define the Book Return Methon
def return_book():
    # accept the book number to  return the book and return date
    book_num = input("Enter Book Number To Return :")
    ret_date = get_Date()
    # after the accepting data , update the accepting data in the all issued book using update query.
    qry = "update all_book_issued set rdate={0} where book_num={1} and rdate='NR'".format(ret_date,book_num)
    # calling the function and update the data
    library_mg_db_operations(qry)
    print("book returned...")
    input()

# Define The Which books is not returned function
def view_not_returned_books():
   #  Connect the Data base file
   con = sqlite3.connect("Library_management.db")
   con.cursor()
   # select the data from all book issued table
   data1= con.execute("select *from all_book_issued")
   print("\n======================================================================================================================================================================================")
   print("{:<0} {:<3} {:<1} {:<3} {:<2} {:<14} {:<30} {:<4} {:<10} {:<15} {:<30} {:<2} {:<9} {:<2} {:<3} ".format("Er.No", "||", "Book ENo.", "||", "Std. ENo.", "||","Student Name", "||", "Studetn Class","||","Book Name", "||", "Issue Date", "||", "Return Date"))
   print("======================================================================================================================================================================================")
   #  for loop for achive all issued book data.
   for ls in data1:
       # check the ls[4] is equal to 'NR' if is True then it's Exicute.
       if ls[4] == "NR":
           list1 = list((ls[0], ls[1], ls[2], ls[3], ls[4]))
           #  Connect the Data base file.
           con = sqlite3.connect("Library_management.db")
           con.cursor()
           # select the data from all books table.
           data2 = con.execute("select * from all_books ")
           # for loop for achive all book data.
           for ls2 in data2:

               # check the list[1]'issued book enrollment number is equal to ls2[0]book enrollment number' if is True then it's exicute.
               if list1[1] == ls2[0]:
                   list2 = list((ls2[0], ls2[1], ls2[2]))
                   # Connect the Data base file.
                   con = sqlite3.connect("Library_management.db")
                   con.cursor()
                   # select the data from all student table
                   data3 = con.execute("select * from all_student ")
                   # for loop for achive all student data
                   for ls3 in data3:
                       list3 = list((ls3[0],ls3[1],ls3[2]))

                       # checking the list1[2]'issued student enrollment number is equal to list3[0]student enrollment number' if is True then it's exicute.
                       if list1[2]==list3[0]:
                           # Output printed...
                           print("{:<5} {:<3} {:<9} {:<3} {:<9} {:<4} {:<40} {:<4} {:<13} {:<5} {:<40} {:<3} {:<9} {:<3} {:<3} ".format(list1[0], "||", list1[1], "||", list3[0],"||", list3[1], "||", list3[2],"||", list2[1], "||", list1[3],"||", list1[4]))
   print("======================================================================================================================================================================================")

   con.commit()
   con.close()
   input()

def add_new_book():
    # accepting the data like : book enrollment number, book name, book auther name, book publication name, book publication date and book price.
    book_num = input("Enter Book Enrollment Number :")
    book_name = input("Enter Book Name :")
    book_auth = input("Enter Book Auther Name :")
    book_publ = input("Enter Book Publication Name :")
    book_pbdate = input("Enter Book Publication Date :")
    book_price = input("Enter Book Price :")
    # after the accepting data, insert the all accepting data in all boook table using insert query.
    qry = "insert into all_books values ({0}, '{1}', '{2}', '{3}', '{4}', {5})".format(book_num,book_name,book_auth,book_publ,book_pbdate,book_price)
    # calling the function and save the data.
    library_mg_db_operations(qry)
    print("New Book",book_name,"is Added...")
    input()

def search_book():
    # accept book enrollment number
    book_num = int(input("Enter Book Enrollment Number :"))
    #  Connect the Data base file
    con = sqlite3.connect("Library_management.db")
    con.cursor()
    ds = con.execute("select * from all_books ")
    print("\n---------------------------------------------------------------------------------------------------------------------------------------------")
    print("{:<5} {:<3} {:30} {:<2} {:<28} {:<2} {:<25} {:<2} {:<15} {:<2} {:<10} ".format("Book No.", "||", "Book Name","||", "Book Auther Name","||", "Book Publication.","||", "Book Pub. Date", "||","Book Price"))
    print("=============================================================================================================================================")
    # for loop for achive the all books data.
    for ls in ds:
        # checking the 'ls[0] book enrollment number is equal to user accept book enrollment number' if is True then is't execute.
        if ls[0] == book_num:
            # print the output the search book information.
            print("{:<8} {:<3} {:30} {:<2} {:<28} {:<2} {:<25} {:<2} {:<15} {:<2} {:<1} {:<1}".format(ls[0], "||", ls[1],"||", ls[2], "||",ls[3], "||", ls[4],"||", ls[5], "$"))
    print("---------------------------------------------------------------------------------------------------------------------------------------------")
    con.commit()
    con.close()
    input()

def book_history():
    #  Connect the Data base file
    con = sqlite3.connect("Library_management.db")
    con.cursor()
    ds = con.execute("select * from all_books ")
    print("\n===================================================================================================================================================")
    print("{:<5} {:<3} {:30} {:<2} {:<28} {:<2} {:<25} {:<2} {:<15} {:<2} {:<10} ".format("Book No.","||","Book Name","||","Book Auther Name", "||", "Book Publication.","||", "Book Pub. Date","||", "Book Price"))
    print("===================================================================================================================================================")
    # for loop for achive the all books data.
    for ls in ds:
        # print the all books data in screen output.
        print("{:<8} {:<3} {:30} {:<2} {:<28} {:<2} {:<25} {:<2} {:<15} {:<2} {:<1} {:<1}".format(ls[0], "||", ls[1], "||", ls[2], "||", ls[3], "||", ls[4], "||", ls[5], "$"))
    print("===================================================================================================================================================")

    con.commit()
    con.close()
    input()

def add_new_student():
    # accepting the details like : student enrollment number,student name,student class name,student mobile number and student email id.
    stdNum = input("Enter Student Enrollment Number :")
    stdName = input("Enter Student Name :")
    stdClass = input("Enter Student Class Name :")
    stdMob = input("Enter Student Mo.Number :")
    stdEmail = input("Enter Student Email ID :")
    # after the accepting data, the data is save the all student table using insert query.
    qry = "insert into all_student values({0}, '{1}', '{2}', {3}, '{4}')".format(stdNum,stdName,stdClass,stdMob,stdEmail)
    # calling the function and save the data.
    library_mg_db_operations(qry)
    print("New Student",stdName,"is added Sucessfull...")
    input()

def search_student():
    # accept the student enrollment number.
    std_num = input("Enter Student Enrollment Number :")
    #  Connect the Data base file
    con = sqlite3.connect("Library_management.db")
    con.cursor()
    ds = con.execute("select * from all_student ")
    print("\n-------------------------------------------------------------------------------------------")

    print("{:<0} {:<3} {:<25} {:<2} {:<10} {:<2} {:<10} {:<2} {:<2} ".format("Er.No", "||", "Name", "||", "Class", "||","Mo.No.", "||", "Email Id."))
    print("-------------------------------------------------------------------------------------------")
    # for loop for achive the all student table data.
    for ls in ds:
        # checking the 'ls[0] student enrollment number is equal to user accepting student enrollment number' if is True then it's execute.
        if ls[0] == int(std_num):
            # print the search student information.
            print("{:<5} {:<3} {:<25} {:<2} {:<10} {:<2} {:<10} {:<2} {:<0}".format(ls[0], "||", ls[1], "||", ls[2], "||", ls[3], "||", ls[4]))
            print("-------------------------------------------------------------------------------------------")
    con.commit()
    con.close()
    input()

def student_history():
    #  Connect the Data base file
    con = sqlite3.connect("Library_management.db")
    con.cursor()
    ds = con.execute("select * from all_student ")

    print("\n============================================================================================")
    print("{:<0} {:<3} {:<25} {:<2} {:<10} {:<2} {:<10} {:<2} {:<2} ".format("Er.No","||","Name","||","Class", "||", "Mo.No.","||", "Email Id."))
    print("============================================================================================")
    # for loop for achive the all student data.
    for ls in ds:
            # print the all student data in screen output.
            print("{:<5} {:<3} {:<25} {:<2} {:<10} {:<2} {:<10} {:<2} {:<0}".format(ls[0],"||", ls[1],"||", ls[2], "||",ls[3], "||",ls[4]))
    print("============================================================================================")

    con.commit()
    con.close()
    input()

# Create_all_tables()

while True:
    print("Welcome to the Library Management System")
    print("\nSelecte Your Options")
    print("1 - Issue Book")
    print("2 - Return Book")
    print("3 - Vive Not Returned Book")
    print("4 - Add New Book")
    print("5 - Search Book")
    print("6 - Book History")
    print("7 - Add New Student")
    print("8 - Search Student")
    print("9 - Student History")
    print("0 - Exit")
    ch = int(input("Provide Your Choice : "))
    if   ch == 1: issue_book()
    elif ch == 2: return_book()
    elif ch == 3: view_not_returned_books()
    elif ch == 4: add_new_book()
    elif ch == 5: search_book()
    elif ch == 6: book_history()
    elif ch == 7: add_new_student()
    elif ch == 8: search_student()
    elif ch == 9: student_history()
    elif ch == 0: exit(0)