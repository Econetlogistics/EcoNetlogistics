shipment = Shipment(
    tracking_number=generate_tracking_number(),
    sender_name=request.form["sender_name"],
    receiver_name=request.form["receiver_name"],
    origin=request.form["origin"],
    destination=request.form["destination"],
    weight=float(request.form["weight"]),
    shipment_type=request.form["shipment_type"],
    current_status="Pending",
    current_location=request.form["origin"]
)
