# SmartContractWallet and Consumer Contracts

This repository includes two Solidity smart contracts: `SmartContractWallet` and `consumer`. The `SmartContractWallet` contract offers a secure way to manage funds with guardianship features and allowances, while the `consumer` contract is a simple contract to demonstrate balance checks and deposits.

## Contracts

### SmartContractWallet

The `SmartContractWallet` contract provides functionalities for secure fund management:
- **Ownership Management**: The contract starts with the deployer as the owner. Ownership can be transferred with confirmation from multiple guardians.
- **Allowance System**: The owner can set allowances for other addresses, which are then restricted by an allowance limit.
- **Guardian System**: Guardians can propose a new owner, and once a sufficient number of guardians agree, the ownership can be transferred.
- **Fund Transfer**: Allows sending funds to other addresses with a specified payload, and enforces allowance constraints.

**Key Functions:**
- `setGuardian(address _guardian, bool _isGuardian)`: Set or remove a guardian.
- `proposeNewOwner(address payable _newOwner)`: Propose a new owner for the wallet.
- `setAllowance(address _for, uint _amount)`: Set or remove allowances for an address.
- `transfer(address payable _to, uint _amount, bytes memory _payload)`: Transfer funds to another address with a payload.
- `receive() external payable`: Receive Ether.

### consumer
The `consumer` contract provides basic functionality to deposit funds and check the balance.

**Key Functions:**
- `getbalance()`: Retrieve the balance of the contract.
- `deposit()`: Deposit Ether into the contract.

## Deployment Instructions
1. **Install Dependencies**
   Make sure you have Node.js and npm installed. If using Truffle or Hardhat, install necessary dependencies:
   ```bash
   npm install @openzeppelin/contracts
   
2. Compile Contracts
 Compile the smart contracts using a Solidity compiler such as solc, or through a development environment like Truffle or Hardhat.

3. Deploy Contracts
 --Deploy SmartContractWallet: Deploy this contract first. It will initialize with the deployer 
 as the owner.
 --Deploy consumer: Deploy this contract as needed to interact with the wallet.
   
5. Interact with Contracts
   
 -- Manage Guardians and Ownership
   
// - javascript code
// Set a guardian
await smartContractWallet.setGuardian('0xGuardianAddress', true);
// Propose a new owner
await smartContractWallet.proposeNewOwner('0xNewOwnerAddress');

 -- Set Allowances

// - javascript code
await smartContractWallet.setAllowance('0xAddressWithAllowance', 1000);

 -- Transfer Funds
 
 // - javascript code
await smartContractWallet.transfer('0xRecipientAddress', 500, "0xPayload");

 -- Deposit and Check Balance

 // - javascript code
// Deposit Ether into consumer contract
await consumer.deposit({ value: web3.utils.toWei('1', 'ether') });

// Check balance
let balance = await consumer.getbalance();
