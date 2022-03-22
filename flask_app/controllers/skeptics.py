from flask import Flask, render_template, request, redirect, session
from flask_app import app
from flask_app.models.skeptic import Skeptic

@app.route("/skeptic/create", methods=["POST"])
def skeptic_process():
    data = request.form
    print(data)
    Skeptic.insert(data)
    return redirect(f"/sighting/{data['sighting_id']}")

@app.route("/skeptic/delete/<id>/<sighting>")
def delete_skeptic(id,sighting):
    data={"user_id": id}
    Skeptic.delete(data)
    return redirect(f"/sighting/{sighting}")
