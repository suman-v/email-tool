# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 14:20:39 2020

@author: User
"""

# function will create the format of email for each company 
def email_format(first,last,org_email):  
    # get fisrt name,last name and company name as inputs            
    email = org_email.split("@")         #split email to get prefix and domain name
    domain = email[1]
    email_prefix = ''
    # print (email)
    #if email prefix is combination of first name and last name then true, 
    #if prefix is either first name or last name the false
    status = "." in email[0]       
    if status == True:     
        prefix = email[0].split(".")
        if prefix[0] == first and prefix[1] == last:        # first + last
            email_prefix = "f+l"
            # print (f"company:{email}  format{email_prefix}")
           
        if prefix[0] == first[:1] and prefix[1] == last:        # first[initial] + last
         
            email_prefix = "fi+l"
            # print (f"company:{email}  format{email_prefix}")
        if prefix[0] == last and prefix[1] == first[:1]:        # last + first[initial]
          
            email_prefix = "l+fi"
            # print (f"company:{email}  format{email_prefix}")

        if prefix[0] == first[:1] and prefix[1] == last[:1]:        # first[initial] + last[initial] 
         
            email_prefix = "fi+li"
            # print (f"company:{email}  format{email_prefix}")

    status_2 = "_" in email[0]
    
    if status_2 == True:
        prefix = email[0].split("_")
        if prefix[0] == first and prefix[1] == last:        # first + last
            email_prefix = "f+l2"
            # print (f"company:{email}  format{email_prefix}")
        
        
    if status == False:
       
        prefix = email[0]
        if prefix == first:
            email_prefix = "f"
            # print (f"company:{email}  format{email_prefix}")
        
        if prefix == last:
   
            email_prefix = "l"
            # print (f"company:{email}  format{email_prefix}")
            
        if prefix == first[:1]:
         
            email_prefix = "fi"
            # print (f"company:{email}  format{email_prefix}")
            
        if prefix == last[:1]:
          
            email_prefix = "li"
            # print (f"company:{email}  format{email_prefix}")
            
    status3 = "." and "_" in email[0]
    if status3 == False:
    
        if email[0] == first+last[:1]:
            # print ("f+li")
            email_prefix = "fli"
            # print (f"company:{email}  format{email_prefix}")
    
        if email[0] == first[:1]+last:
            # print ("fi+l")
            email_prefix = "fil"
            # print (f"company:{email}  format{email_prefix}")
    
    
        if email[0] == last+first[:1]:
            # print ("l+fi")
            email_prefix = "lfi"
            # print (f"company:{email}  format{email_prefix}")
            
    
        if email[0] == last[:1]+first:
            # print ("li+f")
            email_prefix = 'lif'
            # print (f"company:{email}  format{email_prefix}")

    return email_prefix, domain

#email_database = email_format("suman", "verma", "s@math.com")

def create_email(f,l,company,email_format):
#    email_format = email_database[company]
    try:
        formt = email_format.split("@")
        if formt[0] == "f+l":
            pre  = f+"."+l
        if formt[0] == "l+fi":
            pre  = l+"."+f[:1]
        if formt[0] == "l":
            pre  = l
        if formt[0] == "fi+l":
            pre  = f[:1]+"."+l
        if formt[0] == "f":
            pre  = f
        if formt[0] == "f+l2":
            pre  = f+"_"+l
        if formt[0] == "fi+li":
            pre  = f[:1]+"."+l[:1]
            
        if formt[0] == "f+l2":
            pre  = f+""+l

        if formt[0] == "fli":
            pre  = f+l[:1]
        if formt[0] == "lfi":
            pre  = l+f[:1]    
            
        if formt[0] == "fil":
            pre  = f[:1]+l
            
            
        if formt[0] == "lif":
            pre  = l[:1]+f 
            
        return pre+"@"+formt[1]
        
    except:
        
        return "NA"
    
#email_format("suman", "verma", "s@math.com")
#
#
#
#company = database.to_dict()
#company.keys()
#
#range_company = company['first name']
#
#email_database = {}
#for num in range_company:
#    f,l,com,email = company['first name'][num], company['last name'][num], company['company'][num], company['email'][num]
#    email_prefix,domain = email_format(f,l,email)
#    format_of_email = email_prefix+"@"+domain
#    email_database.update({company['company'][num]:format_of_email})
#    
    
    
