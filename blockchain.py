# Crate a blockhain project

from ast import Break

MINING_REWARD = 10

genesis_block = {
       'previous_hash': '',
        'index': 0,
        'transactions': []
}

blockchain = [genesis_block]
open_transactions = []
owner = 'Clement'
participants = {'Clement'}


def hash_block(block):
    return '_'.join([str(block[key]) for  key in block])


def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]    
    amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]
    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]    
    amount_received = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_received += tx[0]
    return amount_sent, amount_received - amount_sent

def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1.0):
    """ Append a new value as well as the last blockchain value to the blockchain value to the block
    
    Arguments: 
        :sender: The sender of the coins.
        :recipient: The recipeint of the coins.
        :amount: The amount of coins sent with the transaction (default = 1.0)
    """
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    open_transactions.append(transaction)
    participants.add(sender)
    participants.add(recipient)


    # if last_transaction == None:
    #     last_transaction = [1]
    # # blockchain.append([last_transaction,
    # #                    transaction_amount])

def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    reward_transaction = {
        'sender': 'MINING',
        'recipient': owner,
        'amount': MINING_REWARD
    }

    open_transactions.append(reward_transaction)
    block = {   
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': open_transactions
    }
    blockchain.append(block)
    return True


def get_transaction_value():
    """Return the input of the user (a new transaction amount) as a float"""
    tx_recipient = input('Enter the recipient of the transaction:')
    tx_amount = float(input('Your transaction amount please: '))
    return (tx_recipient, tx_amount) 

tx_amount = get_transaction_value()
add_transaction(tx_amount)


def get_user_choice():
    user_input = input("Your choice: ")
    return user_input


def print_blockchain_elements():
    for block in blockchain:
        print('Out putting Block')
        print(block)
    else: 
        print("-" * 30)
        print("-" * 30)

def verify_chain():
    # block_index = 0
    is_valid = True
    for block_index in range(len(blockchain)):
        # Below is rewritted above
        for (index, block) in enumerate(blockchain):
            if index == 0:
                continue
            if block['previous_hash'] != hash_block(blockchain[index - 1]):
                return False
        return True

            # if block_index == 0:
            #     block_index += 1
            #     continue
            # elif blockchain[block_index][0] == blockchain[block_index - 1]:
            #     is_valid = True
            # else: 
            #     is_valid = False
            


    #         break
    #     return is_valid
    


# tx_amount = get_transaction_value()
# add_value(tx_amount)
# add_value(last_transaction=get_last_blockchain_value(),transaction_amount=tx_amount)

# tx_amount=get_user_input()
# add_value(tx_amount, get_last_blockchain_value())

waiting_for_input = True


while waiting_for_input:
    print("Please choose")
    print("1: Add a new transaction value")
    print("2: Mine a new block")
    print("3: Output the blockchain blocks")
    print("4: Output participants")
    print("h: Manipulate the chain")
    print("q: Quit")
    user_choice = get_user_choice()
    if user_choice == '1':  
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print(participants)  
    elif user_choice == "h":
        if len(blockchain) >=1:
            blockchain[0] = [2]
    elif user_choice  == "q":
        waiting_for_input = False
    else:
        print("Input was invalid, please pick a value from the list!")
    if not verify_chain():
        print("Invalid blockchain !")
        break
    print(get_balance('Clement'))
else: 
    print("User left!")

    print("Choice registered! ")

# print(blockchain)
