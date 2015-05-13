#!/usr/bin/env python
# -*- coding: utf-8 -*-

def DisplayMenu():
    print "1- Add Item\
    2-Search Item\
    3- Item Sold\
    4- Exit"
    
DisplayMenu()   
CHOICE = raw_input(int('Choose Action'))
while CHOICE != 4: # Class Reference
    if CHOICE ==1:
        Additem(parameters) # Class Reference
    elif CHOICE == 2:
        Searchitem(parameter) # Class Reference
    else:
        Itemsold(parameters) # Class Reference
DisplayMenu()

def  AddItem(Stock_Num,Category,Item_Name,Color,Size,
             Purchased,Quantity_Available,Cost):
    print 'add item function'
    
def Get_Item_Descr():
    
    Stock_number = raw_input('Stock number')
    Category = raw_input('Item Categoy')
    Item_Name = raw_input('Item NAme')
    Color = raw_input('Item Color')
    Size = raw_input('Item Size')
    Purchased = raw_input('Quantity Purchased')
    # Quantity_Available = raw_input(
    Cost = raw_input('Item Cost')
