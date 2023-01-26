import sqlite3

class BlockchainDB:
    transactions = {}

    def __init__(self, data_base_path):
        self.conn = sqlite3.connect(data_base_path)
        self.cursor = self.conn.cursor()

    # Creates specific table
    def create_table(self, connection, table_name, tx_hash, from_acc, to_acc, value):
        if self.is_connected_to_db(connection):
            self.cursor.execute(f"CREATE TABLE {table_name}' ('{tx_hash}',{from_acc}', '{to_acc}' text, '{value}' text)")
            BlockchainDB.transactions[table_name] = True
            self.conn.commit()

    # Check if our  file connected to data_base
    def is_connected_to_db(self, connection):
        return connection

    def drop_table(self, connection, table_name):
        if self.is_connected_to_db(connection):
            self.cursor.execute(f"drop table if exists {table_name}")
            print('Table has been deleted successfully!')
            self.conn.close()

    # Add transaction record to table
    def add_record(self, from_acc, to_acc, value, connection, table_name):
        if self.is_connected_to_db(connection):
            self.cursor.execute(f"INSERT INTO {table_name} VALUES (?,?,?)", (from_acc, to_acc, value))
            self.conn.commit()
            self.conn.close()
            print('Record have been added successfully')
            

#
#
# def get_all_customers():
#     # Create connection with db
#     conn = _sqlite3.connect('customers.db')
#     # Create cursor to execute functions
#     c = conn.cursor()
#
#     c.execute("SELECT rowid, * FROM customers")
#
#     conn.commit()
#     print('Executed successfully!')
#
#     customers_list = c.fetchall()
#     for customer in customers_list:
#         print(customer)
#
#     conn.close()
#
#

#
#
# def delete_record(record_id):
#     # Create connection with db
#     conn = _sqlite3.connect('customers.db')
#     # Create cursor to execute functions
#     c = conn.cursor()
#     c.execute(f"DELETE FROM customers WHERE rowId='{record_id}'")
#     print('Executed successfully!')
#     conn.commit()
#
#     conn.close()
#
#
# def get_single_costumer(first_name):
#     # Create connection with db
#     conn = _sqlite3.connect('customers.db')
#     # Create cursor to execute functions
#     c = conn.cursor()
#     c.execute(f"SELECT * FROM customers WHERE first_name='{first_name}'")
#     costumer = c.fetchone()
#     print('Executed successfully!')
#     print(costumer)
#
#
# def add_many_records(customers_list):
#     # Create connection with db
#     conn = _sqlite3.connect('customers.db')
#     # Create cursor to execute functions
#     c = conn.cursor()
#     # add many customers
#     c.executemany("INSERT INTO customers VALUES(?,?,?)", customers_list)
#     # Save and execute function
#     conn.commit()
#     print('Executed successfully!')
#
#     # Close DB  file
#     conn.close()
#
#
# def get_customer_by_id(customer_id):
#     # Create connection with db
#     conn = _sqlite3.connect('customers.db')
#     # Create cursor to execute functions
#     c = conn.cursor()
#     c.execute(f"SELECT * FROM customers WHERE rowId='{customer_id}'")
#     conn.commit()
#     customer_by_id = c.fetchone()
#     print(customer_by_id)
