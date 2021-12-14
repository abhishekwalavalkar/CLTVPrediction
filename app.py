#!/usr/bin/env python
# coding: utf-8

# Dependencies
#!/usr/bin/env python
# coding: utf-8

# Dependencies
from flask import Flask, request, jsonify,render_template
import pandas as pd
import numpy as np

# Your API definition
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('output.html')

@app.route('/predict',methods=['POST'])
def input_web():
    try:
        cust_id = request.form.to_dict()
        data=pd.read_csv('data_new.csv')
        data.drop(['CLTV Score'],axis=1,inplace=True)
        data['Customer id']=data['Customer id'].astype('str')
        if cust_id['cust_id'] in data['Customer id'].values:
            row=data[data['Customer id']==cust_id['cust_id']]
            print(row)
            score=row['Avg no of transactions per year']*row['Avg revenue per transaction']*row['Retention rate']
            score.reset_index(drop=True,inplace=True)
            print(score)
            output = (f"The CLTV score for this Customer ID {cust_id['cust_id']} is $ {str(round(score[0],2))}")
            print(output)
            #return jsonify({'Customer ID':cust_id['cust_id'],'CLTV': str(round(score[0],2))})
            return output
        else:
            return str('Error! Customer ID not available')
    except:
        return jsonify({'trace': traceback.format_exc()})

@app.route('/predict_api',methods=['POST'])
def predict_api():
    try:
        cust_id=request.get_json(force=True)
        print('Customer ID',cust_id['Customer ID'])
        data=pd.read_csv('data_new.csv')
        data.drop(['CLTV Score'],axis=1,inplace=True)
        #data['Customer id']=data['Customer id'].astype('str')
        if cust_id['Customer ID'] in data['Customer id'].values:
            row=data[data['Customer id']==cust_id['Customer ID']]
            print(row)
            score=row['Avg no of transactions per year']*row['Avg revenue per transaction']*row['Retention rate']
            score.reset_index(drop=True,inplace=True)
            print(score)
            output = (f"The CLTV score for this Customer ID {cust_id['Customer ID']} is $ {str(round(score[0],2))}")
            print(output)
            return jsonify({'Customer ID':cust_id['Customer ID'],'CLTV': str(round(score[0],2))})
        else:
            return jsonify({'Error':'Customer ID not available'})
    except:
        return jsonify({'trace': traceback.format_exc()})

    
if __name__ == '__main__':
    app.run(port=5000, debug=True,use_reloader=False)
    
