import pyodbc


class DatabaseConnection:
    def __init__(self, server, database, driver):
        self.server = server
        self.database = database
        self.driver = driver
        self.connection = None
        self.cursor = None

    def __enter__(self):
        connection_string = (
            f'DRIVER={self.driver};'
            f'SERVER={self.server};'
            f'DATABASE={self.database};'
            'Trusted_Connection=yes;'
        )
        self.connection = pyodbc.connect(connection_string)
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Close the cursor
        if self.cursor:
            self.cursor.close()
        # Close the connection
        if self.connection:
            self.connection.close()

    def execute_query(self, query):
        try:
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return rows
        except pyodbc.Error as e:
            print(f"An error occurred: {e}")
            return None


class DatabaseUtils:
    def add_new_customer(self, db, username, password):
        query = f'INSERT INTO Customer (username, password) VALUES (\'{username}\', \'{password}\');'
        db.execute_query(query)

    def customer_exists(self, db, username):
        query = f'SELECT * FROM Customer WHERE username = \'{username}\';'
        rows = db.execute_query(query)
        return len(rows) > 0

    def add_new_product(self, db, name, image_path):
        query = f'INSERT INTO Product (name, image_path) VALUES (\'{name}\', \'{image_path}\');'
        db.execute_query(query)

    def get_all_products(self, db):
        query = 'SELECT * FROM Product;'
        result = db.execute_query(query)
        return result

    def get_cart(self):
        pass

    def update_cart(self):
        pass


server = r'MRMODYHPPAVILIO\SQLEXPRESS01'
database = 'EcommerceDB'
driver = '{ODBC Driver 17 for SQL Server}'
