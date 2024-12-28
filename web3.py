from web3 import Web3


w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

w3.eth.defaultAccount = w3.eth.accounts[0]

contract_address = 'YOUR_CONTRACT_ADDRESS'
contract_abi = 'YOUR_CONTRACT_ABI'

contract = w3.eth.contract(address=contract_address, abi=contract_abi)


result = contract.functions.getPropertyOwner('PROPERTY_ID').call()
print(result)
