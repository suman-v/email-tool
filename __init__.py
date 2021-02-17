from flask import Flask, render_template, request, redirect, url_for, flash
import os
from os.path import join, dirname, realpath
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 14:20:39 2020

@author: User
"""
from email_creator import email_format, create_email
# from email_validate import email_test
from datetime import date



app = Flask(__name__)

# Upload folder
UPLOAD_FOLDER = 'static/files'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER

# File extension
file_extension = ['csv']
import pandas as pd
from datetime import datetime
@app.route('/')
def home():
    return render_template('home.html')
from flask import Flask, make_response, request
import io
import csv, sys
@app.route("/", methods=['POST'])
def uploadFiles():
    if request.method == 'POST':
        # if request.form['fi1le-1']
            # get the uploaded file
            uploaded_file1 = request.files['file-1']
            uploaded_file2 = request.files['file-2']
            print ("slret",uploaded_file1)
            

            import pathlib
            print (pathlib.Path(__file__).parent.absolute())
            if uploaded_file1.filename != '' and uploaded_file2.filename != '':
                if uploaded_file1.filename.split('.')[1] == 'csv' and  uploaded_file2.filename.split('.')[1] == 'csv':
               
                    """
                    Your Logic with 2 files

                    """
                    
                    # stream = io.StringIO(uploaded_file1.stream.read(), newline=None)
                    data = pd.read_csv(uploaded_file1, encoding=sys.getfilesystemencoding())
                    data['First Name'] = data['First Name'].str.lower()
                    data['Last Name']= data['Last Name'].str.lower()
                    data['Company']= data['Company'].str.lower()
                    data['Email']= data['Email'].str.lower()
                 
                    company = data.to_dict()
                   
                    range_company = company['First Name']
                    
                    email_database = {}
                    for num in range_company:
                        f,l,com,email = company['First Name'][num], company['Last Name'][num], company['Company'][num], company['Email'][num]
                        try:
                            email_prefix,domain = email_format(f,l,email)
                            format_of_email = email_prefix+"@"+domain
                        except:
                            format_of_email = "NA"
                            
                        
                        email_database.update({com:format_of_email})
    
                       
                    # stream2 = io.StringIO(uploaded_file2.stream.read(),encoding=sys.getfilesystemencoding())
                    s = set()
                    
                    for i in email_database.values():
                        i = i.split("@")
                        s.add(i[0])
                    print (s)
                    input_data = pd.read_csv(uploaded_file2)
                    input_data['First Name'] = input_data['First Name'].str.lower()
                    input_data['Last Name']= input_data['Last Name'].str.lower()
                    input_data['Company']= input_data['Company'].str.lower()

                    
                    input_data['email'] = ''
#                    input_data['email_status'] = ''
                    for i in range (input_data.shape[0]):
                        f= input_data['First Name'][i]
                        l= input_data['Last Name'][i]
                        c= input_data['Company'][i]     
                        
                        try :
                            formatemail = email_database[c]
                            domain = formatemail.split("@")
                        except:
                            
                            formatemail = "NA"
                            domain = "NA"
                        
#                        status = email_test(formatemail,domain[1] )
                        input_data['email'][i] = create_email(f,l,c,formatemail)
#                        input_data['email_status'][i] = status


                    # datetime object containing current date and time
                    now = datetime.now()
                    s = str(now).split(".")
                    
                    
                    
                    missing_data = input_data[input_data['email'] == "NA"]
                    missing_data.to_csv("Missing_file.csv" , index = False)
                    status = f"{missing_data.shape[0]} Missing Email Found"

                    input_data = input_data[input_data['email'] != "NA"]
                    
                    
                    import datetime as dt

                    today = dt.datetime.today().strftime('%Y-%m-%d %H-%M-%S')


                    name  = f"output_file_{str(s[0])}"
                    print (name+".csv")
                    input_data.to_csv(f"Output_file_{today}.csv" , index = False)
                    
                    
                    return render_template('home.html', output=status)
                
                else:
                    context = {
                        "error" : "Upload only CSV files!"   # If you want to pass anything to FrontEnd
                    }
                    return render_template('error.html', context=context)  # Check error.html for any changes
       
    

if __name__ == "__main__":
  app.run()
