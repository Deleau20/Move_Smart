from flask import Blueprint, render_template, request, flash, redirect
from routes.voyage import Voyage

voyage_bp = Blueprint('voyage', __name__, url_prefix='/voyage')

@voyage_bp.route('/')
def voyages():
    voyages = Voyage.objects()
    return render_template('voyages.html', voyages=voyages)

@voyage_bp.route('/calculate', methods=['POST'])
def calculate_price():
    origin = request.form['origin']
    destination = request.form['destination']
    try:
        voyage = Voyage.objects(origin=origin, destination=destination).first()
        if voyage:
            price = voyage.calculate_price()
            flash(f"The price for the trip from {origin} to {destination} is {price}$.", 'success')
        else:
            flash(f"No voyage found for the specified origin and destination.", 'warning')
    except Exception as e:
        flash('Error calculating price', 'danger')
    
    return redirect('/voyage')