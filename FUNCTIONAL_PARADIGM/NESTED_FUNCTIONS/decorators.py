# A decorator is a function that takes another function as an argument
# and extends its behavior without changing the original function explicitly
# and return another already wrapped function or closure.

from functools import wraps

def net_price(price, tax):
    """ calculate the net price from price and tax
    Arguments:
        price: the selling price
        tax: value added tax or sale tax
    Return
        the net price
    """
    return price * (1 + tax)

def currency(func):
    """The currency function returns the wrapper function. The wrapper function has the *args and **kwargs parameters.
    These parameters allow you to call any func function with any combination of positional and keyword-only arguments.
    Also here is a wraps-decorator from functools-module that dacorates wrapper function for returning by updating it.
    It helps us not lose the original documentation of the functions that we need to decorate."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"${result}"
    return wrapper

net_price = currency(net_price)
print(net_price(10, 0.5))


# Here is a more convinient way and syntax to decorate functions.
@currency
def add_money(banknotes, pennies):
    """Adds banknotes and pennies""" 
    return banknotes + pennies

print(add_money(100, 0.50))

print(help(net_price))
print(help(add_money))
print()
print(net_price.__name__)
print(add_money.__name__)
print()
print(net_price.__doc__)
print(add_money.__doc__)




