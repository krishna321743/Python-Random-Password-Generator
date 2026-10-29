#random password generator

import random as rd
import string as st
password_len=12
charvalue=st.ascii_letters+st.digits+st.punctuation
password=""
for i in range(password_len):
    
    password+=rd.choice(charvalue)
print("you random password is:",password)
