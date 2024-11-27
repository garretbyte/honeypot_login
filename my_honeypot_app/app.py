from flask import Flask, render_template, redirect, url_for, flash, session, request

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return render_template('home.html')

# Store users and their passwords
users = {
    'admin': 'password',  # Example user
    'user1': 'password123',
    'user2': 'securepass'
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Validate credentials
        if username in users and users[username] == password:
            session['logged_in'] = True
            session['username'] = username  # Track the logged-in user
            flash(f'Welcome, {username}!')
            return redirect(url_for('honeypot'))
        else:
            flash('Invalid credentials. Please try again.')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/honeypot')
def honeypot():
    if not session.get('logged_in'):
        flash('Unauthorized access detected!')
        return redirect(url_for('login'))
    return render_template('honeypot.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.')
    return redirect(url_for('login'))

if __name__ == '__main__':
        app.run(host="0.0.0.0", port=8080, debug=True)
