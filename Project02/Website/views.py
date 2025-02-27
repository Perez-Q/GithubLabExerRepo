from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from . import db
from datetime import datetime
from .models import HybridCar, FuelUsage 
from .hybrid_cars import add_hybrid_car

views = Blueprint("views", __name__)

@views.route("/")
@login_required
def home():
    cars = HybridCar.query.filter_by(user_id=current_user.id).all()
    return render_template("home.html", user=current_user, cars=cars)

@views.route("/register_car", methods=["POST"])
@login_required
def register_car():
    make = request.form.get("make")
    model = request.form.get("model")
    year = request.form.get("year")
    battery_capacity = request.form.get("battery_capacity_kWh")
    fuel_efficiency = request.form.get("fuel_efficiency_mpg")

    if not make or not model or not year:
        flash("Make, model, and year are required.", "error")
        return redirect(url_for("views.home"))

    try:
        year = int(year)
        battery_capacity = float(battery_capacity) if battery_capacity else 0.0
        fuel_efficiency = float(fuel_efficiency) if fuel_efficiency else 0.0
    except ValueError:
        flash("Invalid input for year, battery capacity, or fuel efficiency.", "error")
        return redirect(url_for("views.home"))

    result = add_hybrid_car(
        user_email=current_user.email,
        make=make,
        model=model,
        year=year,
        battery_capacity=battery_capacity,
        fuel_efficiency=fuel_efficiency
    )

    flash(result, "success")
    return redirect(url_for("views.home"))

@views.route("/log_fuel/<int:car_id>", methods=["POST"])
@login_required
def log_fuel(car_id):
    car = HybridCar.query.get(car_id)
    
    if not car or car.user_id != current_user.id:
        flash("Car not found or unauthorized access.", "error")
        return redirect(url_for("views.home"))

    fuel_used = request.form.get("fuel_used")
    distance_traveled = request.form.get("distance_traveled")

    try:
        fuel_used = float(fuel_used)
        distance_traveled = float(distance_traveled)
    except ValueError:
        flash("Invalid input for fuel used or distance traveled.", "error")
        return redirect(url_for("views.home"))

    fuel_log = FuelUsage(
        car_id=car.id, 
        fuel_used=fuel_used, 
        distance_traveled=distance_traveled,
        date=datetime.utcnow()  # Ensure a valid date is provided
    )

    db.session.add(fuel_log)
    db.session.commit()

    flash("Fuel log recorded successfully!", "success")
    return redirect(url_for("views.home"))

@views.route("/delete_car/<int:car_id>", methods=["POST"])
@login_required
def delete_car(car_id):
    car = HybridCar.query.get(car_id)

    if not car or car.user_id != current_user.id:
        flash("Car not found or unauthorized access.", "error")
        return redirect(url_for("views.home"))

    # Delete all associated fuel logs
    FuelUsage.query.filter_by(car_id=car.id).delete()

    # Delete the car itself
    db.session.delete(car)
    db.session.commit()

    flash("Car and all its fuel logs have been deleted.", "success")
    return redirect(url_for("views.home"))
