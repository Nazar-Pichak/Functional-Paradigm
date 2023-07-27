import colorama

# Nested functions

global_ = 'Black'

def colors():
    enclosing = 'Yellow'
    def print_red():
        local = 'Red'
        print(colorama.Fore.RED + local, colorama.Fore.YELLOW + enclosing, colorama.Fore.BLACK + global_ + colorama.Fore.RESET)

    def print_green():
        local = 'Green'
        print(colorama.Fore.GREEN + local, colorama.Fore.YELLOW + enclosing, colorama.Fore.BLACK + global_ + colorama.Fore.RESET)

    print_red()
    print_green()

colors()
