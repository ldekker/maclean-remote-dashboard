from webui import WebUI
from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
ui = WebUI(app, debug=True)

@app.route('/', methods=['GET','POST'])
def mainPage():
    result=0
    cam = ""
    if request.method=='POST':
        cam = request.form['camera']

        if cam == "front":
            return redirect(url_for('frontView'))

        if cam == "rear":
            return redirect(url_for('rearView'))

        if cam == "split":
            return redirect(url_for('splitView'))

    return render_template('mainPage.html',result=result)


@app.route('/front', methods=['GET','POST'])
def frontView():
    result=0
    cam = ""
    if request.method=='POST':
        cam = request.form['camera']

        if cam == "front":
            return redirect(url_for('frontView'))

        if cam == "rear":
            return redirect(url_for('rearView'))

        if cam == "split":
            return redirect(url_for('splitView'))

    return render_template('frontView.html',result=result)


@app.route('/rear', methods=['GET','POST'])
def rearView():
    result=0
    cam = ""
    if request.method=='POST':
        cam = request.form['camera']

        if cam == "front":
            return redirect(url_for('frontView'))

        if cam == "rear":
            return redirect(url_for('rearView'))

        if cam == "split":
            return redirect(url_for('splitView'))

    return render_template('rearView.html',result=result)

@app.route('/split',methods=['GET','POST'])
def splitView():
    result=0
    cam = ""
    if request.method=='POST':
        cam = request.form['camera']

        if cam == "front":
            return redirect(url_for('frontView'))

        if cam == "rear":
            return redirect(url_for('rearView'))

        if cam == "split":
            return redirect(url_for('splitView'))

    return render_template('splitView.html',result=result)

if __name__=='__main__':
    ui.run()
