
# **Honey Pot App**

This is a simple Flask application designed as a learning project to explore Python development, web security concepts, and iterative improvement. The application includes a login system, a honeypot area, and plans for future database integration.

## **Features**
- **Home Page**: A welcome page introducing the Honey Pot App.
- **Login System**: Users can log in with pre-defined credentials.
- **Honeypot Page**: A restricted area designed to simulate a honeypot and log unauthorized access attempts.
- **Logout Functionality**: Users can securely log out of their session.

## **Setup Instructions**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/garretbyte/honeypot_login.git
   cd honey-pot-app
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.7+ installed, then install required packages:
   ```bash
   pip install flask flask-sqlalchemy flask-bcrypt
   ```

3. **Run the Application**:
   Start the Flask server on port **8080**:
   ```bash
   python app.py
   ```
   By default, Flask runs on `http://127.0.0.1:8080`.

4. **Access the Application**:
   Open a web browser and go to:
   ```
   http://127.0.0.1:8080
   ```

## **Application Structure**
```
/honey-pot-app
│
├── app.py           # Main Flask application
├── templates/       # HTML templates for the app
│   ├── home.html    # Home page
│   ├── honeypot.html# Honeypot (restricted) page
│   └── login.html   # Login page
├── static/          # Static files (CSS, images, etc.)
├── README.md        # This file
└── requirements.txt # Python dependencies
```

## **Learning Goals**
- **SQLAlchemy Integration**: Future iterations will replace the in-memory user dictionary with an SQLite database for persistent user management.
- **Password Hashing**: Passwords will be securely stored using bcrypt hashing.
- **Honeypot Logging**: Unauthorized access attempts will be logged in a database for analysis.
- **User Roles**: Plan to introduce user roles (e.g., admin, user) for enhanced access control.

## **Contributing**
This project is a personal learning initiative. Feedback and contributions are welcome! Feel free to fork the repository and submit pull requests.

## **License**
This project is licensed under the MIT License. See the LICENSE file for details.
