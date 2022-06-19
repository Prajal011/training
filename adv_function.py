# # # # def square_root(num):
# # # #     return num**0.5

# # # # sq = square_root
# # # # ans = sq(100)
# # # # print(square_root(25))
# # # # print(f"square root {ans}")



# # # def welcome (name):
# # #     print(f"Welcome {name}!")

# # # def greet_ram(a):
# # #     a("Ram")

# # # greet_ram(welcome)

# # def welcome (name):
# #     return f"Welcome {name}!"

# # def greet_ram(a):
# #     return a("Ram")

# # print(greet_ram(welcome))


# def total (num1,num2):
#     return num1+num2

# def square_root(func):
#     return(func(50,50)**0.5)


# print(square_root(total))
# 



def total(num1 , num2):
    return num1 + num2

def square(func,num1,num2):
    return(func(num1,num2)**0.5)


print(square(total,250,250))