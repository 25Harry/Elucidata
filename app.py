from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import pandas as pd
import os
import xlrd


app = Flask(__name__)

UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST': 
        file = request.files['file[]']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            data = pd.read_excel(file)
        
        data.to_excel("data.xlsx")
        return render_template('upload.html', data=data.to_html())

@app.route('/filter', methods=['GET', 'POST'])
def filter():
        file = 'data.xlsx'
        data = pd.read_excel(file)
        s1 = " PC"
        filtered_df1 = data.loc[(data['Accepted Compound ID'].str.endswith(s1, na = False))]
        filtered_df1=filtered_df1.drop(['Unnamed: 0'],axis=1)
        filtered_df1.to_excel("PC.xlsx")

        s2 = " LPC"
        filtered_df2 = data.loc[(data['Accepted Compound ID'].str.endswith(s2, na = False))]
        filtered_df2=filtered_df2.drop(['Unnamed: 0'],axis=1)
        filtered_df2.to_excel("LPC.xlsx")

        s3 = " plasmalogen"
        filtered_df3 = data.loc[(data['Accepted Compound ID'].str.endswith(s3, na = False))]
        filtered_df3=filtered_df3.drop(['Unnamed: 0'],axis=1)
        filtered_df3.to_excel("plasmalogen.xlsx")
        return render_template('filter.html', data1=filtered_df1.to_html(), data2=filtered_df2.to_html(), data3=filtered_df3.to_html())

@app.route('/roundoff', methods=['GET', 'POST'])
def roundoff():
        file = 'data.xlsx'
        df = pd.read_excel(file)
        df['Retention Time Roundoff (in mins)'] = round(df['Retention time (min)'])
        v=df[list(df.columns)[-1]]
        df=df.drop(['Retention Time Roundoff (in mins)'],axis=1) 
        df=df.drop(['Unnamed: 0'],axis=1)
        df.insert(2,'Retention Time Roundoff (in mins)',v)        
        df.to_excel("roundoff.xlsx")       
        return render_template('roundoff.html', data=df.to_html())


@app.route('/mean', methods=['GET', 'POST'])
def mean():
        file = 'data.xlsx'
        df = pd.read_excel(file)
        df['Retention Time Roundoff (in mins)'] = round(df['Retention time (min)'])
        df1 = df.drop(['m/z', 'Retention time (min)', 'Accepted Compound ID'], axis = 1)
        df2 = df1.groupby('Retention Time Roundoff (in mins)', as_index=False).mean()
        df2 = df2.drop(['Unnamed: 0'],axis=1)
        df2.to_excel("mean.xlsx")
        return render_template('mean.html', data=df2.to_html())          

if __name__ == '__main__':
    app.run(debug=True)