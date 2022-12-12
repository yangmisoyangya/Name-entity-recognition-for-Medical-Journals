from flask import Flask,url_for,render_template,request,redirect
import spacy
from spacy import displacy
nlp = spacy.load('en_ner_bc5cdr_md')
nlp1 = spacy.load('en_ner_bionlp13cg_md')
import json
import re
import pandas as pd
from PyPDF2 import PdfReader

HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""

from flaskext.markdown import Markdown

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Column

app = Flask(__name__)
Markdown(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///medical.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#initialize the database
db = SQLAlchemy(app)

#create db model
class Medicals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200),nullable=False)
    entity = db.Column(db.String(200),nullable=False)
    date_created = db.Column(db.DateTime,default=datetime.utcnow)
    #create a function to return a string when we add something  
    def __repr__(self):
        return f"Medicals('{self.name}','{self.entity}')"


# def analyze_text(text):
# 	return nlp(text)

@app.route('/')
def index():
        return render_template('index.html')
    
@app.route('/about')
def about():
		return render_template('about.html')    
    

@app.route('/extractpdf',methods=['GET','POST'])
def extractpdf():
    if request.method == 'POST':
        f = request.files['file']
        reader = PdfReader(f)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        words = re.sub("[^A-Za-z" "]+", " ", text).lower()
        docx=nlp(words)
        Dataframe=[(ent.text,ent.label_) for ent in docx.ents]
        uniue_char = []
        for c in Dataframe:
            if not c in uniue_char:
                uniue_char.append(c)
        df=pd.DataFrame(uniue_char,columns=['name','disease/chemical'])
        result1 = HTML_WRAPPER.format(df)
    
    return render_template('data.html',tables=[df.to_html()], titles=[''],result1=result1)

@app.route('/extractbio',methods=['GET','POST'])
def extractbio():
    if request.method == 'POST':
        f = request.files['file']
        reader = PdfReader(f)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        words = re.sub("[^A-Za-z" "]+", " ", text).lower()
        docx=nlp1(words)
        Dataframe=[(ent.text,ent.label_) for ent in docx.ents]
        uniue_char = []
        for c in Dataframe:
            if not c in uniue_char:
                uniue_char.append(c)
        df=pd.DataFrame(uniue_char,columns=['name','Biomedicals'])
        result2 = HTML_WRAPPER.format(df)
    
    return render_template('bio.html',tables=[df.to_html()], titles=[''],result2=result2)


@app.route('/extract',methods=["GET","POST"])
def extract():
	if request.method == 'POST':
		raw_text = request.form['rawtext']
		docx = nlp(raw_text)
		html = displacy.render(docx,style="ent")
		html = html.replace("\n\n","\n")
		result = HTML_WRAPPER.format(html)

	return render_template('result.html',rawtext=raw_text,result=result)
  
if __name__ == '__main__':    
  app.run(host='0.0.0.0',port=3000)
