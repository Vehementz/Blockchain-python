# Crate a blockhain project

blockchain = []


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    """ Append a new value as well as the last blockchain value to the blockchain value to the block"""
    blockchain.append([last_transaction,
                       transaction_amount])


def get_transaction_value():
    """Return the input of the user (a new transaction amount) as a float"""
    return float(input('Your transaction amount please: '))


tx_amount = get_transaction_value()
add_value(tx_amount)


def get_user_choice():
    user_input = input("Your choice: ")
    return user_input


def print_blockchain_elements():
    for block in blockchain:
        print('Out putting Block')
        print(block)


tx_amount = get_transaction_value()
add_value(tx_amount)
# add_value(last_transaction=get_last_blockchain_value(),transaction_amount=tx_amount)

# tx_amount=get_user_input()
# add_value(tx_amount, get_last_blockchain_value())

while True:
    print("Please choose")
    print("1: Add a new transaction value")
    print("2: Output the blockchain blocks")
    print("q: Quit")
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice  == 'q':
        break
    else:
        print("Input was invalid, please pick a value from the list!")
    print("Choice registered! ")

# print(blockchain)
