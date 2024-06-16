

from flask import Flask,render_template,request
#from flask_sqlalchemy import SQLAlchemy
import csv
import random

app = Flask(__name__,template_folder='/home/univtimetable/mysite/template')

import module_b
s3_tup_b,s5_tup_b,s7_tup_b,data3b,data5b,data7b,L2,L4,L6,L8,L10,L12,L14,L16,L18,L20,L22=module_b.printing_b()

import module_a
s3_tup_a,s5_tup_a,s7_tup_a,data3a,data5a,data7a,L1,L3,L5,L7,L9,L11,L13,L15,L17,L19,L21=module_a.printing_b()



#Flask
@app.route('/')
def home():
    return render_template('index.html')


headings=("8:15am-9:15am", "9:15am-10:15am", "10:30am-11:30am", "11:30am-12:30pm", "12:30pm-1:30pm", "1:30pm-2:30pm","2:30pm-3:30pm")
side=("Monday", "Tuesday","Wednesday","Thursday","Friday")
top=("Course Code", "Course Name",	"Type",	"Course Instructor")
#headings=headings,data=s3_tup,

@app.route('/student',methods=["POST","GET"])
def second():
    if request.method=="POST":
        for val in request.form.keys():
            if val=='sem':
                sem=request.form[val]
            if val=='sec':
                sec=request.form[val]
        #print("SEC",sec)
        if sem=="3":
            if sec=="A":
                return render_template("student.html",headings=headings,data=s3_tup_a,title=top,course= data3a, main="Semester: 3         Section: A",side=side)
            else:
                return render_template("student.html",headings=headings,data=s3_tup_b,title=top,course= data3b, main="Semester: 3         Section: B")
        if sem=="5":
            if sec=="A":
                return render_template("student.html", headings=headings,data=s5_tup_a,title=top,course= data5a, main="Semester: 5         Section: A")
            else:
                return render_template("student.html", headings=headings,data=s5_tup_b,title=top,course= data5b, main="Semester: 5         Section: B")
        if sem=="7":
            if sec=="A":
                return render_template("student.html", headings=headings,data=s7_tup_a,title=top,course= data7a, main="Semester: 7         Section: A")
            else:
                return render_template("student.html", headings=headings,data=s7_tup_b,title=top,course= data7b, main="Semester: 7         Section: B")
    return render_template("student.html")


@app.route('/faculty',methods=["POST","GET"])
def third():
    if request.method=="POST":
        faculty=request.form["faculty"]
        if faculty=="1":
            return render_template("faculty.html",headings=headings,data=L1,main="Faculty ID: L1")
        elif faculty=="2":
            return render_template("faculty.html",headings=headings,data=L2,main="Faculty ID: L2")
        elif faculty=="3":
            return render_template("faculty.html",headings=headings,data=L3,main="Faculty ID: L3")
        elif faculty=="4":
            return render_template("faculty.html",headings=headings,data=L4,main="Faculty ID: L4")
        elif faculty=="5":
            return render_template("faculty.html",headings=headings,data=L5,main="Faculty ID: L5")
        elif faculty=="6":
            return render_template("faculty.html",headings=headings,data=L6,main="Faculty ID: L6")
        elif faculty=="7":
            return render_template("faculty.html",headings=headings,data=L7,main="Faculty ID: L7")
        elif faculty=="8":
            return render_template("faculty.html",headings=headings,data=L8,main="Faculty ID: L8")
        elif faculty=="9":
            return render_template("faculty.html",headings=headings,data=L9,main="Faculty ID: L9")
        elif faculty=="10":
            return render_template("faculty.html",headings=headings,data=L10,main="Faculty ID: L10")
        elif faculty=="11":
            return render_template("faculty.html",headings=headings,data=L11,main="Faculty ID: L11")
        elif faculty=="12":
            return render_template("faculty.html",headings=headings,data=L12,main="Faculty ID: L12")
        elif faculty=="13":
            return render_template("faculty.html",headings=headings,data=L13,main="Faculty ID: L13")
        elif faculty=="14":
            return render_template("faculty.html",headings=headings,data=L14,main="Faculty ID: L14")
        elif faculty=="15":
            return render_template("faculty.html",headings=headings,data=L15,main="Faculty ID: L15")
        elif faculty=="16":
            return render_template("faculty.html",headings=headings,data=L16,main="Faculty ID: L16")
        elif faculty=="17":
            return render_template("faculty.html",headings=headings,data=L17,main="Faculty ID: L17")
        elif faculty=="18":
            return render_template("faculty.html",headings=headings,data=L18,main="Faculty ID: L18")
        elif faculty=="19":
            return render_template("faculty.html",headings=headings,data=L19,main="Faculty ID: L19")
        elif faculty=="20":
            return render_template("faculty.html",headings=headings,data=L20,main="Faculty ID: L20")
        elif faculty=="21":
            return render_template("faculty.html",headings=headings,data=L21,main="Faculty ID: L21")
        elif faculty=="22":
            return render_template("faculty.html",headings=headings,data=L22,main="Faculty ID: L22")
        else:
            return render_template('faculty.html')

    else:
        return render_template('faculty.html')


if __name__=='__main__':
    app.run(debug=True)



















