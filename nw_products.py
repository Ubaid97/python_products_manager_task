import pyodbc # to establish pyodbc connection

class Products:
    def __init__(self):
        # the following block of code is used to establish a pyodbc connection to northwind database
        self.server = "databases1.spartaglobal.academy"
        self.database = "Northwind"
        self.username = "SA"
        self.password = "Passw0rd2018"
        self.northwind_connection = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        # server name - database name - username and password is required to connect to pyodbc
        self.cursor = self.northwind_connection.cursor()

    # function that prints out the average value of all items in the products table
    def products_avg_value(self):
        # running sql query to select the average unit price of all items in the products table
        avg_value = self.cursor.execute("SELECT AVG(UnitPrice) FROM Products").fetchone()
        print(type(avg_value)) # this lets me know that avg_value is a list
        # avg_value has one item, so to print that item by itself, it will selected using its index [0]
        print(f"this is the average value of all our stock items: {avg_value[0]}") # prints out the avg_value of the items in products table