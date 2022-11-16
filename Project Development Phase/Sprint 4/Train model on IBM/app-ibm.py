import numpy as np
from flask import Flask,render_template,request
import pickle

import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "628i3j3-GpGkQuV9e6LMj86WTz4sURkK3mgnsN1J4YZN"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}


app= Flask(__name__)

@app.route('/')
def home() :
  return render_template("web.html")
@app.route('/login',methods = ['POST'])
def login() :
  do = request.form["do"]
  ph = request.form["ph"]
  co = request.form["co"]
  bod = request.form["bod"]
  tc = request.form["tc"]
  na = request.form["na"]
  total = [[float(do),float(ph),float(co),float(bod),float(na),float(tc)]]
  
  payload_scoring = {"input_data": [{"fields": [['f0','f1','f2','f3','f4','f5']], "values": total}]}
  response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/2ad7e145-2d11-434d-9fc2-8e0a355734ed/predictions?version=2022-11-15', json=payload_scoring,
  headers={'Authorization': 'Bearer ' + mltoken})
  print("Scoring response")
  print(response_scoring.json())
  pred=response_scoring.json()
  res=pred['predictions'][0]['values'][0][0]
  print(res)
  return render_template('web.html', output='{}'.format(res))

if __name__ == '__main__':
     app.run(debug = True,port=5010)