from flask import Blueprint, redirect, url_for, render_template, request, abort
from .logicCard import correctCard, getInformation
import threading

views = Blueprint('views', __name__)

mutex = threading.Lock()

res = {}

@views.route('/card/<nm>')
def card(nm):
    if (correctCard(nm) == True):
        info = getInformation(nm)
        if (info[0] == False):
            abort(500, 'No such card in database')   

        value = info[1][0][1:]
        key = "bin,brand,type,category,issuer,alpha_2,alpha_3,country,latitude,longitude,bank_phone,bank_url".split(",")
        global res
        mutex.acquire()
        try:
            res = dict(zip(key, value))
        finally:  
            mutex.release()  

        return redirect(url_for("views.info"))
    else:
        abort(500, 'Incorrect number')

@views.route('/info', methods = ['POST', 'GET'])
def info():
    if (request.method == 'POST'):
        return redirect(url_for("views.home"))

    else:
        return render_template("info.html",bin=res)

@views.route('/', methods = ['POST', 'GET'])
def home():
    if request.method == "POST":
        nm = request.form["nm"]
        if (correctCard(nm) == True):
            info = getInformation(nm)
            if (info[0] == False):
                abort(500, 'No such card in database') 
                            
            value = info[1][0][1:]
            key = "bin,brand,type,category,issuer,alpha_2,alpha_3,country,latitude,longitude,bank_phone,bank_url".split(",")
            global res
            mutex.acquire()
            try:
                res = dict(zip(key, value))  
            finally:
                mutex.release()  
            return redirect(url_for("views.info"))
        else:
            abort(500, 'Incorrect number')
        
    else:
        return render_template("page.html")