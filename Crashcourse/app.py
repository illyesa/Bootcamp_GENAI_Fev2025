from main import add, subtract

def calculate_numbers(a, b, fn):
    if fn == 'add':
        return add(a, b)
    elif fn == 'subtract':
        return subtract(a, b)
    else :
        print("error")
        return 0
print(calculate_numbers(1, 4, 'add'))  # This should work - we're able to access 'add' from the helpers file!