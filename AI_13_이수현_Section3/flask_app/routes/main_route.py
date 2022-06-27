
from flask import Blueprint, render_template, request
import numpy as np
import pickle
import pymysql


model = pickle.load(open('/Users/shlee/Desktop/section3.project/flask_app/model.pkl', 'rb'))

bp = Blueprint('index',__name__)

@bp.route('/')
def index() :
    return render_template('index.html')

@bp.route('/checkcompany')
def checkcompany() :
    return render_template('checkcompany.html')

@bp.route('/reviews')
def reviews() :
    return render_template('reviews.html')

@bp.route('/predict',methods=["GET","POST"])
def predict():
    if request.method == "POST":
        data1 = float(request.form["salary"])
        data2 = float(request.form["wlb"])
        data3 = float(request.form["culture"])
        data4 = float(request.form["promotion"])
        data5 = float(request.form["management"])
        arr = [[data1, data2, data3, data4,data5]]
        pred = model.predict(arr)
        pred = round(pred[0][0],1)
        return render_template('after.html', data=pred)
    else:
        return render_template("checkcompany.html")

@bp.route('/thankyou',methods=["GET","POST"])
def conn_db():
    if request.method =="POST":
        conn = pymysql.connect(host='localhost', user='facial09', password='1420',
                    db='section3', charset='utf8') # 한글처리 (charset = 'utf8')
        
        cur = conn.cursor()
        cur.execute(f'''INSERT INTO company VALUES("{request.form["names"]}",{request.form["salary"]},{request.form["wlb"]},{request.form["culture"]},
                    {request.form["promotion"]},{request.form["management"]},{request.form["recommendrate"]},
                    {request.form["ceorating"]},{request.form["growth"]},{request.form["total"]})''')
        conn.commit()
        conn.close()
        return render_template('thankyou.html')
    else:
        return render_template('reviews.html')