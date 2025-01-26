from fastapi import FastAPI # Import FastAPI

from validator import isEmailValid, getEmailDomain # Import necessary functions from validator.py

app = FastAPI() # Create FastAPI instance

@app.get("/validate-email") # Define route for email validation
def validate_email(email:str): # Function for validation. Takes email as parameter
    email = email.strip() # Removing whitespaces from email
    if email == "": # If email is empty
        return {"Email": "Email is empty", "Valid": False}
    
    valid = isEmailValid(email) # Check if email is valid

    if not valid: # If email is not valid
        return {"Email": email, "Valid": False} # Return email and validation result

    return {
            "Email": email, 
            "Email-length":len(email),
            "Valid": valid,
            "Domain": getEmailDomain(email)
        } # Return email, validation result and additional information
    
    
    