# Import module 
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox
import random
import tkinter.font as font
from python_backend import * 

window = Tk()



# setting attribute
window.state('zoomed')
window.title("A Piece of Cake")

pic_folder = "C:\\New folder\\Pictures"

weight = 1
egg = "EGG" 
##############################################################
def TOP_RIBBON():
    b = 107
    drop_font = font.Font(family='Georgia', size=12, weight='bold')

    #celebration_tab
    celebration_tab = Button ( window, text = 'CELEBRATION', bg="#462828",
                               fg="WHITE", highlightbackground ="#462828", height= 1,
                               width=15, command=lambda:celebration_cakes())
    celebration_tab['font'] = drop_font
    celebration_tab.place(x=200, y=b)

    #fruit_tab
    fruit_tab = Button ( window, text = 'FRUIT', bg="#462828",
                               fg="WHITE", highlightbackground ="#462828", height= 1,
                               width=15, command=lambda:fruit_cakes())
    fruit_tab['font'] = drop_font
    fruit_tab.place(x=430, y=b)

    #theme_tab
    theme_tab = Button ( window, text = 'THEME', bg="#462828",
                               fg="WHITE", highlightbackground ="#462828", height= 1,
                               width=15, command=lambda:theme_cakes())
    theme_tab['font'] = drop_font
    theme_tab.place(x=680, y=b)

    #wedding_tab
    wedding_tab = Button ( window, text = 'WEDDING', bg="#462828",
                               fg="WHITE", highlightbackground ="#462828", height= 1,
                               width=15, command=lambda:wedding_cakes())
    wedding_tab['font'] = drop_font
    wedding_tab.place(x=930, y=b)
    cart_button()
    back_to_home()
    
##############################################################

def page_bg(bg_location):
    #Open image using Image module
    img = Image.open(bg_location)
    test = ImageTk.PhotoImage(img)
    

    #Resize the Image using resize method
    resized_image = img.resize((window.winfo_screenwidth(),window.winfo_screenheight()), Image.LANCZOS)
    new_image = ImageTk.PhotoImage(resized_image)
    label1 = tkinter.Label(image=new_image)
    label1.image = new_image

    # Position image
    label1.place(x=0, y=0)

##############################################################
def cake_image(cake_name, x_intercept, y_intercept):
    #Open image using Image module
    img1 = Image.open(pic_folder+"\\"+ cake_name +".jpg")
    test1 = ImageTk.PhotoImage(img1)
    

    #Resize the Image using resize method
    resized_image1 = img1.resize((179,170), Image.LANCZOS)
    new_image1 = ImageTk.PhotoImage(resized_image1)
    label2 = tkinter.Label(image=new_image1)
    label2.image = new_image1
    # Position image
    label2.place(x=x_intercept, y= y_intercept)

##############################################################

def cake_detail_page_image(bg_location, x_intercept, y_intercept):
    #Open image using Image module
    img1 = Image.open(bg_location)
    test1 = ImageTk.PhotoImage(img1)
    

    #Resize the Image using resize method
    resized_image1 = img1.resize((380,480), Image.LANCZOS)
    new_image1 = ImageTk.PhotoImage(resized_image1)
    label2 = tkinter.Label(image=new_image1)
    label2.image = new_image1

    # Position image
    label2.place(x=x_intercept, y= y_intercept)
        
##############################################################

def Buy_Now():
    # Buy Now Button
    buynow = Button ( window, text = 'BUY NOW', activeforeground='#FFFFFF',
                      activebackground='#2DAB57' , bg='#51FF8B',height= 2, width=47, command = Buy_Now_Action)
    # pady is used for giving some padding in y direction
    buynow.place(x=800, y=150)
    
def Buy_Now_Action():
    tkinter.messagebox.showinfo(title="A Piece Of Cake", message="Purchase Completed. THANK YOU !")
    del_cart()
##############################################################
  
def Add_to_Cart_Button(cake_name):
    # Add to Cart Button
    add_to_cart1 = Button ( window,command = lambda:Add_to_Cart(cake_name),text = 'ADD TO CART', activeforeground='#FFFFFF',
                           activebackground='#9F4CA6' , bg='#F682FF',height= 2, width=47)
    add_to_cart1.place(x=531, y=590)
    
##############################################################
    
def Add_to_Cart(cake_name):
    print(weight)
    #cart_items.append(cake_name)
    add_to_table(cake_name,weight,egg)
    tkinter.messagebox.showinfo(title="A Piece Of Cake", message=cake_name+" Added To Cart")
    
##############################################################
def weight_click(value):
        global weight
        weight = value
        print(weight)
def type_click(value):
        global egg
        egg = value
        print(egg)
def cake_info(name,price):

    drop_font = font.Font(family='Calibri', size=14, weight='bold')
    cake_weight_label = Label(text = "Cake Weight", bg = "#ECDFDC", fg="#462828",
                      font=('Calibri 18 bold')).place(x = 531,y = 425)
    cake_type_label = Label(text = "Egg/Eggless", bg = "#ECDFDC", fg="#462828",
                      font=('Calibri 18 bold')).place(x = 531,y = 375)
    clicked = StringVar()
    clicked.set( "1" )
    cake_weight = OptionMenu( window , clicked , *["1","2","3","4"], command=weight_click)
    cake_weight.config(bg="#F9F0EE", fg="#462828", highlightbackground ="#D5BAB1", borderwidth=0)
    cake_weight["menu"].config(bg="#F9F0EE", fg="#462828")
    cake_weight['font'] = drop_font
    cake_weight.place(x = 681,y = 425)

    clicked = StringVar()
    clicked.set( "EGG" )
    egg_eggless = OptionMenu( window , clicked , *["EGG","EGGLESS"], command=type_click)
    egg_eggless.config(bg="#F9F0EE", fg="#462828", highlightbackground ="#D5BAB1", borderwidth=0)
    egg_eggless["menu"].config(bg="#F9F0EE", fg="#462828")
    egg_eggless['font'] = drop_font
    egg_eggless.place(x = 681,y = 375)
    cake_name = Label(text = name, bg = "#ECDFDC", fg="#462828",
                      font=('Georgia 28 bold')).place(x = 531,y = 200)
    cake_price = Label(text = price, bg = "#ECDFDC", fg="#462828",
                       font=('Georgia 26 bold')).place(x = 531,y = 250)
    
###############################################################
def cart_button():
    cart = Button ( window, text = 'CART', activeforeground='#FFFFFF',activebackground='#301A29',
            fg='#FFFFFF', bg='#4B3444',height= 1, width=11, command=lambda:cart_page())
    cart.place(x=window.winfo_screenwidth()-85, y=80)

def cart_page():
    y = 250
    page_bg(pic_folder+"\\bg.jpg")
    TOP_RIBBON()

    cart_items = get_from_cart()
    i = 0
    Shopping_cart = Label(text = "SHOPPING CART", bg = "#ECDFDC", fg="#462828",
                      font=('Georgia 28 bold')).place(x = 100,y = 150)
    My_Total = 0

    for cart_item in cart_items:
        My_Total += cart_item[4]
        i += 1
        cake_name = Label(text = cart_item[1], bg = "#ECDFDC", fg="#462828",
                          font=('Georgia 18')).place(x = 100,y = y+(40*i))
        cake_type = Label(text = str(cart_item[2]), bg = "#ECDFDC", fg="#462828",
                          font=('Georgia 18')).place(x = 400,y = y+(40*i))
        cake_qty = Label(text = str(cart_item[3]), bg = "#ECDFDC", fg="#462828",
                          font=('Georgia 18')).place(x = 600,y = y+(40*i))
        cake_price = Label(text = str(cart_item[4]), bg = "#ECDFDC", fg="#462828",
                          font=('Georgia 18')).place(x = 700,y = y+(40*i))

    i+=1
    line = Label(text = "____________________________________________________", bg = "#ECDFDC", fg="#462828",
                          font=('Georgia 24')).place(x = 100,y = y+(40*i))
    i+=1
    line1=Label(text = "TOTAL :", bg = "#ECDFDC", fg="#462828",
                          font=('Georgia 20')).place(x = 100,y = y+(40*i))

    line2=Label(text = str(My_Total), bg = "#ECDFDC", fg="#462828",
                          font=('Georgia 20')).place(x = 700,y = y+(40*i))
    Buy_Now()   
    
       
###############################################################

def cake_detail_page( cake_name, cake_price):
    page_bg(pic_folder+"\\bg.jpg")
    cake_detail_page_image(pic_folder+"\\"+ cake_name +".jpg",100,150)
    TOP_RIBBON()
    Add_to_Cart_Button(cake_name)
    cake_info(cake_name, cake_price)
    #back_button()

###############################################################

def cake_name_button(name, x_intercept, y_intercept,price):

    #ans = get_cake_details(name)
    cake_name = Button(window, text = name, height = 1, width = 17, command=lambda:cake_detail_page(name, str(price)+"/-"))
    cake_name.place(x=x_intercept, y=y_intercept)
    cake_name.config(font=('Bahnschrift Light SemiCondensed',15))

def celebration_cakes():

    #SELECT cake_name, Price_per_unit, Cake_description FROM a_piece_of_cake.available_cakes where Cake_Dept ='Celebration'
    cakes = get_cakes('celebration')

    row = 90
    img_column = 175
    button_column = 325
    page_bg(r"C:\New folder\Pictures\bg.jpg")
    for cake in cakes:
        cake_image(cake[0],row, img_column)
        cake_name_button(cake[0],row,button_column,cake[1])
        row+=330
        if row>1400:
            row = 90
            img_column += 300
            button_column += 300
        


    TOP_RIBBON()

###############################################################

def fruit_cakes():

    page_bg(r"C:\New folder\Pictures\bg.jpg")

    cakes = get_cakes('fruit')

    row = 90
    img_column = 175
    button_column = 325
    page_bg(r"C:\New folder\Pictures\bg.jpg")
    for cake in cakes:
        cake_image(cake[0],row, img_column)
        cake_name_button(cake[0],row,button_column,cake[1])
        row+=330
        if row>1400:
            row = 90
            img_column += 300
            button_column += 300

    TOP_RIBBON()

###############################################################

def wedding_cakes():

    page_bg(r"C:\New folder\Pictures\bg.jpg")
    cakes = get_cakes('wedding')

    row = 90
    img_column = 175
    button_column = 325
    page_bg(r"C:\New folder\Pictures\bg.jpg")
    for cake in cakes:
        cake_image(cake[0],row, img_column)
        cake_name_button(cake[0],row,button_column,cake[1])
        row+=330
        if row>1400:
            row = 90
            img_column += 300
            button_column += 300
    

    TOP_RIBBON()

###############################################################

def theme_cakes():

    page_bg(r"C:\New folder\Pictures\bg.jpg")
    cakes = get_cakes('theme')

    row = 90
    img_column = 175
    button_column = 325
    page_bg(r"C:\New folder\Pictures\bg.jpg")
    for cake in cakes:
        cake_image(cake[0],row, img_column)
        cake_name_button(cake[0],row,button_column,cake[1])
        row+=330
        if row>1400:
            row = 90
            img_column += 300
            button_column += 300
    

    TOP_RIBBON()

##############################################################
def Show_More_Page():
    page_bg(pic_folder+"\\Show more page.png")
    #Celebration Cakes Button
    Celebration_Cakes_Button = Button ( window, text = 'Celebration Cakes', activeforeground='#FFFFFF',
                      activebackground='#E1AFF0' , bg='#E1AFF0', font=('Cambria'), height= 3, width=38 , command=lambda:celebration_cakes())
    Celebration_Cakes_Button.place(x=80, y=625) 

    #Theme cake Button
    Theme_Cakes_Button = Button ( window, text = 'Theme Cakes', activeforeground='#FFFFFF',
                      activebackground='#E1AFF0' , bg='#E1AFF0', font=('Cambria'), height= 3, width=38 , command=lambda:theme_cakes())
    Theme_Cakes_Button.place(x=510, y=625)

    #Wedding Cakes Button
    Wedding_Cakes_Button = Button ( window, text = 'Wedding Cakes', activeforeground='#FFFFFF',
                      activebackground='#E1AFF0' , bg='#E1AFF0', font=('Cambria'), height= 3, width=38 , command=lambda:wedding_cakes())
    Wedding_Cakes_Button.place(x=935, y=625)
    back_to_home()

###############################################################

def homepage():
    page_bg(pic_folder+"\\Home page.png")
    Show_More_Button = Button ( window, text = 'Show More>', activeforeground='#FFFFFF',
                      activebackground='#F292D2' , bg='#F292D2', font=('Cambria'), height= 1, width=18, command=lambda:Show_More_Page())
    # pady is used for giving some padding in y direction
    Show_More_Button.place(x=500, y=650)
    
###############################################################

def back_to_home():
    back = Button ( window, text = '⌂', activeforeground='#FFFFFF',activebackground='#301A29',
            fg='#FFFFFF', bg='#4B3444',height= 1, width=3, command=lambda:homepage())
    back.place(x=5, y=110)
    
###############################################################











    
