####################
HnM
####################
*********************
Inventory Control
*********************


OVERVIEW: 
============
Using the new ways of shopping customers have the opportunity to choose
between different suppliers based on the availability of product, choices
available for that product and the difference in prices. All this not only
provied added benefits to buyers  but it also incresed the competition
among the suppliers. They need to make sure that their inventory system is
updated all the tyme informationthey have about their invetory is also updated
and in addition to this they should have the stock available. Either we talk about
online or in store shopping invetory management techniques make a big
difference.

Think about when you are shopping in Macys and you can not find your size or
color or you want to know if store hasadditional choices available related to tha
item,  you ask the customer service representative to scan the item and check if
they have that item for your size or in different colors. Representative scans it
for us and can inform us right  away if item is availabe or not. The scanner is just
reading the database for the item availability and different sub catagories for
size and color related to taht item. This is  possible because the store is contrling
the inventory system using the *PERPETUAL INVENTORY*  system, which not only
updates the records in real time  also reduces the risk of theft. 


PERSONAS:
==================

Hadi:
--------------
Bussiness owner, Mr. Hadi starts a new business a shoe store. he is planning to
expand his bussiness. With the idea of expansio he also realizes that this is the
time when hinstead of  inventory counting method he should have automated
system of inventory.  This will help him to keep records handy all the time.

Mujju:
--------------
Mr. Hadi hired Mujju and his team  to develop a program for his company
to keep the automated record of inventory. 

GOALS:
------------------

This program will do the following:

-  Keep record of added inventory
- Items added
- Items sold
- Count the total left in inventory.
- Calculate the profit  earned. 


PROBLEM SCENARIO:
====================

Mr. Hadi has faced difficulty to find exactly the shoe for his customers
Based on his records and memory he knows that he has that item in his
store but can't find it. At las he comes up to a conclusion that the item is
lost. Ths type of situation not only causes to loose a business opportunity
but a 100% loss for that item as he can't even reccover the cost. Also,
counting the inventory takes more time. Mujju and his team need to make 
sure that the info provided in books for the availability of goods and sales
are accurate. The accurate numbers are important to keep maintain correct
records in future. Keeping in mind, though companies have automated
systems but once in a week/month or atleast once in a  year they domaual
inventory count.  The numbers through both inventory systems should match.


USER STORIES:
====================
The software will help the business not only to keep updated their inventory
records but also to kee track of sales and profits earned. As every thing is
automated this will make possible to redue the risk of inventory theft.
By gathereing the info about the types of items store carries, the amount
available for the items, and the cost of purchase softwre is developed and 
implemented.


ACCEPTANCE STORIES:
====================

Scenario 1: 
---------------------------------

**Adding New Item**


|**Given** New items need to be added to inventory
|**And**    Would like to add them
|**When** Click the  *Add* button
|**Then**  (I will be taken to a  screen to enter  information
Item Name, Serial Number, Description, Sizes Available, Quantity and
Cost of item. Calculate purchase price (item Quantity purchased x cost)
This will help to record Profit and Loss )

|**And**  The *Total Quantity* will be updated.


Scenario 2: 
---------------------------------

**Selling An Item**

**Given** Item is sold
**And**   Would lik to update related info
**When** Click the  *Sold* button
**Then**  I will be taken to a  screen to enter  information
Item Name, Serial Number,Price, Date sold, cost
**And**  Updates will be made for : *Quantity left ( Begining - Available)*,
*Profit(Price-cost of item)*, * Total Earned ( accumulation of earned)*
| 
Scenario 3: 
---------------------------------

**Recording Lost, Stolen, Damaged Item and Loss** 

| **Given** Item is in inventory list but can not be found or is damaged
| **And**    Would lik to update related info
| **When** Click the  *Write off Item* button
| **Then**  I will be taken to a  screen to enter  information 
Item Name, Serial Number, Cost, Size, Quantity

| **And**   Calculations will be for : *Loss = Quantity Lost x cost * , not using 
this number in program as this is relevant  for accounting purposes.

Updates will me made for *Quantity Available* for that size and type  of shoe. Quantity Available will be reduced b the Quantity lost 
