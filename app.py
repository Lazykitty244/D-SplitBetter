from flask import Flask, render_template, request, redirect, url_for, session
import os
import json
import requests
from werkzeug.utils import secure_filename
from collections import defaultdict

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.secret_key = 'supersecretkey'  # Required for session
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# OCR API info
OCR_API_URL = "https://ocr.asprise.com/api/v1/receipt"
API_KEY = "TEST"  # Use your real API key if you have one

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        usernames = request.form.get('usernames')
        user_list = [u.strip() for u in usernames.split(',') if u.strip()]
        session['users'] = user_list

        file = request.files['receipt']
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Call OCR API
            with open(filepath, 'rb') as f:
                res = requests.post(OCR_API_URL,
                                    data={
                                        'api_key': API_KEY,
                                        'recognizer': 'auto',
                                        'ref_no': 'flask_upload_001'
                                    },
                                    files={
                                        'file': f
                                    })

            response_json = res.json()
            items = response_json['receipts'][0].get('items', [])

            # Clean item list
            cleaned_items = []
            for item in items:
                cleaned_items.append({
                    'description': item.get('description', 'Unknown'),
                    'amount': item.get('amount', '0.00')
                })

            session['items'] = cleaned_items
            return render_template('items.html', items=cleaned_items, users=user_list)

    return render_template('index.html')

@app.route('/split', methods=['POST'])
def split():
    form_data = request.form
    users = session.get('users', [])
    items = session.get('items', [])
    shares = defaultdict(float)

    for item in items:
        description = item['description']
        amount = float(item['amount'])
        people = []

        for user in users:
            checkbox_name = f"{description}_{user}"
            if checkbox_name in form_data:
                people.append(user)

        if people:
            split_amount = amount / len(people)
            for person in people:
                shares[person] += split_amount

    return render_template('split_result.html', shares=shares)

if __name__ == '__main__':
    app.run(debug=True)