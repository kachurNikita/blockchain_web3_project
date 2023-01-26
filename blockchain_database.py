import sqlite3

class BlockchainDB:
    transactions = {}

    def __init__(self, data_base_path):
        self.conn = sqlite3.connect(data_base_path)
        self.cursor = self.conn.cursor()

    # Creates specific table
    def create_table(self, connection, table_name, tx_hash, from_acc, to_acc, value):
        if self.is_connected_to_db(connection):
            self.cursor.execute(f"CREATE TABLE {table_name} ('{tx_hash}','{from_acc}', '{to_acc}' text, '{value}' text)")
            BlockchainDB.transactions[table_name] = True
            self.conn.commit()

    # Check if our file connected to data_base
    def is_connected_to_db(self, connection):
        return self.conn

    # delete table
    def drop_table(self, connection, table_name):
        if self.is_connected_to_db(connection):
            self.cursor.execute(f"drop table if exists {table_name}")
            print('Table has been deleted successfully!')
            self.conn.close()

    # Add transaction record to table
    def add_record(self, tx_hash, from_acc, to_acc, value, connection, table_name):
        if self.is_connected_to_db(connection):
            self.cursor.execute(f"INSERT INTO {table_name} VALUES (?,?,?,?)", (tx_hash, from_acc, to_acc, value))
            self.conn.commit()
            self.conn.close()
            print('Record have been added successfully')

