

def exception(cls):
    new_cls = type(cls.__name__, (cls, Exception), {})
    new_cls.__module__ = cls.__module__
    new_cls.__doc__ = cls.__doc__
    return new_cls


@exception
class InsufficientFundsError:
    def __init__(self, balance, amount, minimum_balance):
        self.balance = balance
        self.amount = amount
        self.minimum_balance = minimum_balance  
        self.message = (
            f"Insufficient funds: Current balance {balance}, "
            f"attempted withdrawal {amount}, "
            f"minimum required balance {minimum_balance}."
        )
        super().__init__(self.message)


@exception
class InvalidTransactionError:
    def __init__(self, amount):
        self.amount = amount
        self.message = (
            f"Invalid transaction: {amount}. "
            "Withdrawal amount must be greater than 0."
        )
        super().__init__(self.message)

def process_withdrawal(prompt, current_balance, minimum_balance):
    execute = True
    while execute:
        user_input = input(prompt).strip()
        
        try:
            amount = float(user_input)
            if amount <= 0:
                raise InvalidTransactionError(amount)
            
            if current_balance - amount < minimum_balance:
                raise InsufficientFundsError(current_balance, amount, minimum_balance)
            
            return amount
        
        except ValueError:
            print("Please enter a valid amount (amount must be number).")
        except InvalidTransactionError as e:
            print(f"{e}")
        except InsufficientFundsError as e:
            print(f"{e}")


amount = process_withdrawal("Enter withdrawal amount: $ ", 1000.00, 100.00)
print(f"Withdrawal successful: $ { amount}")
print(f"New balance: ${1000.00 - float(amount)}")
print()