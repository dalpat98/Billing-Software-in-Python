'''
Restaurant billing system
'''

import time 


name_list={} #names and usernames of all registered peoples
login_data={} #list of all username with passwords
item_list={} #food items with its price
item_serial={} #food items with serial no.. like 1,2,3....
bill={} #contains dish_name:quantity for order
no_of_dish=1 #it is used to print 1,2,3... serial no. in front of items

def register(call): #call takes value 1 if it is called by admin() else takes 2 if called by customer()
    print("---------------------------Register-------------------------")
    name=input("Enter Name :")
    username=input("Enter Username :")
    password=input("Enter Password :")
    for i in login_data.keys():
        if i==username:
            print("\nUser Already Exits! Please Login")
            if call==1:
                return login(1) #by default returns true because forcefully everyone is registered
            else:
                return login(2)
            #if user exist then login is called and by default true value is returned
    else:
        login_data[username]=password
        name_list[username]=name
        print("\nHeyy",name,"You Are Registered successfully...\nLogin to Continue")
        if call==1:
            return login(1) #by default returns true because forcefully everyone is registered
        else:
            return login(2)
        
def login(call):
    print("---------------------------Login-------------------------")
    un=input("Enter Username :")
    pd=input("Enter Password :")
    userexist=False #by default user doesn't exist before checking condition 
    for i in login_data.keys():
        if i==un:
            userexist=True #if user exist then it would be true
            if login_data[un]==pd:
                print("\nLogin Successful")
                print("Welcome ",name_list[un]," Explore things easily here!\n")
                return True
            else:
                print("\nIncorrect Username/Password.... Please Try again")
                if call==1:
                    return login(1) #by default returns true because forcefully everyone is registered
                else:
                    return login(2)
    if userexist==False: #this will be only execute when user with specified username doesn't exist 
        print("\nUser not found... Please register or login with different account to continue")
        if call==1:
            return admin() #by default returns true because forcefully everyone is registered
        else:
            return customer()
    
def admin():
    print("1.Login")
    print("2.Register")
    ch=int(input("Enter your choice :"))
    if ch==1:
        val=login(1)#val is return value of login() function #1 is for admin() login call
    else:
        val=register(1) #by default returns true because forcefully everyone is registered
        
    while val==True:
        print("------------------------------------------------------------")
        print("1.Modify Menu")
        print("2.Display Menu")
        print("3.Logout")
        choice=int(input("Enter your choice :"))
        if choice==1:
            print("1.Add item")
            print("2.Delete item")
            print("3.Go Back")
            kh=int(input("Enter your choice :"))
            if kh==1:
                add_item()
            elif kh==2:
                delete_item()
            else:
                continue
        elif choice==2:
            display_menu()
        else:
            val=False #session time out.... Termination of while loop
            print("Logout Successfully")
            main() #after logout customer can login so main() is called here
        
def customer():
    print("1.Login")
    print("2.Register")
    ch=int(input("Enter your choice :"))
    if ch==1:
        val=login(2)#val is return value of login() function #2 is for customer() login call
    else:
        val=register(2) #by default returns true because forcefully everyone is registered
        
    while val==True:
        print("------------------------------------------------------------")
        print("1.Display Menu")
        print("2.Order food")
        print("3.Logout")
        choice=int(input("Enter your choice :"))
        if choice==1:
            display_menu()
        elif choice==2:
            val=order_food()
        else:
            val=False #session time out.... Termination of while loop
            print("Logout Successfully")
            main() #after logout another can login so main() is called here

def add_item():
    print("---------------------------Add Item-------------------------")
    name=input("Enter Name of Dish :")
    price=int(input("Enter Price :"))
    item_list[name]=price
    global no_of_dish  #by default in python we have to say compiler that this is global variable
    item_serial[no_of_dish]=name # serial number(key):dish_name(value)
    no_of_dish+=1
    print("\nItem Added Successfully")
    
def delete_item():
    print("---------------------------Delete Item-------------------------")
    if len(item_list)==0:
        print("Nothing left to delete")
    else:
        name=input("Enter Name of Dish :")
        for i in range(len(item_list)):
            if name in item_list.keys():
                del(item_list[name])
                print("\nItem deleted Successfully")
            else:
                print("\nIncorrect Details... try again")
                break
def display_menu():
    print("---------------------------FOOD MENU-------------------------")
    if(len(item_list))==0:
        print("Nothing to Show for now")
    else:
        number=1 #it is used to print 1,2,3... serial no. in front of items
        for i in item_list.keys():
            print(number,".",i,"\t= ",item_list[i])
            number+=1
        
def order_food():
    display_menu()
    print("----------------Order Food from above Menu--------------")
    if(len(item_list))==0:
        print("Oops...Nothing to order for now!")
        order=False
    else:
        order=True
    while order==True:
        dish_number=int(input("Enter dish number :-"))
        quantity=int(input("Enter Quantity :-"))
        bill[item_serial[dish_number]]=quantity  
        #here item_serial[dish_number]==dish_name and bill contains dish_name(key):quantity(value)
        cont=input("Want to add more ?(y/n): ") #for repeatation of loop
        if cont=='Y' or cont=='y':
            order=True
        else:
            order=False
    print("\nFood Ordered successfuly\n\n")
    return generate_bill() #value returned by gererate_bill() function will be again returned to customer() where order_food() is called
    
def animate_bill():
    for i in range(4):
        print("\rGenerating your BILL    ",end="");
        time.sleep(0.5)
        print("\rGenerating your BILL.   ",end="");
        time.sleep(0.5)
        print("\rGenerating your BILL..  ",end="");
        time.sleep(0.5)
        print("\rGenerating your BILL... ",end="");
        time.sleep(0.5)
        print("\rGenerating your BILL....",end="");
        time.sleep(0.5)
    print("\n\tBill Generated Successfully")
    
    
def generate_bill():
    animate_bill()
    print("\n-------------------------Bill-------------------------")
    number=1
    t_bill=0
    for i in bill.keys():
        one_tbill=bill[i]*item_list[i] # total amount of one item
        print(number,".",i,"\t",bill[i],"x",item_list[i]," = ",one_tbill)#serial number. dish_name  quantity*price = total_price
        t_bill+=one_tbill
        number+=1
    print("--------------------------------------------------")
    print(" TOTAL BILL    =      ",t_bill)
    print(" Gst 5%        =      "+"{:.2f}".format((t_bill/100)*5)) #to print upto 2 decimal places
    print(" Cgst 5%       =      "+"{:.2f}".format((t_bill/100)*5))
    t_bill+=t_bill/10
    print("                     --------------")
    print("Grand Total    =      ",t_bill)
    print("                     --------------")   
    thank_msg()
    return True  ## this will be excepted by order_food() function
    


def thank_msg():
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
                     THANK YOU                                         \n\
                    Visit Again !                                        \
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    
    
def main():
    print("---------------------------Welcome-------------------------")
    print("1.Admin panel")
    print("2.Customer panel")
    print("3.Exit")
    choice=int(input("Enter your choice :"))
    if choice==1:
        admin()
    elif choice==2:
        customer()
    else:
        return 0

main() #main function call ++starting of program++