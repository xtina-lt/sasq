from flask import Flask, render_template, request, redirect, session
from flask_app import app
from flask_app.models.sighting import Sighting
from flask_app.models.user import User

'''READ ALL'''
@app.route("/dashboard")
def sightings_dashboard():
    if session:
        return render_template("sightings_dash.html", output=Sighting.select_all())
    else:
        return redirect("/")

'''READ ONE'''
@app.route("/sighting/<id>")
def read_sighting(id):
    data={"id": id}
    result = Sighting.select_one(data)
    check = False
    if result.holds:
        for i in result.holds:
            if i.id == session['logged_in']['id']:
                check = True
    return render_template("sighting.html", output = result, check=check)

'''CREATE'''
@app.route("/sighting/create")
def sighting_create():
    if session:
        return render_template("sighting_create.html")
    else:
        return redirect("/")

@app.route("/sighting/create/process", methods=["POST"])
def sighting_create_process():
    data = request.form
    Sighting.insert(data)
    return redirect("/dashboard")

'''EDIT'''
@app.route("/sighting/<id>/update")
def sighting_update(id):
    if session:
        data={"id": id}
        check = Sighting.select_one(data)
        if check:
            return render_template("sighting_edit.html", output = check)
        else:
            return redirect("/catchall")
    else:
        return redirect("/")

@app.route("/sighting/update/process", methods=["POST"])
def sighting_update_process():
    data={k:v for k,v in request.form.items()}
    data['detail']=data['detail'].strip()
    Sighting.update(data)
    return redirect(f"/sighting/{data['id']}")

'''DELETE'''
@app.route("/sighting/<id>/delete")
def delete_sighting(id):
    data={"id":id}
    Sighting.delete(data)
    return redirect("/dashboard")
