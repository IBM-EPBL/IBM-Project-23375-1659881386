import numpy as np
from flask import Flask,render_template,request
import pickle
app= Flask(__name__)
model=pickle.load(open(r'C:\Users\Admin\Desktop\final_project\App\wqi.pkl','rb'))
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
  y_pred = model.predict(total)
  y_pred=y_pred[[0]]
  if(y_pred >= 95 and y_pred<=100):
    pred = 'Excellent, The Predicted Value Is'+ str(y_pred)
  elif(y_pred >= 89 and y_pred<=94):
    pred = 'Very Good, The Predicted Value Is'+ str(y_pred)
  elif(y_pred >= 80 and y_pred<=88):
    pred = 'Good, The Predicted Value Is'+ str(y_pred)
  elif(y_pred >= 65 and y_pred<=79):
    pred = 'Fair, The Predicted Value Is'+ str(y_pred)
  elif(y_pred >= 45 and y_pred<=64):
    pred = 'Marginal, The Predicted Value Is'+ str(y_pred)
  else:
    pred = 'Poor, The Predicted Value Is'+ str(y_pred)
    
  return render_template('web.html', output='{}'.format(pred))

if __name__ == '__main__':
     app.run(debug = True)