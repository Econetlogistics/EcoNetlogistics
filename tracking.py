from flask import Blueprint, render_template, request

from models import Shipment

tracking = Blueprint("tracking", __name__)


@tracking.route("/", methods=["GET", "POST"])
def tracker():

    shipment = None

    error = None

    if request.method == "POST":

        tracking_number = request.form.get("tracking_number")

        shipment = Shipment.query.filter_by(
            tracking_number=tracking_number
        ).first()

        if shipment is None:
            error = "Tracking number not found."

    return render_template(
        "tracking.html",
        shipment=shipment,
        error=error
    )
