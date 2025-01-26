import re # Importing regex module

def isEmailValid(email:str) -> bool:  # Function to validate email
    if len(email) < 7 or re.match("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email) == None: # If email is less than 7 symbols either it doesn't match the regex
        return False # Email is invalid
    return True # Email is valid

def getEmailDomain(email): # Function to get domain from email
    return email.split("@")[1] # Split email by "@" and return the second part
