from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.incidents import Incident
from flask_login import login_required, current_user

incident_bp = Blueprint('incident', __name__, url_prefix='/incident')

@incident_bp.route('/')
@login_required
def incidents():
    incidents = Incident.objects(user_id=current_user.id)
    return render_template('incidents.html', incidents=incidents)

@incident_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create_incident():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        location = request.form['location']
        user_id = current_user.id

        incident = Incident(title=title, description=description, location=location, user_id=user_id)
        try:
            incident.save()
            flash('Incident created successfully!', 'success')
            return redirect(url_for('incident.incidents'))
        except Exception as e:
            flash('Error creating incident', 'danger')
            return redirect(url_for('incident.incidents'))

    return render_template('create_incident.html')