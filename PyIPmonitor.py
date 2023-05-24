#import os   #THIS CODE WAS NOT WORK
# import subprocess
# #import re
# import time

# print("start monitor vpn monitor check")

# expected_IP = "138.68.106.136" # ENTER YOUR EXPECTED PUBLIC IPv4 ADDRESS HERE

# current_IP = subprocess.check_output("dig TXT +short o-o.myaddr.l.google.com @ns1.google.com", shell=True)

# try:
#     while True:
#         if expected_IP in str(current_IP):
#             print("IPs Match - Things are normal")
#         else:
#             print("Current IP: " + str(current_IP) + "\nIP NOT AS EXPECTED!")
#             #Code to complete actions called here
#         time.sleep(5) # Change this timer to reduce/increase time between checks (seconds)
# except KeyboardInterrupt:
#     print("\nHard Exit Initiated. Goodbye!")


#--------------------------------------------------------------------------------------------------------------------
# import time

# # Set the total duration of program execution (in seconds)
# total_duration = 60  # Replace with the desired total duration

# # Set the interval time for program execution and stop (in seconds)
# execution_interval = 5  # Replace with the desired execution interval
# stop_interval = 3  # Replace with the desired stop interval

# # Calculate the number of execution and stop iterations based on the total duration
# num_executions = total_duration // (execution_interval + stop_interval)
# num_stops = num_executions - 1

# # Run the program for the specified duration
# for i in range(num_executions):
#     # Run the execution part of the program
#     print("Executing...")
#     time.sleep(execution_interval)
    
#     # Check if it's not the last iteration
#     if i < num_stops:
#         # Run the stop part of the program
#         print("Stopping...")
#         time.sleep(stop_interval)
#----------------------------------------------------

import requests   #THIS CODE WORKS
import time

def get_public_ip():
    response = requests.get('https://api.ipify.org').text
    return response

interval = 5  # Interval in seconds
while True:
    public_ip = get_public_ip()
    print(f'Public IP: {public_ip}')
    time.sleep(interval)

#----------------------------------------------------------------