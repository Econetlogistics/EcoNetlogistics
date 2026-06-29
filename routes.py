from flask import Blueprint, render_template, request, redirect, url_for, flash

from extensions import db

from models import Shipment

from utils import generate_tracking_number

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("index.html")


@main.route("/dashboard")
def dashboard():

    total = Shipment.query.count()

    pending = Shipment.query.filter_by(
        current_status="Pending"
    ).count()

    delivered = Shipment.query.filter_by(
        current_status="Delivered"
    ).count()

    transit = Shipment.query.filter_by(
        current_status="In Transit"
    ).count()

    return render_template(
        "dashboard.html",
        total=total,
        pending=pending,
        delivered=delivered,
        transit=transit
    )


@main.route("/shipments")
def shipments():

    shipments = Shipment.query.order_by(
        Shipment.created_at.desc()
    ).all()

    return render_template(
        "shipments.html",
        shipments=shipments
    )


@main.route("/shipment/create", methods=["GET", "POST"])
def create_shipment():

    if request.method == "POST":

        shipment = Shipment(

            tracking_number=generate_tracking_number(),

            sender_name=request.form["sender_name"],

            receiver_name=request.form["receiver_name"],

            origin=request.form["origin"],

            destination=request.form["destination"],

            weight=float(request.form["weight"]),

            shipment_type=request.form["shipment_type"],

            current_status="Pending"

        )

        db.session.add(shipment)

        db.session.commit()

        flash("Shipment created successfully!", "success")

        return redirect(url_for("main.shipments"))

    return render_template("create_shipment.html")
