
from flask import Flask, render_template, request, redirect, url_for
from database import create_table, insert_item, get_all_items, get_dashboard_stats, update_item_status
app = Flask(__name__)

# Initialize database
create_table()


# Home page
@app.route('/')
def home():
    items = get_all_items()
    total, lost, found, resolved = get_dashboard_stats()
    return render_template(
        'index.html',
        items=items,
        total=total,
        lost=lost,
        found=found,
        resolved=resolved
    )


# Report Lost or Found Item
@app.route('/report/<report_type>')
def report(report_type):

    if report_type not in ['Lost', 'Found']:
        return "Invalid report type", 400

    return render_template('report.html', report_type=report_type)


# Dashboard
@app.route('/dashboard')
def dashboard():

    items = get_all_items()
    total, lost, found = get_dashboard_stats()

    return render_template(
        'index.html',
        items=items,
        total=total,
        lost=lost,
        found=found
    )

# Update Item Status
@app.route('/update_status/<int:item_id>', methods=['POST'])
def update_status(item_id):

    status = request.form.get('status')

    if status not in ['Open', 'Resolved']:
        return "Invalid status", 400

    update_item_status(item_id, status)

    return redirect(url_for('home'))

# Submit Report
@app.route('/submit', methods=['POST'])
def submit_report():

    report_type = request.form.get('report_type')
    item_name = request.form.get('item_name')
    category = request.form.get('category')
    description = request.form.get('description')
    location = request.form.get('location')
    contact = request.form.get('contact')

    if report_type not in ['Lost', 'Found']:
        return "Invalid report type", 400

    if not all([item_name, category, description, location, contact]):
        return "Please fill in all fields", 400

    insert_item(
        item_name,
        description,
        category,
        location,
        report_type,
        contact
    )

    # Redirect to homepage after successful submission
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
