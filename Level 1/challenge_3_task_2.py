def ask_user_for_number():
    try:
        return int(input("Enter a number: "))
    except:
        print("That is not a number")
        return ask_user_for_number()

def sum_to(n = ask_user_for_number()):
    result = 0
    for i in range(n+1):
        result += i
    return result

def sum_multiples_3_or_5(n = ask_user_for_number()):
    result = 0
    for i in range(n+1):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result

def product_to(n = ask_user_for_number()):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

print("Sum numbers up to: " + str(sum_to()))
print("Sum numbers using only multiples of 3 and 5: " + str(sum_multiples_3_or_5()))
print("Product of numbers up to: " + str(product_to()))