import sqlite3


class BlockchainDB:
    transactions = {}

    def __init__(self, data_base_path):
        self.conn = sqlite3.connect(data_base_path)
        self.cursor = self.conn.cursor()

    # Creates specific table
    def create_table(self, table_name, tx_hash, from_acc, to_acc, value, sender):
        self.cursor.execute(f"CREATE TABLE {table_name} ('{tx_hash}','{from_acc}', '{to_acc}', '{value}', {sender})")
        BlockchainDB.transactions[table_name] = True
        self.conn.commit()

    # delete table
    def drop_table(self, table_name):
        self.cursor.execute(f"drop table if exists {table_name}")
        print('Table has been deleted successfully!')
        self.conn.close()

    # Add transaction record to table
    # tx_hash, from_acc, to_acc, value, blockchain_db.conn, 'transactions', sender_name
    def add_record(self, tx_hash, from_acc, to_acc, value, table_name, sender):
        self.cursor.execute(f"INSERT INTO {table_name} VALUES (?,?,?,?,?)", (tx_hash, from_acc, to_acc, value, sender))
        self.conn.commit()
        self.conn.close()
        print('Record have been added successfully')

