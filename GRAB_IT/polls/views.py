from multiprocessing import connection
from django.http import HttpResponse
from django.shortcuts import render
import mysql.connector
def index(request):
    return render(request, 'home.html', {'name' : 'Lovleen'})
def index1(request):
    return render(request, 'login.html', {'name' : 'Lovleen'})
def index2(request):
    return render(request, 'payment.html', {'name' : 'Lovleen'})
    #  return redirect("http://127.0.0.1:8000/polls/add1")
def thank(request):
    val1 = 100
    return render(request, 'thank.html', {'result' : val1})
def add(request):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Moonstar@0",
    database="grab_it"
    )
    val1 = int(request.POST['num'])
    # create a cursor object
    mycursor = mydb.cursor()
     # execute a SELECT statement to retrieve all data from the table
    mycursor.execute(f"select * from customer where customer_id = {val1}")
    # retrieve all rows from the cursor
    rows = mycursor.fetchall()
    print(rows)
    res = ""
    for row in rows:
        for i in row:
            res = res + " " + str(i)
        res = res + "         " 
    print(res)
    if len(res) == 0:
        res = res + "Failed login"
        return render(request, 'result.html', {'result':res})
    return render(request, 'login.html', {'result' : val1})
def add2(request):
    val1 = (request.POST['num7'])  
    return  render(request, 'shop.html')
def add3(request):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Moonstar@0",
    database="grab_it"
    )
    res = ""
    val1 = int(request.POST['num8'])  
    mycursor = mydb.cursor()
    val2 = val1
    val1 = 1000 - val1
    s = str(val1)
    v = 1000*val2
     # execute a SELECT statement to retrieve all data from the table
    sql = "UPDATE PRODUCT SET pqt = " + s + "   Where PID = 101"
    try:
    # Execute the SQL command
        mycursor.execute(sql)
    
    # Commit your changes in the database
        mydb.commit()
    except:
    # Rollback in case there is any error
        mydb.rollback()
    # retrieve all rows from the cursor
    rows = mycursor.fetchall()
    s  = "shoes"
    try:
    # Execute the SQL command
        mycursor.execute(f"insert into basket (pro_id, customer_id, product_name, product_quantity, Total_cost) values (101, 100,'shoes','{val2}', '{v}'")
    
    # Commit your changes in the database
        mydb.commit()
    except:
    # Rollback in case there is any error
        mydb.rollback()
    # retrieve all rows from the cursor
    rows = mycursor.fetchall()
    for row in rows:
            for i in row:
                res = res + " " + str(i)
            res = res + "         "  
    print(res)
    
    return render(request, 'cart.html', {'result':val2, 'final' : v})
def add4(request):
    val1 = int(request.POST['cardname'])
    val2 = int(request.POST['cardnumber'])
    val3 = int(request.POST['expmonth'])
    val4 = int(request.POST['expyear'])
    val5 = int(request.POST['cvv'])
    return render(request, 'index1.html')
def add1(request):
    render(request, 'login.html', {'name' : 'Lovleen'})
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Moonstar@0",
    database="grab_it"
    )
    res = ""
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    val3 = int(request.POST['num3'])
    val4 = int(request.POST['num4'])
    val5 = int(request.POST['num5'])
    val6 = int(request.POST['num6'])
    # create a cursor object
    mycursor = mydb.cursor()

    # execute a SELECT statement to retrieve all data from the table
    mycursor.execute(f"select Product_Name, Product_prize from Product where Product_Prize>={val1}")
    rows = mycursor.fetchall()
    # retrieve all rows from the cursor
    rows = mycursor.fetchall()

    # display the data
    for row in rows:
        for i in row:
            res = res + str(i)
        res = res + "         "
    if(val2 != 0):
        mycursor = mydb.cursor()
        # execute a SELECT statement to retrieve all data from the table
        mycursor.execute(f"SELECT * from customer where customer_id = {val2}")
        # retrieve all rows from the cursor
        rows = mycursor.fetchall()

        # display the data
        for row in rows:
            for i in row:
                res = res + " " + str(i)
            res = res + "         "
    if(val3 == 1):
        mycursor = mydb.cursor()
        # execute a SELECT statement to retrieve all data from the table
        mycursor.execute(f" select city,zip_code ,count(*) from customer group by city,zip_code with rollup;")
        # retrieve all rows from the cursor
        rows = mycursor.fetchall()
        # display the data
        for row in rows:
            for i in row:
                res = res + " " + str(i)
            res = res + "         "
    if(val3 == 2):
        mycursor = mydb.cursor()
        # execute a SELECT statement to retrieve all data from the table
        mycursor.execute(f"select city,street_num,zip_code,sum(mrp) from customer, payment where customer.customer_id=payment.customer_id group by city,street_num,zip_code with rollup;")
        # retrieve all rows from the cursor
        rows = mycursor.fetchall()
        # display the data
        for row in rows:
            for i in row:
                res = res + " " + str(i)
            res = res + "         "
    if(val3 == 3):
        mycursor = mydb.cursor()
        # execute a SELECT statement to retrieve all data from the table
        mycursor.execute(f"select city,street_name,street_num,zip_code,avg(rating) from customer natural join reviews group by city,street_name,street_num,zip_code with rollup;")
        # retrieve all rows from the cursor
        rows = mycursor.fetchall()
        # display the data
        for row in rows:
            for i in row:
                res = res + " " + str(i)
            res = res + "         "
    if(val3 == 4):
        mycursor = mydb.cursor()
        # execute a SELECT statement to retrieve all data from the table
        mycursor.execute(f"select year,month,count(*) from complaint group by year,month with rollup;")
        # retrieve all rows from the cursor
        rows = mycursor.fetchall()
        # display the data
        for row in rows:
            for i in row:
                res = res + " " + str(i)
            res = res + "         "   
    if(val4 != 0):
        mycursor = mydb.cursor(buffered=True)
        # execute a SELECT statement to retrieve all data from the table
        mycursor.execute(f"delete from customer  where customer_id={val4};")
        mycursor.execute("select * from old_customer")
        # retrieve all rows from the cursor
        rows = mycursor.fetchall()
        # display the data
        for row in rows:
            for i in row:
                res = res + " " + str(i)
            res = res + "         "  
    if(val5 != 0 and val6 != 0):
        mycursor = mydb.cursor(buffered=True)
        # execute a SELECT statement to retrieve all data from the table
        mycursor.execute(f"insert into basket values({val5},1,'Jubilant HollisterStier LLC',{val6},900);")
        # retrieve all rows from the cursor
        rows = mycursor.fetchall()
        # display the data
        for row in rows:
            for i in row:
                res = res + " " + str(i)
            res = res + "         "  
    print(res)
    return render(request, 'result.html', {'result':res})