from datetime import datetime
from extensions import db


# -------------------------
# CUSTOMER
# -------------------------
class Customer(db.Model):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)

    full_name = db.Column(db.String(120), nullable=False)

    email = db.Column(db.String(120), unique=True)

    phone = db.Column(db.String(30))

    address = db.Column(db.Text)

    city = db.Column(db.String(80))

    country = db.Column(db.String(80))

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    shipments = db.relationship(
        "Shipment",
        backref="customer",
        lazy=True
    )


# -------------------------
# DRIVER
# -------------------------
class Driver(db.Model):
    __tablename__ = "drivers"

    id = db.Column(db.Integer, primary_key=True)

    full_name = db.Column(db.String(120))

    phone = db.Column(db.String(30))

    license_number = db.Column(db.String(80))

    status = db.Column(
        db.String(50),
        default="Available"
    )


# -------------------------
# VEHICLE
# -------------------------
class Vehicle(db.Model):
    __tablename__ = "vehicles"

    id = db.Column(db.Integer, primary_key=True)

    plate_number = db.Column(
        db.String(30),
        unique=True
    )

    vehicle_type = db.Column(db.String(80))

    capacity = db.Column(db.String(50))

    status = db.Column(
        db.String(50),
        default="Available"
    )


# -------------------------
# WAREHOUSE
# -------------------------
class Warehouse(db.Model):
    __tablename__ = "warehouses"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))

    city = db.Column(db.String(80))

    country = db.Column(db.String(80))

    address = db.Column(db.Text)


# -------------------------
# SHIPMENT
# -------------------------
class Shipment(db.Model):
    __tablename__ = "shipments"

    id = db.Column(db.Integer, primary_key=True)

    tracking_number = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    sender_name = db.Column(db.String(120))

    receiver_name = db.Column(db.String(120))

    origin = db.Column(db.String(120))

    destination = db.Column(db.String(120))

    weight = db.Column(db.Float)

    shipment_type = db.Column(db.String(80))

    current_status = db.Column(
        db.String(100),
        default="Pending"
    )

    estimated_delivery = db.Column(db.Date)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    customer_id = db.Column(
        db.Integer,
        db.ForeignKey("customers.id")
    )


# -------------------------
# SHIPMENT HISTORY
# -------------------------
class ShipmentHistory(db.Model):
    __tablename__ = "shipment_history"

    id = db.Column(db.Integer, primary_key=True)

    shipment_id = db.Column(
        db.Integer,
        db.ForeignKey("shipments.id")
    )

    location = db.Column(db.String(120))

    status = db.Column(db.String(120))

    remarks = db.Column(db.Text)

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


# -------------------------
# PAYMENT
# -------------------------
class Payment(db.Model):
    __tablename__ = "payments"

    id = db.Column(db.Integer, primary_key=True)

    shipment_id = db.Column(
        db.Integer,
        db.ForeignKey("shipments.id")
    )

    amount = db.Column(db.Float)

    payment_method = db.Column(db.String(80))

    payment_status = db.Column(
        db.String(50),
        default="Pending"
    )

    payment_date = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


# -------------------------
# NOTIFICATION
# -------------------------
class Notification(db.Model):
    __tablename__ = "notifications"

    id = db.Column(db.Integer, primary_key=True)

    shipment_id = db.Column(
        db.Integer,
        db.ForeignKey("shipments.id")
    )

    message = db.Column(db.Text)

    sent_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )
current_location = db.Column(db.String(120), default="Warehouse")

estimated_delivery = db.Column(db.Date)

last_updated = db.Column(
    db.DateTime,
    default=datetime.utcnow
)
