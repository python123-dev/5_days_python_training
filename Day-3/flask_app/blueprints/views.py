#Flask Templates, Forms, Views and Redirects
from flask import Blueprint, render_template, request, redirect, url_for
import models

views_bp = Blueprint('views', __name__)


#view - renders a template listing all customers
@views_bp.route('/')
def index():
    customers = models.get_all_customers()
    return render_template('index.html', customers=customers)


#view + form - GET shows the form, POST reads it and redirects back to index
@views_bp.route('/add', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        models.add_customer(name, address)
        return redirect(url_for('views.index'))   #redirect - avoids re-submitting the form on refresh
    return render_template('add_customer.html')


#view - HTML forms only support GET/POST, so delete is a POST route (not the DELETE /api/customers/<id> API route)
@views_bp.route('/delete/<int:customer_id>', methods=['POST'])
def delete_customer(customer_id):
    models.delete_customer(customer_id)
    return redirect(url_for('views.index'))
