from datetime import datetime
import getpass
import os
import uuid
import json
import unittest
import pathlib as pl


class TestCase(unittest.TestCase):
    """
    Unit test case for the final output
    to check if JSON is created
    """
    def test_json_file(self):
        path = pl.Path('users.json')
        self.assertTrue(path.is_file())

# print current time in Hour:Minutes:Seconds format
print("Time is: ", datetime.now().time().strftime("%H:%M:%S"))

# Getting the current system users name
username = getpass.getuser()
print("Username: ",username)

print("[+] --------------- [-]")

PWD = os.getcwd()
all_users = []

# Display the usernames in each file under users directory 
def display_usernames(users_dir):
    file_names = os.listdir(users_dir)
    for file_name in file_names:
        with open ("users/"+file_name) as f:
            for user in f.readlines():
                user_name = user.strip()
                print(user_name)
                all_users.append(user_name)
    
    # print(file_names)

def gen_random_uuid(user_name):
    """
    generate and return a random UUID of format 
    XYxxxx-xxxx-xxxx-xxxx
    """
    import random
    first_name, last_name = user_name.split()
    uuid = first_name[0:1].upper()+last_name[0].upper()
    for _ in range(4):

        random_hex = str(hex(random.randint(10000,99999)))
        hex_num = random_hex.strip('0x')
        # print(hex_num)
        uuid += hex_num
        uuid += "-"

    uuid = uuid.strip("-")
    return uuid
    # print(uuid)

def gen_email(user_name):
    # generate a dummy email for a username passed
    first_name, last_name = user_name.split()
    return first_name.lower() +last_name.lower() + "@dummy.com"


# Code execution from here

users_dir = input("Enter path to Users: \t")
print("\n[+] Printing User Names\n")
display_usernames(users_dir)

print("[+] Processing user names and Writing to JSON file")
users_info = []
for user in all_users:
    data = {gen_random_uuid(user):{"name":user,"email":gen_email(user)}}
    users_info.append(data)
# print(users_info[0])

with open('users.json','w') as writer:
    writer.write(json.dumps(users_info))

print("\n[+] Done writing \n")

# Runnning Test Cases
print("[+] Test Case to Check if JSON created")
unittest.main()


