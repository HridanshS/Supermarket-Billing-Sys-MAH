import random
import csv

discount_rate=.10 # flat 10% discount in the store
class Product():
    def __init__(self, product_id, name, price, quantity, cost): #Ananya 

        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.cost = cost
    
    def print_function_product(self):   #Ananya 
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")
        print(f"Cost: {self.cost}")
        
    def dict_(self):  #Ananya 
        
        product_dict = {
            'product_id' : self.product_id,
            'name' : self.name,
            'price' : self.price,
            'quantity' : self.quantity,
            'cost' : self.cost,
            'profit' :0,
            'discount':0,
            'sale_price':0

        }
        return product_dict
    
    def add_product(self): # Ananya
        
        csv_fd = open('product.csv', 'r')
        csv_reader= csv.DictReader(csv_fd)
        count = 0
        temp_list=[]
        for row in csv_reader:
            if row["product_id"]== str(self.product_id):
                b= float(row["quantity"])+ float(self.quantity)
                row["quantity"]= str(b)
                count=count+1
                temp_list.append(row)
            else:
                temp_list.append(row)

        if count == 0:
            
            product_dict = {
            'product_id' : self.product_id,
            'name' : self.name ,
            'price' : self.price,
            'quantity' : self.quantity,
            'cost' : self.cost,
            'profit' : 0,
            'discount':0,
            'sale_price' :0
            }
            temp_list.append(product_dict)
        csv_write_1= open('product.csv','w')
        csv_writer_1 = csv.DictWriter(csv_write_1, fieldnames= ['product_id','name','price','quantity','cost','profit','discount','sale_price'])
        csv_writer_1.writeheader()
        csv_writer_1.writerows(temp_list)

    def remove_product(self): #Ananya
        temp_list=[]
        csv_fd = open('product.csv', 'r')
        csv_reader= csv.DictReader(csv_fd)
        for row in csv_reader:
            if row["product_id"]!=str(self.product_id):
                temp_list.append(row)
        csv_write_1= open('product.csv','w')
        csv_writer_1 = csv.DictWriter(csv_write_1, fieldnames= ['product_id','name','price','quantity','cost','profit','discount','sale_price'])
        csv_writer_1.writeheader()
        csv_writer_1.writerows(temp_list)
    
    def modify_product(self): #Ananya 
        csv_fd = open('product.csv', 'r')
        csv_reader= csv.DictReader(csv_fd)
        temp_list=[]
        for row in csv_reader:
            if row ["product_id"]==str(self.product_id):
                row["name"]= self.name
                row["price"] = self.price
                row["quantity"]=self.quantity
                temp_list.append(row)
            else:
                temp_list.append(row)
        csv_write_1= open('product.csv','w')
        csv_writer_1 = csv.DictWriter(csv_write_1, fieldnames= ['product_id','name','price','quantity','cost','profit','discount','sale_price'])
        csv_writer_1.writeheader()
        csv_writer_1.writerows(temp_list)
    
    #to calculate the profit
    def compute_profit(self): #Miguel Urena
        csv_fd = open('product.csv', 'r')
        csv_reader= csv.DictReader(csv_fd)
        temp_list=[]
        for row in csv_reader:
            row["profit"]=float(row['sale_price'])-float(row['cost'])
            temp_list.append(row)
        csv_write_1= open('product.csv','w')
        csv_writer_1 = csv.DictWriter(csv_write_1, fieldnames= ['product_id','name','price','quantity','cost','profit','discount','sale_price'])
        csv_writer_1.writeheader()
        csv_writer_1.writerows(temp_list)
    
    # to calculate the discount amount and add it as a column to a csv
    def compute_discount_amount(self): #Miguel Urena
        csv_fd = open('product.csv', 'r')
        csv_reader= csv.DictReader(csv_fd)
        temp_list=[]
        for row in csv_reader:
            row["discount"]= float(row["price"])*float(discount_rate)
            temp_list.append(row)
        csv_write_1= open('product.csv','w')
        csv_writer_1 = csv.DictWriter(csv_write_1, fieldnames= ['product_id','name','price','quantity','cost','profit','discount','sale_price'])
        csv_writer_1.writeheader()
        csv_writer_1.writerows(temp_list)
    
    #to compute the final sale price after discount and add it after as a column to csv
    def compute_sale_price(self): #Ananya Chokhany
        csv_fd = open('product.csv', 'r')
        csv_reader= csv.DictReader(csv_fd)
        temp_list=[]
        for row in csv_reader:
            row["sale_price"]= float(row['price'])-float(row['discount'])
            temp_list.append(row)
        csv_write_1= open('product.csv','w')
        csv_writer_1 = csv.DictWriter(csv_write_1, fieldnames= ['product_id','name','price','quantity','cost','profit','discount','sale_price'])
        csv_writer_1.writeheader()
        csv_writer_1.writerows(temp_list)
    
    #to display the item with the highest cost price
    def display_highest_cost_price(self): #Ananya Chokhany
        csv_fd = open('product.csv', 'r')
        csv_reader= csv.DictReader(csv_fd)
        cost_price=0
        temp_list=[]
        for row in csv_reader:
            if float(row['cost'])>= cost_price:
                cost_price=float(row['cost'])
        csv_fd = open('product.csv', 'r')
        csv_reader= csv.DictReader(csv_fd)
        for row in csv_reader:
            if float(row['cost'])== cost_price:
                temp_list.append(row)
        print(temp_list)
    
    #to display the item with the lowest profit
    def display_lowest_profit(self): #Ananya Chokhany
        csv_fd = open('product.csv', 'r')
        csv_reader= csv.DictReader(csv_fd)
        temp_list=[]
        profit=0
        for row in csv_reader:
            profit=float(row['profit'])
        
        csv_fd = open('product.csv', 'r')
        csv_reader= csv.DictReader(csv_fd)
        for row in csv_reader:
             if float(row['profit'])<= profit:
                 profit=float(row['profit'])

        csv_fd = open('product.csv', 'r')
        csv_reader= csv.DictReader(csv_fd)
        for row in csv_reader:
            if float(row['profit']) == profit:
                temp_list.append(row)
        print(temp_list)
        

#to convert the list to a dictionary
def convert_to_dict(list_of_things): #Ananya Chokhany
    return [x.dict_() for x in list_of_things]

# to write to the csv file for the Class Product
def write_list_to_file(product_dictionary): # Ananya Chokhany
    csv_fd = open('product.csv', 'w')
    csv_writer = csv.DictWriter(csv_fd, fieldnames=list(product_dictionary[0].keys()))
    csv_writer.writeheader()
    csv_writer.writerows(product_dictionary)
    csv_fd.close()
    return csv_writer

# to write to the csv file for the class Cart
def write_list_to_file_1(): #Ananya Chokhany
    csv_fd_1 = open('carts.csv', 'w')
    csv_writer_x = csv.DictWriter(csv_fd_1, fieldnames=['cart_id','name','price','quantity','status'])
    csv_writer_x.writeheader()
    csv_fd_1.close()
    return csv_writer_x



class Cart():

    def __init__(self, cart_id, status=open): #Ananya 
        self.cart_id = cart_id
        self.status = 'open'

    #Hridansh
    def print_function(self):    #print function
        print("These are the parameters of the cart: ")
        print(f"Cart ID: {self.cart_id}")
        print(f"Status: {self.status}")

   #Miguel
    def dict_(self):
        cart_dict = {
            'cart_id' : self.cart_id,
            'name' : [],
            'quantity': 0,
            'price' : 0,
            'status' : 'open',
        }
        return cart_dict

    #Hridansh 
    def update_list(self, current_list, new_product): #helper function
        for i in range(len(current_list)):
            if current_list[i] == new_product:
                break
        current_list.append(new_product)
        return current_list

    #Hridansh
    def add_to_cart(self, product_id, quantity): # to add items to the cart
        list_of_dicts_cart = []
        if len(list_of_dicts_cart) == 0:
            list_of_dicts_cart.append(self.dict_())
        for i in range(len(list_of_dicts_cart)):
            if list_of_dicts_cart[i]['cart_id'] == self.cart_id:
                if len(list_of_dicts_cart[i]['name']) == 0:
                    list_of_dicts_cart[i]['name'].append(product_id)
                else:
                    list_of_dicts_cart[i]['name'] = update_list(list_of_dicts_cart[i]['name'], product_id)
                list_of_dicts_cart[i]['quantity'] += quantity
                total_price = 0
                total_price = (self.find_price(product_id)) * quantity
                list_of_dicts_cart[i]['price'] += total_price
        csv_fd_2 = open('carts.csv', 'a')
        csv_writer_x_1 = csv.DictWriter(csv_fd_2,fieldnames=['cart_id','name','price','quantity','status'])
        csv_writer_x_1.writerows(list_of_dicts_cart)

   #Hridansh
    def compute_final_bill(self): # to compute the final bill
        csv_fd = open('carts.csv', 'r')
        csv_reader= csv.DictReader(csv_fd)
        cart_id= self.cart_id
        price_list=[]
        temp_list=[]
        total_bill=0
        for row in csv_reader:
            if row['cart_id']== str(cart_id):
                price_list.append(row['price'])
                row['status']='closed'
                temp_list.append(row)
            else:
                temp_list.append(row)
        for price in price_list:
            total_bill= total_bill+float(price)
        print(total_bill)
        csv_fd_2 = open('carts.csv', 'w')
        csv_writer_x_1 = csv.DictWriter(csv_fd_2,fieldnames=['cart_id','name','price','quantity','status'])
        csv_writer_x_1.writeheader()
        csv_writer_x_1.writerows(temp_list)

   #Hridansh
    def remove_from_cart(self, product_id): # to remove items from the cart
        temp_list=[]
        csv_fd = open('carts.csv', 'r')
        csv_reader_writer = csv.DictReader(csv_fd)
        cart_id=self.cart_id
        for row in csv_reader_writer:
            if str(row['cart_id'])==(cart_id):
                if row['name'][1]!= str(product_id):
                    temp_list.append(row)
            else:
                temp_list.append(row)
                
        csv_fd_2 = open('carts.csv', 'w')
        csv_writer_x_1 = csv.DictWriter(csv_fd_2,fieldnames=['cart_id','name','price','quantity','status'])
        csv_writer_x_1.writeheader()
        csv_writer_x_1.writerows(temp_list)

    
   #Hridansh
    def find_price(self, product_id): # helper method
        csv_fd = open('product.csv', 'r')
        csv_reader = csv.DictReader(csv_fd)
        #temp_list=[]
        product_price = 0
        for row in csv_reader:
            if row ["product_id"] == str(product_id):
                product_price = float(row["sale_price"])
                csv_fd.close()
                return product_price

    #Miguel Urena
    def modify_cart(self,product_id,quantity): # to modify the items in the cart
        temp_list=[]
        csv_fd = open('carts.csv', 'r')
        csv_reader_writer = csv.DictReader(csv_fd)
        for row in csv_reader_writer:
            if str(row['cart_id'])==(self.cart_id):
                if row['name'][1]== str(product_id):
                    if float((row['quantity'])) >= (quantity):
                        row['quantity']= float(quantity)
                        total_price = 0
                        total_price = (self.find_price(product_id)) * quantity
                        (row['price']) = total_price
                        temp_list.append(row)
                    else:
                        print("Not enough of this product in cart to remove this quantity")
                        #temp_list.append(row)
                else:
                    temp_list.append(row)
            else:
                temp_list.append(row)
       # print(temp_list)
        csv_fd_2 = open('carts.csv', 'w')
        csv_writer_x_1 = csv.DictWriter(csv_fd_2,fieldnames=['cart_id','name','price','quantity','status'])
        csv_writer_x_1.writeheader()
        csv_writer_x_1.writerows(temp_list)

    #Hridansh 
    def print_bill(self): # to save the bill into a txt file 
        csv_fd = open('carts.csv', 'r')
        csv_reader= csv.DictReader(csv_fd)
        txt_fd = open('supermarket_bill.txt', 'w+')
        txt_fd.write("Supermarket Location: 201 Dowman Drive")
        txt_fd.write("\n")
        txt_fd.write("For Delivery Service call us @ +1 (470) 233 0721")
        txt_fd.write("\n")
        txt_fd.write("----------------")
        txt_fd.write(f"\nCart ID: {self.cart_id}")
        txt_fd.write("\n")
        txt_fd.write("----------------\n")
        txt_fd.write("Product\tQty\tPrice\n")
        for row in csv_reader:
            item = str(row['name'][1])
            txt_fd.write(f"{self.find_name(item)}\t{row['quantity']}\t{self.find_price(item)}")
            txt_fd.write("\n")
        
   #Hridansh
    def find_name(self, product_id): # helper function 
        csv_fd = open('product.csv', 'r')
        csv_reader = csv.DictReader(csv_fd)
        product_name = ""
        for row in csv_reader:
            if row ["product_id"] == str(product_id):
                product_name = row["name"]
                csv_fd.close()
                return product_name


if __name__ == "__main__":
    product1= Product(1,'Fruit', '120','200','50')
    product2= Product(2,'Vegetable','100','250','40')
    product3= Product(3,'Milk','130','60','55')
    list_product= [product1,product2]
    product_dictionary=convert_to_dict(list_product)
    write_list_to_file(product_dictionary)
    product3.add_product()
    product3.remove_product()
    product3.compute_sale_price()

    write_list_to_file_1()
    cart_obj = Cart("001")
    cart_obj_1 = Cart("002")
    cart_obj.add_to_cart(1, 5)
    cart_obj.add_to_cart(2, 10)
    cart_obj_1.add_to_cart(2, 5)
    cart_obj.remove_from_cart(1)
    cart_obj.modify_cart(2, 2)
    cart_obj.compute_final_bill()
    
    
    cart_obj = Cart("001")
    cart_obj.print_bill()





  

    




       




