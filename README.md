# Blockchain_1
Wallet has one owner. Wallet is able to receive funds no matter what, and it is possible for the owner to spend funds on any kind of address.
It is possible to allow certain people to spend up to a certain amount of fund. 
Had set the new owner with 3 out of 5 guardians in case the funds are lost. This is for, if the owner loses his private key,there should be some kind of recovery functionality.
The Solidity code comprises two contracts: consumer and SmartContractWallet. 
Let's break down each part:
	
1.Consumer Contract:	  
  This contract has two functions:
getbalance(): It returns the balance of the contract.
deposit(): It allows anyone to send Ether to the contract.

2.SmartContractWallet Contract:
      This contract constitutes a wallet-like smart contract with multi-signature capabilities. Let's explain each part:

State Variables:__

owner: Stores the address of the current owner of the wallet.

allowance: Maps addresses to the amount they are allowed to spend from the wallet.

isAllowedToSend: Maps addresses to boolean values indicating whether they are allowed to send funds from the wallet.

guardians: Maps addresses to boolean values indicating whether they are guardians of the wallet.

nextOwner: Stores the address proposed to be the next owner.

nextOwneGuardianVotedBool: Maps addresses to another mapping of addresses to boolean values, indicating whether a guardian has voted for a proposed new owner.

guardiansResetCount: Tracks the number of guardians who have confirmed a new owner proposal.

confirmationsFromGuardiansForReset: Defines the required number of guardian confirmations for a new owner proposal.

Constructor:__

Initializes the owner with the address of the deployer of the contract.

Functions:
setGuardian: Allows the current owner to set or remove a guardian for the wallet.

proposeNewOwner: Allows guardians to propose a new owner for the wallet. After a certain number of confirmations from guardians, the new owner is set.

setAllowance: Allows the owner to set the allowance for an address to spend from the wallet.

transfer: Allows any address (owner or allowed address) to transfer funds from the wallet to another address.

receive: Fallback function to receive Ether.

This contract enables features like multi-signature ownership, setting allowances for spending, and transferring funds with proper authorization checks.
