import mysql.connector 

def get_from_cart():
    con = mysql.connector.connect(user='root', password='sr@123', host='127.0.0.1',
                                  database='a_piece_of_cake')
    mycursor = con.cursor()
    mycursor.execute("SELECT C.Cake_id, A.Cake_name, C.Type, C.Qty, C.Total FROM a_piece_of_cake.cart c, a_piece_of_cake.available_cakes a where c.Cake_id = a.Cake_id;")
    ans = mycursor.fetchall()
    con.close()
    return ans


def add_to_cart():
    Cake_id = int(input("Cake_id: "))
    Cake_name = input("Cake_name: ")
    Price_per_unit = int(input("Price_per_unit: "))
    Cake_Dept = input("Cake_Dept: ")
    Cake_description = input("Cake_description: ")
    Flavour_bool = int(input("Flavour_bool "))
    mycursor.execute("INSERT INTO available_cakes \
      VALUES({},'{}',{},'{}','{}',{})".format(Cake_id, Cake_name, Price_per_unit, Cake_Dept, Cake_description, Flavour_bool))
    con.commit()
 

def get_cakes(dept):
    con = mysql.connector.connect(user='root', password='sr@123', host='127.0.0.1',
                                  database='a_piece_of_cake')
    mycursor = con.cursor()
    mycursor.execute("SELECT cake_name, Price_per_unit, Cake_description FROM a_piece_of_cake.available_cakes where Cake_Dept ='"+dept+"';")
    ans = mycursor.fetchall()
    con.close()
    return ans

def get_cake_details(name):
    con = mysql.connector.connect(user='root', password='sr@123', host='127.0.0.1',
                                  database='a_piece_of_cake')
    mycursor = con.cursor()
    mycursor.execute("SELECT cake_id, cake_name, Price_per_unit, Cake_description FROM a_piece_of_cake.available_cakes where cake_name ='"+name+"';")
    ans = mycursor.fetchall()
    con.close()
    return ans

def add_to_table(cake_name,qty,egg):
    con = mysql.connector.connect(user='root', password='sr@123', host='127.0.0.1',
                                  database='a_piece_of_cake')
    mycursor = con.cursor()
    ans = get_cake_details(cake_name)
    Cake_id = ans[0][0]
    ppu = ans[0][2]
    Total = ppu*int(qty)

    sql = "INSERT INTO cart (cake_id, Qty, Total, Type) \
      VALUES({},{},{},'{}')".format(Cake_id, int(qty), Total, egg)
    mycursor.execute(sql)
    con.commit()
    
def del_cart():
    con = mysql.connector.connect(user='root', password='sr@123', host='127.0.0.1',
                                  database='a_piece_of_cake')
    mycursor = con.cursor()
    mycursor.execute("DELETE FROM cart;")
    con.commit()












