# 1 برنا مه ای که قا عده و ارتفاع متوازی الا ضلاع را خوا نده، م ساحت آن را
# نمایش می دهد 
# width =  float(input('what is width?'))
# heigth = float(input('what is heigth?'))
# Area = heigth*width
# print('Area is:',Area)


# 2. برنا مه ای که شعاع و ارتفاع ا ستوانه ای را خوا نده، ح جم و م ساحت کل
# # استوانه را محاسبه می کند:
# pi = 22 / 7
# radius = float(input('waht is radius?'))
# heigth = float(input('what is heigth?'))
# voloum = pi* radius**2 *heigth
# Area = ((2*radius**2)*pi) + (heigth*2*radius*pi)
# print('Area is:', Area)
# print('volume is:', voloum)



# string =input('Inter String:')
# rep = int(input('Enter Repeat:'))
# print(string*rep)

# a = int(input('Enter a:'))
# b = int(input('Enter b:'))
# complexx = complex(a,b)
# print(complexx)

# W = int(input('How many liter?'))
# M = 3 *(10**-23)
# L = 950
# tedad = (L / M)*W
# print (tedad)

# S = int(input('How much is yoir salary?'))
# B = 0.07 * S
# M  = 0.1 * S
# P = S - (B + M)
# print('Your Insurance:' , B)
# print('Your tax:' , M)
# print('You recve:', P)

# while True:
#     num = int(input('Enter a nubmer:'))
#     sum = 0
#     for i in range(1, num):
#         if (num % i ==0):
#             sum +=i
#     if(sum ==num):
#         print('Perfected') 
#     else:
#         print('Not Pedfected')
#     yes = str(input('Continue?'))
#     if (yes== 'N' or yes=='n'):
#         break

# n = int(input('Enter a number:'))
# if n == 0:
#     print('0')
# if n ==1:
#     print('0,1')
# elif n>1:
#     result = []
#     a , b = 0,1
#     i = 3
#     while i<n:
#         result.append(a)
#         a , b=b , a+b
#     print(result)
  
# s = input('Enter a string:')
# for i in s:
#     print(i ,end = ' ')

# while True:
#  m = int(input('Enter m:'))
#  tedad = int(input('Enter tedad:'))
#  s = int(input('Enter s:'))
#  k = (12*m) / (12 - tedad * s / 100)
#  p= k / tedad
#  print('k = ', k, '\t' , p)
#  ansi=input('Do you want to continue?')
#  if (ansi == 'n' or ansi =='N'):
#      break

# while True:
#  id = int(input('Enter your Id:'))
#  h = int(input('How many hours did you work?'))
#  hp = int(input('What is your wage per hour?'))
#  salary = hp*h 
#  if h>40:
#   print('Your salaray is:', salary*3/2)
#  else:
#   print('Your salary is:',salary)


# # Q9, P17:
# # n = int(input('Enter n:'))
# # p = int(input('Enter p:'))
# # inc = int(input('Enter inc:'))
# # print ('Year    Price')
# # for i in range(1, n+1):
# #  p = p + (p*inc/100)
# #  print(i , ' ', p)

# # Q11, P18:
# # while True: 
# #  sum = 0
# #  x = int(input("Enter x:"))
# #  y = int (input ("Enter y:"))
# #  if (x == 0 and y == 0): 
# #     break 
# #  temp = y 
# #  if (y < 0):
# #     temp = -y
# #  for i in range(1, temp+1):
# #      sum = sum + x 
# #  if (y < 0): 
# #      sum = -sum 
# #  print(x, " * ", y, " = ", sum)


# # Q12, P18:
# # number = input('Please enter your number:')
# # reverse_number = int(number[::-1])
# # print(reverse_number)

# # pow = 10
# # sum = 0
# # num = int(input("Enter a number:")) 
# # temp = num 
# # while temp > 0: 
# #     sum = (pow * sum) + temp % 10
# #     temp =temp // 10
# # if (sum == num): 
# #     print("Yes") 
# # else: print("No")


# # Q13, P19:
# # m = int(input('Enter m:'))
# # n = int(input('Enter n:'))
# # result = m**n
# # print(result)

# Q1, P19:
# def fibo (n):
#     if (n == 1):
#           return (1)
#     if (n == 2):
#           return (1) 
#     return (fibo (n - 2) + fibo (n - 1)) 
# def main():
#     n = int(input("Enter n:")) 
#     print("Result is:") 
#     for i in range(1, n+1):
#         print (fibo(i), end =" ") 
# main()



# # import struct
# # print(struct.calcsize('P')*8)

# # import platform
# # import os
# # print('Name is:', os.name)
# # print('Platform system is:', platform.system())
# # print('Platform release is:' , platform.release())


# # import site
# # print('Site package is:' , site.getsitepackages())

# # from subprocess import call
# # call(['calc.exe'])


# Q2, P20:
# foot = inch =foot_to_meter=foot_to_centimeter=inch_to_meter=inch_to_centimeter =0
# def read ():
#     foot = int(input("Foot?")) 
#     inch = int(input("Inch?")) 
# def calculate (): 
#     foot_to_meter = 0.3048 * foot 
#     foot_to_centimeter = 100 * foot_to_meter 
#     inch_to_meter = (1.0 / 12)*0.3048* inch 
#     inch_to_centimeter = 100 * inch_to_meter 
# def write(): 
#     print ("The ", foot, " foot is ", foot_to_meter, " meter" ) 
#     print("The ", foot, " foot is ", foot_to_centimeter, " centiMeter") 
#     print("The ", inch, ", inch is ", inch_to_meter ," meter") 
#     print ("The ", inch, ", inch is ",inch_to_centimeter, " centiMeter") 
# def main(): 
#     read () 
#     calculate () 
#     write () 
# main()


# New Book:
# Q3, P150:    
# def main():
#     return (g*m1*m2)/d**2
# g = 10
# m1=int(input('Enter m1:'))
# m2=int(input('Enter m2:'))
# d=int(input('Enter d:'))
# print('f is:') 
# main() 
# 
# 
# from tkinter import *
# import os

# def shutdown():
#     return os.system('shutdown /s /t 1')

# def restart():
#     return os.system('shutdown /r /t 1')

# def logout():
#     return os.system('shutdown -l')

# master =Tk()
# # master.geometry('100')

# master.configure(bg='light blue')

# Button(master, text='Shutdown' , command= shutdown).place(x=20,y=20)
# Button(master, text='Restart' , command= restart).place(x=25,y=50)
# Button(master, text='Log out' , command= logout).place(x=20,y=80)
# mainloop()


# Q11, P156:
# def subdigit(n):
#     if n<10:
#         return n
#     else:
#         q=n
#         sum =0
#         while q>0:
#             sum+=q%10
#             q//=10
#         return sum
# def main():
#     n=int(input('Enter a number:'))
#     print('Result is:', subdigit(n))
# main()  
# 
# 
#           
# Q13, P157:
# import time
# def sum_of_numbers(n):
#     start_time = time.time()
#     s=0
#     for i in range(1, 1+n):
#         s+=i
#     end_time = time.time()
#     return s, end_time-start_time    
# def main():
#  n=int(input('Enter n:'))
#  print('Time to sum of 1 to',n,'and requried time to calculate is:', sum_of_numbers(n))
# main()


# Q15, P159:
# def func(a,b):
#  return (a*b - a/b)
# def main():
#     a = int(input('Enter a:'))
#     b = int(input('Enter b:'))
#     print('Result is:', func(a,b)) 
# main()
# 
#            
# 

#   Q2,P232:
# import numpy as np
# import random
# import numpy.matlib
# def createRandom(arr, n, m):
#     for i in range (0,n):
#         for j in range (0,m):
#             arr[i,j] = random.randint(0,20)
#     return arr
# def printArray(arr, n, m):
#     for i in range(0,n):
#         for j in range(0,m):
#             print(arr[i,j], end= '\t')
#         print()
# def main():
#     n= m =3 
#     a= np.matlib.empty((n,m), dtype = 'i')
#     a= createRandom(a, n, m)
#     printArray(a, n, m)
#     print('=======================')
#     print('Sum is:', np.sum(a))
#     print('Average is:', np.average(a))
#     print('Max rows are:', np.amax(a, axis =1))
#     print('Min columns are:', np.amin(a, axis=0))
# 

# Q7, P238:
# from array import *
# def main():
#     table = array('i', [1000,2000,3000,4000,5000,8000, 10000,20000,30000,50000])
#     sum = 0
#     while True:
#         number = int(input('Enter number:'))
#         if number == -999:
#             break
#         n= int(input('Enter n:'))
#         sum = 0.0
#         i =1
#         while i<=n:
#             code =int(input("Enter code "+ str(i)+":"))
#             if code >=0 and code <10:
#                 sum+= table[code]
#             else:
#                 print('Enter code between 0 to 9')
#                 continue
#             i = i+1
#         print('***Number is', number, 'Sum is', sum)

# main() 


# Q4, P361:

# from typing import List
# def letter_count(str):
#     counts =dict()
#     letters = str.split()
#     for letter in letters:
#         if letter in counts:
#             counts[letter]+=1
#         else:
#             counts[letter]=1
#     return counts
# print(letter_count(input('Enter your letters:')))

 
# s = list(input(int('Enter your list:')))









# 
# Q4, P362:
# def reverse_string(str1):
#     return ''.join(reversed(str1))
# string= input('Enter astring:')
# print(reverse_string(string))


# Q42, P383:
# j= 97
# for i in range(65,91):
#     upCh = chr(i)
#     lowCh = chr (j)
#     print(upCh, '=', i, '\t', lowCh, '=', j, end='\t')

# Q27, P402:
# color_dict = {'red':'#FF0000',
# 'black' :'000000'
# }
# for key in sorted(color_dict):
#     print('%s:%s' %(key, color_dict[key]))


# Q2, P407:
# class User:
#     UserName = 'fanavarienovin'
#     Password=  '123456'
#     def isCorrect(self, userName, password):
#       return self.UserName==userName and self.Password==password
      
# userName = input('Enter userName:')
# password = input('Enter Password:')  
# user1 = User()
# if user1.isCorrect(userName, password):
#     print('Correct')
# else:
#     print('Not Correct!')    


# # Q12, P416:
# yard =int(input('Enter yard:')) 
# meter = 1.96 * yard 
# print('m is:', meter)



# Q1, P426:
# import io
# myFile = open('D:\\data\\1.txt', 'w')
# while True:
#     sentence = input('Enter a sentence:')
#     if len(sentence)!=0:
#         sentence+='\n'
#         myFile.write(sentence)
#     else:
#         break
# myFile.close    


# خودم:
# fo = open('D:\\data\\1.txt', 'w')
# fo.write('Hi Rocket')
# fo.close()

# import os
# if not os.path.exists('D:\\mytestfolder\\'):
#     os.mkdir('D:\\mytestfolder\\')
# fo=open('D:\\data\\1.txt', 'w')
# fo.write('Hi shaqi')
# fo.close()


# Q2, P426:
# import io
# myFile = open('D:\\data\\1.txt', 'a')
# while True:
#     line = input('Enter a sentence:')
#     if line!='':
#         line+='\n'
#         myFile.write(line)
#     else:
#         break
# myFile.close 


# Q3, P426:
import os
fileName = input('Enter a name of file:')
if os.path.exists(fileName):
    myFile = open(fileName, 'r')
    while True:
        line = myFile.readline()
        if line != '':
            print(line, end='')
        else:
            myFile.close()
            break
               
               
# Q6, P428:           
# import os.path
# import time
# print('File :', __file__)
# print('Access time:', time.ctime(os.path.getatime(__file__)))



# Q8,P429:
# import io
# def ReplaceTextFile(urlFile, textReplace, newText):
#     myfileRd= open(urlFile, 'r')
#     myfileWr = open('D:\\data\\1.txt', 'w')
#     while True:
#         line=myfileRd.readline()
#         if line != '':
#             line=line.replace(textReplace, newText)
#             myfileWr.write(line)
#         else:
#             break
#     myfileWr.close()
#     myfileRd.close()
# def main():
#     fileName = input('Enter name of file:')
#     oldString= input('Enter oldString:')
#     newString = input('Enter newString:')
#     ReplaceTextFile(fileName, oldString, newString)
# main()  
# 

# inp = input()
# lst = map(int, inp)
# sortedLst = sorted(lst)
# print(lst)




# print(s.sort())    
# data_list = [ int(x) for x in input("Enter multiple value: ")]
# s = list(input('Enter your data'))
# data_list = [s]
# while True:
#     data = input()
#     if data == "/":
#         break
#     data_list += [data]

# print(s)






# txt = "welcome to the jungle"
# x = txt.split()
# print(x)


# if you import ints without space:
# x = sorted ([int(x) for x in input('Enter your list:')])
# print(list(x))



# if you import ints with space:
# x = sorted ([int(x) for x in input('Enter your list:').split()])
# print(x)


# x = []
# for i in range(10):
#     x.append(i+1)
# print(x)

x= [i+1 for i in range(10)]
print(x)

# x= []
# n = int(input('Enter your numner:'))
# for i in range(n):
#     x.append(i)
# print(x)  




# #code for disabling the softspace feature
# print('G','F','G', sep='')

# #for formatting a date
# print('09','12','2016', sep='-')

# #another example
# print('pratik','geeksforgeeks', sep='@')

# import webbrowser
# url = input('Enter your youtub URL:')
# url = url [:12]+'ss'+url[12:]
# webbrowser.open(url)

# list = [1,2,3,4,5,6,7,8,9]
# print(list[4:])


# import termcolor2
# print (termcolor2.colored('Hello World!', color= 'red'))

# def main ():
#     a = []
#     maxvalue = 0
#     maxcount = 0
#     for i in range (10):
#       a.append(int(input('Enter your list:')))
#     for i in range(10):
#       currentvalue = a[i]
#       currentcount = 0
#       for j in range(10):
#          if a[j] == currentvalue:
#             currentcount+=1
#       if currentcount > maxcount:
#          maxcount=currentcount
#          maxvalue= maxvalue

#     print('maxVlue', maxvalue, "\n max count ", maxcount, "\n a", a)     

# main()



# import pyttsx3
# engine = pyttsx3.int(
# engine.say ('Hi, This is shaghayegh')



# import tkinter as tk
# root = tk.Tk()
# HEIGHT = 500
# WIDTH = 600
# # C = tk.Canvas(root, height=HEIGHT, width=WIDTH)
# # C.pack()
# frame = tk.Frame(root,  bg='#42c2f4', bd=5)
# frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
# textbox = tk.Entry(frame, font=40)
# textbox.place(relwidth=0.65, relheight=1)
# submit = tk.Button(frame, text='Get Weather', font=40)
# #submit.config(font=)
# submit.place(relx=0.7, relheight=1, relwidth=0.3)

# root.mainloop()


# import phonenumbers
# from phonenumbers import geocoder, carrier, timezone

# phone_number = phonenumbers.parse('+989904847919')
# national_f = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.NATIONAL)
# print(national_f) 
# print(phonenumbers.is_valid_number(phone_number))
# print(geocoder.description_for_number(phone_number, 'en'))
# print(carrier.name_for_number(phone_number, 'en'))
# print(timezone.time_zones_for_number(phone_number))

# def password_compare (pass1, pass2):
#     if pass1 != pass2: 
#      print(' not correct')
#      return  False
#     return True 
# for i in range (3):
#     p1 = input('Please enter pass 1:')
#     p2 = input ('Please enter pass 2:')

#     flag = password_compare(p1, p2)

#     if flag == True:
#         print('Password is correct')
#         break
#     print('\n\n', 'Please try again!')    
# password_compare (pass1, pass2)



# def polstar (n):
#     for i in range (n):
#         for j in range (i):
#             print(' ', end= '')
            
#         for j in range(n-i):
#             print('*', end= '')
                
#             print()
# # polstar(10) 

# n=10
# for i in range (10,0,-1):
#     print(" "*n, end= '')
#     print("*" * (2*i-1))
#     n+=1


# a = 100.1342
# print(round(a, 3))