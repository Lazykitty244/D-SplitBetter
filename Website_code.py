from flask import Flask, request, redirect, url_for, flash, session, render_template_string
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure random key
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create uploads directory if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Hard-coded credentials (update as needed)
USERNAME = 'admin'
PASSWORD = 'password123'

# HTML template for the login page
login_page = '''
<!DOCTYPE html>
<html>
<head>
    <title>Login - DSplitBill</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background: linear-gradient(135deg, #72edf2, #5151e5);
            font-family: Arial, sans-serif;
        }
        .container {
            background: #fff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 0 15px rgba(0,0,0,0.2);
            text-align: center;
            width: 320px;
        }
        .logo {
            font-size: 2em;
            font-weight: bold;
            color: #5151e5;
            margin-bottom: 10px;
        }
        input[type="text"],
        input[type="password"] {
            width: 90%;
            padding: 10px;
            margin: 8px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        input[type="submit"] {
            width: 95%;
            padding: 10px;
            background-color: #5151e5;
            border: none;
            color: white;
            border-radius: 4px;
            font-size: 1em;
            cursor: pointer;
        }
        .error {
            color: red;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">DSplitBill</div>
        <h2>Welcome!</h2>
        {% with messages = get_flashed_messages() %}
          {% if messages %}
            <div class="error">
              {% for message in messages %}
                <p>{{ message }}</p>
              {% endfor %}
            </div>
          {% endif %}
        {% endwith %}
        <form method="POST">
            <input type="text" name="username" placeholder="Username" required/><br/>
            <input type="password" name="password" placeholder="Password" required/><br/>
            <input type="submit" value="Login"/>
        </form>
    </div>
</body>
</html>
'''

# HTML template for the upload page
upload_page = '''
<!DOCTYPE html>
<html>
<head>
    <title>Upload File - DSplitBill</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background: linear-gradient(135deg, #72edf2, #5151e5);
            font-family: Arial, sans-serif;
        }
        .container {
            background: #fff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 0 15px rgba(0,0,0,0.2);
            text-align: center;
            width: 320px;
        }
        .logo {
            font-size: 2em;
            font-weight: bold;
            color: #5151e5;
            margin-bottom: 10px;
        }
        input[type="file"] {
            margin: 15px 0;
        }
        input[type="submit"] {
            padding: 10px 20px;
            background-color: #5151e5;
            border: none;
            color: white;
            border-radius: 4px;
            font-size: 1em;
            cursor: pointer;
        }
        .success {
            color: green;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">DSplitBill</div>
        <h2>Hi {{ session['username'] }}!</h2>
        {% with messages = get_flashed_messages() %}
          {% if messages %}
            <div class="success">
              {% for message in messages %}
                <p>{{ message }}</p>
              {% endfor %}
            </div>
          {% endif %}
        {% endwith %}
        <form method="POST" enctype="multipart/form-data">
            <input type="file" name="file" required/><br/>
            <input type="submit" value="Upload"/>
        </form>
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == USERNAME and password == PASSWORD:
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('upload_file'))
        else:
            flash('Invalid credentials. Please try again.')
    return render_template_string(login_page)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected')
            return redirect(request.url)
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            flash('File uploaded successfully!')
            return redirect(url_for('upload_file'))
    return render_template_string(upload_page)

if __name__ == '__main__':
    app.run(debug=True)
