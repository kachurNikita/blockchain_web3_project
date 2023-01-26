import json


class ERC20TOKEN:
    def __init__(self):
        self.tokenName = ''
        self.tokenContract = None
        self.total_token_supply = 0

    # get specific contract
    def get_contract(self, blockchain, contract_Abi, contract_address):
        if self.web3_is_connected(blockchain):
            abi = json.loads(contract_Abi)
            self.tokenContract = blockchain.eth.contract(address=contract_address, abi=abi)
            self.tokenName = self.tokenContract.functions.name().call()

    # set contract name
    def set_contract_name(self, blockchain):
        if self.web3_is_connected(blockchain):
            self.tokenName = self.tokenContract.functions.name().call()

    # Check are we connected to blockchain
    def web3_is_connected(self, blockchain):
        return blockchain.isConnected()

    # get contract name
    def get_token_contract_name(self):
        print(self.tokenName)

    # shows total token supply
    def set_total_token_supply(self):
        self.total_token_supply = self.tokenContract.functions.totalSupply().call()

    def get_total_token_supply(self, tokenName):
        print(f'Maximum token supply {self.total_token_supply} {tokenName}')

    def get_last_blockchain_block_number(self, blockchain):
        if self.web3_is_connected(blockchain):
            blockchain_block_number = blockchain.eth.get_block_number()
            print(f'The last blockchain number is {blockchain_block_number}')

    # 'latest', 'earliest', 'pending', 'safe', 'finalized'
    def get_blockchain_block_data(self, blockchain, block_in_chain):
        if self.web3_is_connected(blockchain):
            block_data = blockchain.eth.get_block(block_in_chain)
            print(block_data)
