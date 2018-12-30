#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 21:58:31 2017
Store
"""
import datetime
from random import randint

class StoreChain(object):
    #init method
    def __init__(self, name = "", address = ""):
        self.__name = name
        self.__address = address
                
    #__str__ method
    def __str__(self):
        return self.__name + " " + self.__address
        
    #properties
    @property
    def name(self):
        return self.__name
    @property
    def address(self):
        return self.__address
    
    #setters
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be str")
        self.__name = value
    @address.setter
    def address(self, value):
        if not isinstance(value, str):
            raise TypeError("Address must be str")
        self.__address = value


class Store(StoreChain):
    #init method
    def __init__(self, id = 0, name = "", address = "", tel = 0):
        super().__init__(name, address)
        self.__id = id
        self.__tel = tel
                
    #__str__ method
    def __str__(self):
        return self.__id+" "+super().__str__()+" "+self.__tel   
    
    #properties
    @property
    def id(self):
        return self.__id
    @property
    def tel(self):
        return self.__tel
    
    #setters
    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError("Id must be number")
        self.__id = value
    @tel.setter
    def tel(self, value):
        if not isinstance(value, int):
            raise TypeError("Tel must be numbers witout - ")
        self.__tel = value
        
        
class Citizen(object):
    #init method
    def __init__(self, ssn = 0, name = "", address = ""):
        self.__ssn = ssn
        self.__name = name
        self.__address = address
                
    #__str__ method
    def __str__(self):
        return self.__ssn+" "+self.__name+" "+self.__address
        
    #properties
    @property
    def ssn(self):
        return self.__ssn
    @property
    def name(self):
        return self.__name
    @property
    def address(self):
        return self.__address
    
    #setters
    @ssn.setter
    def ssn(self, value):
        if not isinstance(value, int):
            raise TypeError("SNN must be number")
        self.__ssn = value
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be str")
        self.__name = value
    @address.setter
    def address(self, value):
        if not isinstance(value, str):
            raise TypeError("Adress must be str")
        self.__address = value
   
    
class Staff(Citizen):
    #init method
    def __init__(self, ssn = 0, name=" ", address=" ", jobId = 0, jobTitle = " ", salary = 0):
        super().__init__(ssn, name, address)
        self.__jobId = jobId
        self.__jobTitle = jobTitle
        self.__salary = salary
        
                
    #__str__ method
    def __str__(self):
        return Citizen().__str__()+" "+self.__jobId+" "+self.__jobTitle+" "+self.__salary   
    
    #properties
    @property
    def jobId(self):
        return self.__jobId
    @property
    def jobTitle(self):
        return self.__jobTitle
    @property
    def salary(self):
        return self.__salary
    
    #setters
    @jobId.setter
    def jobId(self, value):
        if not isinstance(value, int):
            raise TypeError("Job id must be number")
        self.__jobId = value
    @jobTitle.setter
    def jobTitle(self, value):
        if not isinstance(value, str):
            raise TypeError("Job title must be str")
        self.__jobTitle = value
    @salary.setter
    def salary(self, value):
        if not isinstance(value, int):
            raise TypeError("Salary must be int")
        self.__salary = value
     

class Customer(Citizen):
    #init method
    def __init__(self, ssn = "", name = "", address = "", id = 0, ppoint = 0, tel = 0, member=[]):
        super().__init__(ssn, name, address)
        self.__id = id
        self.__ppoint = ppoint
        self.__tel = tel
        self.__member = member
                
    #__str__ method
    def __str__(self):
        return super().__str__()+" "+self.__id+" "+self.__ppoint+" "+self.__tel+" "+self.__member
    
    #property methods\
    @property
    def id(self):
        return self.__id
    @property
    def ppoint(self):
        return self.__ppoint
    @property
    def tel(self):
        return self.__tel
    @property
    def member(self):
        return self.__member
    
    #setters
    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError("Id must be int")
        self.__id = value
    @ppoint.setter
    def ppoint(self, value):
        if not isinstance(value, int):
            raise TypeError("Point must be number")
        self.__ppoint = value
    @tel.setter
    def tel(self, value):
        if not isinstance(value, int):
            raise TypeError("tel must be number without -")
        self.__tel = value
    @member.setter
    def member(self, value):
        if not isinstance(value, str):
            raise TypeError("member must be str")
        self.__member = value 
        

class Product():
    #init method
    def __init__(self, pcode="", name = "", desc = "", price = 0.0, point = 0):
        self.__pcode = pcode
        self.__name = name
        self.__desc = desc
        self.__price = price
        self.__point = point
        #self.__quantity = quantity
                
    #__str__ method
    def __str__(self):
        return self.__pcode+" "+self.__name+" "+self.__desc+" "+self.__price+" "+self.__point
    
    #property methods
    @property
    def pcode(self):
        return self.__pcode
    @property
    def name(self):
        return self.__name
    @property
    def desc(self):
        return self.__desc
    @property
    def price(self):
        return self.__price
    @property
    def point(self):
        return self.__point
#    @property
#    def quantity(self):
#        return self.__quantity
    
    #setters
    @pcode.setter
    def pcode(self, value):
        if not isinstance(value, str):
            raise TypeError("Product code must be str")
        self.__pcode = value
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be str")
        self.__name = value
    @desc.setter
    def desc(self, value):
        if not isinstance(value, str):
            raise TypeError("Description must be str")
        self.__desc = value
    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise TypeError("Price must be double")
        self.__price = value
    @point.setter
    def point(self, value):
        if not isinstance(value, int):
            raise TypeError("Point must be int")
        self.__point = value
#    @quantity.setter
#    def quantity(self, value):
#        if not isinstance(value, int):
#            raise TypeError("Quantity must be int")
#        self.__quantity = value

        
class Order(object):
    #init method
    def __init__(self, store, customer, staff, product, quantity):
        self.__store = store
        self.__staff = staff
        self.__customer = customer
        self.__product = product
        self.__quantity = quantity
    
    #property methods
    @property
    def store(self):
        return self.__store
    @property
    def customer(self):
        return self.__customer
    @property
    def staff(self):
        return self.__staff
    @property
    def product(self):
        return self.__product
    @property
    def quantity(self):
        return self.__quantity
    
    #setters
    @store.setter
    def store(self, value):
        if not isinstance(value, Store):
            raise TypeError("store must be Store type")
        self.__store = value
    @customer.setter
    def customer(self, value):
        if not isinstance(value, Customer):
            raise TypeError("customer must be Customer type")
        self.__customer = value
    @staff.setter
    def staff(self, value):
        if not isinstance(value, Staff):
            raise TypeError("staff must be Staff type")
        self.__staff = value
    @product.setter
    def product(self, value):
        if not isinstance(value, Product):
            raise TypeError("product must be Product type")
        self.__product = value
    @quantity.setter
    def quantity(self, value):
        if not isinstance(value, int):
            raise TypeError("Quantity must be int")
        self.__quantity = value
    
    #print receipt
    def printReceipt(self):
        now = datetime.datetime.now()
        print('\n\t\tWelcome to ', self.__store.name)
        print('\t\tStaff: ', self.__staff.name)
        print('\t\tCustomer ID: ', self.__customer.id)
        print('\n\t\t      RECEIPT')
        print (now.strftime('\t\t     %Y-%m-%d\n\t\t      %H:%M:%S'))
        print('\t\t     ST #', self.__store.id)
        print()
        print (' Product Name'.ljust(20)+'Product Code'.ljust(20)+'Price'.ljust(11)+'Q')
        total = 0.0
        items = 0
        count = 0
        for x in self.__product:
            print (" "+x.name.ljust(19)+str(x.pcode).ljust(20)+str(x.price).ljust(10),self.__quantity[count])
            total += (x.price * self.__quantity[count])
            items += self.__quantity[count]
            self.__customer.ppoint += (x.point * self.__quantity[count])
            count = count + 1
        print('\n\n\n\n TOTAL'.ljust(42),'%.2f'%total)
        print()
        print('# ITEMS SOLD '.rjust(32),items)
        print('\n Total Points: ',self.__customer.ppoint)
        print()
        print('***CUSTOMER COPY***'.rjust(38))
        print('\n\n\n')
        
#main

pro = []
quant = []

store = Store(1010, 'Walmart', 'Namgu Incheon', 2033230294) 
cus1 = Customer(457555462, "Anna Dalf", "Suson-ru, Incheon", 3021, 10023, 1098505432, ['VIP','Gold'])
cus2 = Customer(543564232, "Chuck Thompson", "Yonsu, Incheon", 4051, 54000, 1043234432, ['VVIP','Premium'])
staff1 = Staff(675843245, "Harrison Tom", "Nam-gu, Incheon", 25, "Cashier", 800000)
staff2 = Staff(703274382, "Jessie Heard", "Suson-ru, Incheon", 17, "Cashier", 900000)

pro1 = Product(13746382943, "Banana", "Brazil", 5.40, 54)
pro2 = Product(78382914563, "Milk", "1000 ml", 4.90, 49)
pro3 = Product(29325467324, "Almond", "500 kg", 7.00, 70)
pro4 = Product(67532956372, "Cacao", "200 g", 3.10, 31)

num = int(input("How many products do you have? : "))

for i in range (0,num):
    code = ''.join(["%s"% randint(0, 9) for num in range(0, 11)])
    name = input("Product name: \n")
    price = float(input("Price: \n"))
    quant.append(int(input("Quantity: \n")))
    point =  int(price)
    pro.append(Product(code, name, " ",price, point))

order = Order(store, cus1, staff1, pro, quant)

order.printReceipt()
    
    
