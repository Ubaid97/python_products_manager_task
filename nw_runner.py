# importing Products table to inherit its connection to northwind db and function for getting the avg value of items
from nw_products import Products

stock_dept = Products() # creating an instance of the Products class
stock_dept.products_avg_value() # calling and executing function in Products class that gets and prints the average value of all stock items in the products table
