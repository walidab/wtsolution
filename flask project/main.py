

from django.shortcuts import render
from flask import Flask,request,render_template,redirect, request_started
import random
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('home.html')

@app.route('/send-money', methods=['POST','GET'])
def send():
    return render_template('send-money.html')



@app.route('/walid')
def calcul():
    walid = 12
    tina = 13
    tinwal = 25
    return render_template('walid.html',tinwal=tinwal)




















@app.route('/result', methods=['POST','GET'])
def result():
    verb1 = str(request.form.get('name'))
    adj = str(request.form.get('adj'))
    
    dec = {"mange": "ech","dor":"etess","bois":"essaw","travail":"khedem","regard":"wali"}
    nume = dec[str(verb1)]

    
    if adj == "1"  :
        nume = ("adh"+ nume+"agh")
        verb1 = ("je "+ verb1)

    elif adj == "2":
        nume = ("at"+ nume+"edh")

    elif adj == "3":
        nume = ("adhi"+ nume+"")

    elif adj == "4":
        nume = ("adh"+ nume+"en")

    elif adj == "5":
        nume = ("an"+ nume+"eth")
    else: 
        return "oulachith "

    return render_template('walid.html', adj=adj, verb1=verb1, nume=nume)


if __name__ == "__main__":
    app.run(debug=True)
