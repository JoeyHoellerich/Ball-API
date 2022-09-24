from urllib import request
from flask import (Blueprint, request)
from . import models

bp = Blueprint("reptiles", __name__, url_prefix="/reptiles")

@bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        reptile_data = models.Reptiles.query.all()
        reptile_dict = {}
        for reptile in reptile_data:
            reptile_dict[reptile.id] = {
                "common_name": reptile.common_name,
                "scientific_name": reptile.scientific_name,
                "conservation_status": reptile.conservation_status,
                "native_habitat": reptile.native_habitat,
                "fun_fact": reptile.fun_fact

            }
        return reptile_dict
    elif request.method == "POST":
        new_reptile = models.Reptiles(
            common_name=request.form['common_name'],
            scientific_name= request.form['scientific_name'],
            conservation_status = request.form['conservation_status'],
            native_habitat = request.form['native_habitat'],
            fun_fact = request.form['fun_fact']
        )

        models.db.session.add(new_reptile)
        models.db.session.commit()
        return "new reptile added"