




# # def outer_function():
# #     def first_child():
# #         print("I am first child")
    
# #     def second_child():
# #         print("I am second child")
# #     first_child()
# #     second_child()

# # outer_function()



# def calculator(operator):
#     def add(num1,num2):
#         return num1+num2
#     def product(num1,num2):
#         return num1*num2
#     if operator == '+':
#         return add
#     elif operator =='*':
#         return product


# a = calculator("+") # calculator fucntion reference is given to variable a
# b = calculator("*")

# result = a(10,20)
# print(result)

# result = b(90,70)
# print(result)








#DECORATOR

# def greetings(func):
#     def wrapper():
#         print("Welcome to college")
#         func()
#         print("Welcome again")
#     return wrapper

# @greetings
# def hello():
#     print(f"hello students!")

# hello()


# greet = greetings(hello)
# greet()



def smart_division(func):
    def wrapper(a,b):
        if b == 0:
            return "cannot divide by zero"
        else:
            return func(a,b)
    return wrapper



@smart_division
def divison(a,b):
    return a/b

print(divison(10,2))  # fuction call garda actual ma wrapper function call vairahuncha
print(divison(0,2))
print(divison(2,0))