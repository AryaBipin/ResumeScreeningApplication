# Import required libraries
from turtle import color
from flask import Flask, redirect,request,render_template,flash,url_for,send_from_directory
import os
from PIL import Image,ImageDraw
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import cgi, os
import cgitb; cgitb.enable()
import PyPDF2
import re
form = cgi.FieldStorage()
import re
from collections import Counter
import string
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image as img  
import pytesseract as PT  
import sys 
import pdf2image
from pdf2image import convert_from_path as CFP  
import pytesseract
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud
import datetime as date
import sqlite3
#from pymysql import Error
#import csv 

#import pyodbc


#1. Install tesseract using windows installer available at: https://github.com/UB-Mannheim/tesseract/wiki

#2. Note the tesseract path from the installation.Default installation path at the time the time of this edit was: C:\Users\USER\AppData\Local\Tesseract-OCR. It may change so please check the installation path.

#3. pip install pytesseract          

#4. Set the tesseract path in the script before calling image_to_string:

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')
'''@app.route('/uploaderdata', methods = ['GET', 'POST'])
def save_file():
    if request.method == 'POST':
        
        my_list = request.values['include_area']
        conn = pyodbc.connect(Driver="{SQL Server}",Server=".",Database="ResumeScreening",Trusted_Connection="Yes") 
        cursor = conn.cursor()
        for item in my_list:
            query = """INSERT INTO table_name (jobkeywords) Values (%s) """
            values=(item)
            cursor.execute (query, values)
            cursor.commit()
'''
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if request.values['include_area']:
            text_content=[]
            text_content1=[]
            text_content_tmp=[]
            text_content_1=[]
            text_tokens=[]
            text_content_1t=[]
            text_content2=[]
            text_contentt=[]
            tmp=0
            length=0
            #Converting the pdf or doc or docx files to txt
            fi = request.files['file']
            #obtain values of Keywords to Search
            text_content_tmp = request.values['include_area']
           
            print(text_content_tmp)
            #Split the words seperated by commas
            text_content1=text_content_tmp.split(',')
            
            

             #create a copy of Keywords List  
            text_content2=text_content_tmp.split(',')
            
            listt=[]
            listtt=[]

             #Keep keywords in the form skill1/skill2 from keywords list2
            letters = set('/')
            text_content2 = [item for item in text_content2 if letters & set(item)]
            for i in text_content2:
                j=i.replace('\r\n','')
                text_content_1.append(j)
            
            for i in text_content1:
                j=i.replace('\r\n','')
                text_content.append(j)       

            fil = os.path.basename(fi.filename) 
            fi.save(os.path.join("static/uploads",fil)) 

            #Using aspose        
            #doc = aw.Document("static/uploads//"+fil)
            #doc.save('static/uplods/sample.txt')

            #open text file in read mode
            #text_file = open("static/uplods/sample.txt",encoding="utf8")
 
            #read whole file to a string
            #text = text_file.read()
            #text = text.replace('-\n', '') 
 
            #close file
            #text_file.close()

            #text = text.lower()

            # Tokenize Using Regular Expression

            #text_tokens=regexp_tokenize(text, "[\w']+")

            #Removal of stop words
            PDF_file_1 ="static/uploads//"+fil

            #Download Poppler from "https://blog.alivate.com.au/poppler-windows" Then extract it.In the code section just add poppler bin_path  
            pages_1 =pdf2image.convert_from_path(PDF_file_1,poppler_path="C:/Users/Adfolks User/Downloads/poppler-0.68.0_x86/poppler-0.68.0/bin/") 

            # Now, we will create a counter for storing images of each page of PDF to image  
            image_counter1 = 1  

            # Iterating through all the pages of the pdf file stored above  

            for page in pages_1:  
                
                # PDF page n: page_n.jpg 
                filename1 = "Page_no_" + str(image_counter1) + " .jpg"  
                 # Now, we will save the image of the page in system  
                page.save(filename1, 'JPEG')  
                # Then, we will increase the counter for updating filenames  
                image_counter1 = image_counter1 + 1  
                # Variable for getting the count of the total number of pages  
            filelimit1 = image_counter1 - 1 
                # then, we will create a text file for writing the output  
            out_file1 = "output_text.txt" 
            # Now, we will open the output file in append mode so that all contents of the # images will be added in the same output file.  
            f_1 = open(out_file1,"a+")
            f_1.truncate(0)
            f_1.seek(0)  
    
 
         # Iterating from 1 to total number of pages 
            for K in range(1, filelimit1 + 1):
                filename1 = "Page_no_" + str(K) + " .jpg"  
            
    # Here, we will write a code for recognizing the text as a string variable in an image file by using the pytesserct module  
                text = str(((PT.image_to_string (img.open (filename1)))))  
                    
    # : The recognized text will be stored in variable text  
    # : Any string variable processing may be applied to text content  
    # : Here, basic formatting will be done:-  
      
                text = text.replace('-\n', '')      
    
    # At last, we will write the processed text into the file.  
                f_1.write(text) 
# Closing the file after writing all the text content.
            f_1.close()
          
            filtered_sentence_1 = []
            filtered_sentence=[]
  
            #for w in text_tokens:
             #   if w not in ENGLISH_STOP_WORDS:
              #      filtered_sentence_1.append(w)
            
            #englishStemmer2=SnowballStemmer("english")
           # for w in text_tokens:
            #    filtered_sentence.append(englishStemmer2.stem(w))
                    
            #Stemming        
            #ps = PorterStemmer()
            #for w in filtered_sentence_1: 
            #    ww=ps.stem(w)     
             #   filtered_sentence.append(ww)

            #lemmatizer = WordNetLemmatizer()
            #nltk.download('wordnet')
            #for w in text_tokens:
            #   filtered_sentence=lemmatizer.lemmatize(w)
             # Initializie score counters 
            include = 0
        
            # Create an empty list where the scores will be stored
            scores = []

            file=open(out_file1, 'r+')

            #Read a text file into string and strip newlines
            #text = file.read().replace('\n', '')
            text=file.read()

            #Convert the string into lowercase
            text = text.lower()
            
            #text=re.sub('httpS+s*', ' ', text)  # remove URLs
            #text = re.sub('RT|cc', ' ', text)  # remove RT and cc
            #text = re.sub('@S+', '  ', text)  # remove mentions
            #text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[]^_`{|}~"""), ' ', text)  # remove punctuations
            #Removing Digits from a String
            #text = re.sub(r'\d+','',text)

            #remove punctuation marks from a string 
            #text = text.translate(str.maketrans('','',string.punctuation))    
          
        
            #Split the keyword of type skill1/skill2 in text file and append the keywords to new list 'scores' if found
            for tmp in text_content_1:
                lis=[]
                lis=tmp.split('/')
                for i in lis:
                    if text.find(i)!=-1:
                        if tmp in text_content:
                            text_content.remove(tmp)
                        text_content.append(i)

             #convert all the elements of keyword list to lower case
            text_keywords=[]
            for i in text_content:
                i=i.lower()
                text_keywords.append(i) 
                     
            #Search the keywords in text file and append the keywords to new list 'scores' if found
            for word in text_keywords:
                if text.find(word)!= -1:                 
                    include +=1
                    scores.append(word)
            # length of the keywords list
            requiredWordss=[]
            requiredWords=[]
            sampletext=""
            length=len(text_keywords) 
            k=0          
        
            requiredWordss=text.split()   
            #for i in requiredWordss:
            #for i in requiredWordss:
            for i in text_keywords:
                if text.find(i) != -1:
                    cou=text.count(i)
                    while cou!=0:
                        requiredWords.append(i)
                        cou=cou-1                    
            wordfreqdist = nltk.FreqDist(requiredWords)
           
            mostcommon = wordfreqdist.most_common(50)
            word_freq = pd.DataFrame(wordfreqdist.most_common(15),columns=['words', 'count'])
            word_freq.head(15)
            import matplotlib.pyplot as plt
            fig, ax = plt.subplots(figsize=(12, 8))

            # Plot horizontal bar graph
            c = ['#198086','#167378','#14666b','#198086','#2f8c92','#46999e','#5ea6aa','#75b2b6','#8cbfc2','#a3ccce','#bad8da','#0c4043','#0a3335','#072628','#05191a','#020c0d','#000000']
            word_freq.sort_values(by='count').plot.bar(x='words',y='count',ax=ax,color=c)
            ax.set_title("Common Words Found")
            plt.savefig("static/uploads/graph.png")
            #print(include)
           # plt.show()
            
            #wc = WordCloud().generate(text)
            '''plt.figure(figsize=(10,10))
            plt.imshow(wc, interpolation='bilinear')
            plt.axis("off")
            plt.show()'''
            list=[]
          

            
         #compare the count of Keywords found in pdf  vs count of keywords to search 
    if include/length >= 0.75:
        return render_template('next.html',list=[text_keywords,scores,mostcommon,include,length,mostcommon,fi,text])
        
    else:
        return render_template('next.html',list=[text_keywords,scores,mostcommon,include,length,mostcommon,fi,text])
            
if __name__ == "__main__":
    app.run(debug=True,port=5000)



    #Saving to sqllite is not working
    #changed form action to view the chart in next.html
   
