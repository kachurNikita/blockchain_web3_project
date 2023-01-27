from web3 import Web3
import json
from blockchain_database import BlockchainDB
from blockchain_nodes_and_addresses import \
    ganache_local_blockchain, \
    address_from, \
    address_from_private_key,\
    address_to


class Blockchain:
    def __init__(self,):
        self.blockchain_name = ''
        self.blockchain = None
        self.accounts = None
        self.transactions_hash = {}

    # create blockchain  connection
    def connect_to_blockchain(self, blockchain_url, blockchain_name):

        # simple validation
        assert blockchain_name != '', 'Please provide blockchain name'
        assert blockchain_url != '', 'Please provide blockchain URL'

        self.blockchain = Web3(Web3.HTTPProvider(blockchain_url))
        self.blockchain_name = blockchain_name
        self.accounts = self.blockchain.eth.accounts
        if self.blockchain.isConnected():
            print(f'{self.blockchain_name} blockchain is successfully connected!')
        else:
            print('Oops, something goes wrong! Please check is url address correct!')

    def get_blockchain_name(self):
        print(f'You are now connected to {self.blockchain_name} blockchain!')

    def show_accounts_in_blockchain(self):
        self.accounts = self.blockchain.eth.accounts
        print(self.accounts)

    def get_balance(self, account_id):
        min_index = 0
        max_index = len(self.accounts) - 1
        while min_index <= max_index:
            middle_index = (min_index + max_index) // 2
            if middle_index == account_id:
                return f'account value is: {self.blockchain.fromWei(self.blockchain.eth.getBalance(self.accounts[middle_index]),"ether")}'
            elif middle_index > account_id:
                max_index = middle_index - 1
            elif middle_index < account_id:
                min_index = middle_index + 1
        return f'There is no account with id: {account_id}'

    # send transaction from one account to another
    def send_transaction(self, from_acc, private_key, to_acc, value, blockchain, blockchain_db):
        while True:
            sender_name = input('Please provide your name: ')

            if sender_name:
                break

        # create nonce to keep truck all transactions with current account
        nonce = blockchain.eth.getTransactionCount(from_acc)
        # Specify or define transaction object
        tx = {
            'nonce': nonce,
            'from': from_acc,
            'to': to_acc,
            'value': blockchain.toWei(value, 'ether'),
            'gas': 2000000,
            'gasPrice': blockchain.toWei('50', 'gwei')
        }

        # We get private_key of account_from to sign transaction, it will allow us to send money from particular address
        signed_tx = blockchain.eth.account.signTransaction(tx, private_key)
        tx_hash = blockchain.toHex(blockchain.eth.sendRawTransaction(signed_tx.rawTransaction))
        self.transactions_hash[tx_hash] = {
            'from': from_acc,
            'to': to_acc,
            'value': tx['value']
        }
        blockchain_db.add_record(tx_hash, from_acc, to_acc, value, 'transactions', sender_name)
        print('Transaction executed successfully!!!')

    def show_passed_transactions(self):
        print(self.transactions_hash)


main_blockchain = Blockchain()
main_blockchain.connect_to_blockchain(ganache_local_blockchain, 'Ganache')
blockchain_db = BlockchainDB('blockchain.db')
print(main_blockchain.get_balance(9)
)
# blockchain_db.create_table('transactions', 'tx_hash', 'from', 'to', 'value', 'sender')
# main_blockchain.send_transaction(address_from, address_from_private_key,
#                                  address_to, 1,
#                                  main_blockchain.blockchain, blockchain_db)
# main_blockchain.show_accounts_in_blockchain()
