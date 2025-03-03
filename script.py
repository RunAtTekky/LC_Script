from urllib.request import urlopen
import json

def print_data(username: str):
    url = f"https://alfa-leetcode-api.onrender.com/{username}/solved"
    
    # store the response of URL 
    response = urlopen(url) 
    
    # storing the JSON response from url in data 
    json_data = json.loads(response.read()) 
    
    solved_problems = json_data["solvedProblem"]
    # easy_problems = json_data["easySolved"]
    # medium_problems = json_data["mediumSolved"]
    # hard_problems = json_data["hardSolved"]

    print("Hi, ", username)
    print("Total Problems Solved: ", solved_problems)

    details.append([username,solved_problems])
    # print("Easy: ", easy_problems)
    # print("Medium: ", medium_problems)
    # print("Hard: ", hard_problems)

def write_data_to_file():
    with open("LC_account_details.txt", "w") as file:
        for usrname, problems in details:
            file.write(f"{usrname} {problems}\n")  


# Open the file containing accounts
with open("leetcode_accounts.txt", "r") as file:
    content = file.read()

# Split the file into lines with usernames on each line
lines = content.splitlines()

details = []

for username in lines:
    username = username.strip()
    if not username:
        continue
    try:
        print_data(username)
    except:
        print(f"LMAO, {username} changed their username!")
    print()

write_data_to_file()