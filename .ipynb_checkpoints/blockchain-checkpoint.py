from web3 import Web3
import json
from tokenAddress import ERC20TOKEN
from blockchain_database import BlockchainDB


class Blockchain:
    def __init__(self,):
        self.blockchain_name = ''
        self.blockchain = None
        self.accounts = None
        self.transactions_hash = {}

    def connect_to_blockchain(self, blockchain_url, blockchain_name):
        self.blockchain = Web3(Web3.HTTPProvider(blockchain_url))
        self.blockchain_name = blockchain_name
        if self.blockchain.isConnected():
            print(f'{self.blockchain_name} blockchain is successfully connected!')
        else:
            print('Oops, something goes wrong! Please check is url address correct!')

    def get_blockchain_name(self):
        print(f'You are now connected to {self.blockchain_name} blockchain!')

    def update_blockchain(self, blockchain_url, blockchain_name):
        self.blockchain = Web3(Web3.HTTPProvider(blockchain_url))
        self.blockchain_name = blockchain_name
        if self.blockchain.isConnected():
            print(f'{self.blockchain_name} blockchain is successfully connected!')
        else:
            print('Oops, something goes wrong! Please check is url address correct!')

    # This functionality available only with "GANACHE_BLOCKCHAIN"
    def show_accounts_in_blockchain(self):
        if self.blockchain_name == 'Ganache':
            self.accounts = self.blockchain.eth.accounts
            print(self.accounts)
        else:
            print(f'Please switch blockchain {self.blockchain_name} to "Ganache blockchain"')

    def get_balance(self, account_id):
        if self.accounts != None:
            for account in range(len(self.accounts)):
                if account == account_id:
                    print(f'Current balance of account with index {account_id} is '
                          f'{self.blockchain.fromWei(self.blockchain.eth.getBalance(self.accounts[account]),"ether")}'
                          f' ethers')
        else:
            print('There are no available accounts')

    # send transaction from one account to another
    def sendTransaction(self, from_acc, private_key, to_acc, value, blockchain, blockchain_db):
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

        #  We get private_key of account_from to sign transaction, it will allow us send money from particular address
        signed_tx = blockchain.eth.account.signTransaction(tx, private_key)
        tx_hash = blockchain.toHex(blockchain.eth.sendRawTransaction(signed_tx.rawTransaction))
        self.transactions_hash[tx_hash] = {
            'from': from_acc,
            'to': to_acc,
            'value': tx['value']
        }
        blockchain_db.add_record(from_acc, to_acc, value, blockchain_db.conn, 'transactions')
        print('Transaction executed successfully!!!')

    def show_passed_transactions(self):
        print(self.transactions_hash)


main_blockchain = Blockchain()
# main_blockchain.connect_to_blockchain('https://mainnet.infura.io/v3/12a7a8ae4809410cadc3f3f4f4eba0ee', 'Ganache_local_blockchain')
# contract = ERC20TOKEN()
# contract.get_contract(main_blockchain.blockchain, '[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_upgradedAddress","type":"address"}],"name":"deprecate","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"deprecated","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_evilUser","type":"address"}],"name":"addBlackList","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"upgradedAddress","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balances","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"maximumFee","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"_totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"unpause","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_maker","type":"address"}],"name":"getBlackListStatus","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowed","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"paused","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"who","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"pause","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getOwner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"newBasisPoints","type":"uint256"},{"name":"newMaxFee","type":"uint256"}],"name":"setParams","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"amount","type":"uint256"}],"name":"issue","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"amount","type":"uint256"}],"name":"redeem","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"basisPointsRate","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"isBlackListed","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_clearedUser","type":"address"}],"name":"removeBlackList","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"MAX_UINT","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_blackListedUser","type":"address"}],"name":"destroyBlackFunds","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[{"name":"_initialSupply","type":"uint256"},{"name":"_name","type":"string"},{"name":"_symbol","type":"string"},{"name":"_decimals","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"name":"amount","type":"uint256"}],"name":"Issue","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"amount","type":"uint256"}],"name":"Redeem","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"newAddress","type":"address"}],"name":"Deprecate","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"feeBasisPoints","type":"uint256"},{"indexed":false,"name":"maxFee","type":"uint256"}],"name":"Params","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_blackListedUser","type":"address"},{"indexed":false,"name":"_balance","type":"uint256"}],"name":"DestroyedBlackFunds","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_user","type":"address"}],"name":"AddedBlackList","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_user","type":"address"}],"name":"RemovedBlackList","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[],"name":"Pause","type":"event"},{"anonymous":false,"inputs":[],"name":"Unpause","type":"event"}]','0xdAC17F958D2ee523a2206206994597C13D831ec7')
main_blockchain.update_blockchain('HTTP://127.0.0.1:7545', 'Ganache')
blockchain_db = BlockchainDB('blockchain.db')
# blockchain_db.create_table(blockchain_db.conn, 'transactions', 'from', 'to', 'value')
# blockchain_db.drop_table(blockchain_db.conn, 'transactions')
main_blockchain.sendTransaction('0x22141F1D620e0fa4cEceb9791B6a090581ACcD4C',
                                'd57632fca0260902c3acad931e09469c723e4b570e5a36e79900d4a668e6dc5a',
                                '0x3Cfc4262DF1AA19E90Ce5c870d943826601c98ad',
                                1,
                                main_blockchain.blockchain, blockchain_db
                                )

