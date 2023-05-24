# #Q1
# #Removing duplicates in lists without set() function
# t = [1, 2, 3, 1, 2, 5, 6, 7, 8]
# s = []
# for i in t:
#     if i not in s:
#         s.append(i)
# s  


# #Q2
# #Input password for 3 times
# def pass_word():
#     pass1 = int(input('please enter your pass1:'))
#     pass2 = int(input('please enter your pass2:'))
    
#     if pass1 == pass2:
#         print('pass is correct.')
#     else:
#         print('pass is not correct.')
#         for i in range(3): 
#             pass_word()
#             break       

# pass_word() 


# #Q3
# myList = ['ali', 'ahmad', 'shayan']
# for i in myList:
#         print('salam', i)



# #Q4
# #we want to create a 5x5 matrix
# #x is row, y is column
# n= 5
# a = []
# for x in range(n):
#     b= []
#     for y in range(n):
#         b.append(x+5*y)
#     a.append(b)         
# a  


# #Q5
# # set() omits repetititve items and can sort items. 
# a7 = [13, 18, 20 , 15, 15, 18, 19, 'hello', 'hello' , 19]
# se3 = set(a7)
# se3

# #Q6
# #یک راه دیگه تعریف دیکشنری1
# c_101 = dict()
# c_101[1] = 's-g'
# c_101[2] = 'f-e'
# c_101[3] = 's-k'
# c_101[4] = 's-r'
# c_101


# #یک راه دیگه تعریف دیکشنری2
# c_102 = {
#     5: 's+s',
#     6: "f+f",
#     7: 's_s',
#     8: 's_s',
#     9: 'ss_ss'
# }
# c_102


# #یک راه دیگه تعریف دیکشنری3
# thisdict = dict(brand = "Ford", model = "Mustang", year = 1964)
# thisdict


# #Q7
# #linear matrix 
# n = 5
# m= 4
# b = [[x+5*y for x in range(n)] for y in range(m)]
# b

# #Q8
# #add new items to dictionary via d[]=[]
# def func1(d):
#     d['fisrt'] = [1,2,3]
    
# dic = {'first': {1:1}, 'second': {2, 'a'}}
# print(dic)
# func1(dic)
# print(dic)



# #Q9
# #this code print keyes in default
# dic ={'first': 1, 'second': 2, 'third': 3}
# for i in dic:
#     print(i)


# #Q10
# # FANNI, 21/05/00


# # Q11
# # FANNI, 21/05/00


# #Q12
# import pandas as pd
# import numpy as np
# ser = pd.Series()
# print(ser)
# data = np.array(['g', 'e', 'e', 'k', 's'])
# ser = pd.Series(data)
# print(ser)

# #omit number rows
# print(ser.to_string(index=False))


# #Q13
# #lottary
# import random
# A = ['elizabet', 'melanee', 'rosalee']
# B = random.randint(0, len(A))
# C = A[B]
# print(C)

#Q14
# def average ():
#     n = eval(input('enter n:'))
    
#     sum = 0
#     for i in range (n):
        
#         x = eval(input('enter number:'))
#         sum = sum +x
#     print('average is:', sum/n)  
# average()


# #Q15 ASCII
# o = 'شقایق'
# #حروف فارسی بیت بیشتری دارند 16 بیتی هستند
# for i in range (len(o)):
#     print(ord(o[i]), '*', end = ' ')
    
# #Q16
# #Remove spaces at the beginning and at the end of the string:
# txt = "     banana     "
# x = txt.strip()
# print("of all fruits", x, "is my favorite")


# #Q17
# #Remove spaces to the left of the string:
# txt = "     banana     "
# x = txt.lstrip()
# print("of all fruits", x, "is my favorite")


# #Q18
# A = [64, 25, 64, 12, 22, 11]
# def selection_sort(A):
#     for i in range(len(A)):
#         min_idx = i
#         for j in range (i+1, len(A)):
#             if A[min_idx] > A[j]:
#                 min_idx = j
                
#         A[i], A[min_idx] = A[min_idx], A[i]
        
#     print('Sorted array', end =':')
#     print(A)
# print('Input array:', A, '\n')
# selection_sort(A)

# #Q19
# x = sorted ([int(x) for x in input('Input array:').split()])
# print('Sorted array is:', x)

# #Q20
# #به ترتیب حروف الفبا مرتب می کنه
# x =  ['shaha', 'zeinab', 'arezoo']
# l = sorted(x)
# print(l)


#Q21
# import schedule, requests, time 
# text= ''' سلام من ربات مِلانی ام. اگه پست های این چنل رو دوست دارید لطفا برای بقیه فوروارد کنید.
# @melaneepython
# '''
# # LINK_1_FORMAT => https://api.telegram.org/bot<ENTER_BOT_TOKEN>/getUpdates
# #https://core.telegram.org/bots/api
# # LINK_2_FORMAT => https://api.telegram.org/bot<ENTER_BOT_TOKEN>/sendMessage?chat_id=<ENTER_CHAT_ID>&text="ENTER YOUR TEXT"
# def bot():
#     requests.get(f""" https://api.telegram.org/bot<ENTER_BOT_TOKEN>/sendMessage?chat_id=<ENTER_CHAT_ID>&text={text}"""")
# schedule.every(1).day.at("19:30").do(bot)
# while True:
#     schedule.run_pending()
#     time.sleep(1)

#Q22
# from requests import get
# ip = get('https://api.ipify.org').content.decode('utf8') 
    #https://api.ipify.org is endpoint
# print('My public IP address is: {}'.format(ip))



#Q23 Public IP in linux
#sudo apt install curl
#curl ifconfig.me
#dig TXT +short o-o.myaddr.l.google.com @ns1.google.com

#Q24
# import requests
# import time

# def get_public_ip():
#     response = requests.get('https://api.ipify.org').text
#     return response

# interval = 5  # Interval in seconds
# while True:
#     public_ip = get_public_ip()
#     print(f'Public IP: {public_ip}')
#     time.sleep(interval)














