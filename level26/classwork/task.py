#1) შექმენით ფუნქცია multiply რომელიც მიიღებს 2 პარამეტრს (a, b) შემდეგ კი დააბრუნებს მათ ნამრავლს
def multiply(a , b):
    a = 5
    b = 7
    return(a * b)\
    #შექმენით ფუნქცია even_or_odd რომელიც მიიღებს რიცხვს პარამეტრად და დააბრუნებს "Even" თუ ის არის ლუწი, ხოლო "Odd" თუ კენტია
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"