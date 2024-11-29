from flask import Flask, request, redirect, url_for, session, render_template
from supabase import create_client, Client

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Initialize Supabase client
SUPABASE_URL = ''
SUPABASE_KEY = ''
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        # Register user with Supabase
        response = supabase.auth.sign_up({
            'email': email,
            'password': password
        })
        if response.user:
            session['user'] = response.user
            return redirect(url_for('dashboard'))
        else:
            return 'Registration failed', 400
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Authenticate user with Supabase
        response = supabase.auth.sign_in({
            'email': email,
            'password': password
        })
        if response.user:
            session['user'] = response.user
            return redirect(url_for('dashboard'))
        else:
            return 'Login failed', 400
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return f"Welcome, {session['user']['email']}!"
    return redirect(url_for('register'))

if __name__ == '__main__':
    app.run(debug=True)
