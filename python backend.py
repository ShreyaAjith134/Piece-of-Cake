import mysql.connector as c

con = c.connect(user='root', password='MySQL1234', host='127.0.0.1', database='a_piece_of_cake')
mycursor = con.cursor()
def insert_available_cake():
    Cake_id = int(input("Cake_id: "))
    Cake_name = input("Cake_name: ")
    Price_per_unit = int(input("Price_per_unit: "))
    Cake_Dept = input("Cake_Dept: ")
    Cake_description = input("Cake_description: ")
    Flavour_bool = int(input("Flavour_bool "))
    mycursor.execute("INSERT INTO available_cakes \
      VALUES({},'{}',{},'{}','{}',{})".format(Cake_id, Cake_name, Price_per_unit, Cake_Dept, Cake_description, Flavour_bool))
    con.commit()
    
def get_available_cakes():    
    mycursor.execute("Select * from available_cakes;")
    ans = mycursor.fetchall()
    for i in ans:
        print(i)

insert_available_cake()
get_available_cakes()

mycursor.close()       
con.close()

