import csv
from Website import db
from Website.models import User, HybridCar

CAR_CSV_FILE = "data/hybrid_cars.csv"

def add_hybrid_car(user_email, make, model, year, battery_capacity, fuel_efficiency):
    user = User.query.filter_by(email=user_email).first()
    if not user:
        return "User not found."

    car = HybridCar(make=make, model=model, year=year, battery_capacity_kWh=battery_capacity, fuel_efficiency_mpg=fuel_efficiency, user_id=user.id)
    db.session.add(car)
    db.session.commit()

    with open(CAR_CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([car.id, user_email, make, model, year, battery_capacity, fuel_efficiency])

    return f"Added {make} {model} ({year}) to database and CSV."


