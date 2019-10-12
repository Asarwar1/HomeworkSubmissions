# Import Flask
from flask import Flask

# Create an app
app=Flask(__name__)

# User Index
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "Welcome to my 'Home' page!"

# Define the route
@app.route("/about")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"

if __name__ == '__main__':
    app.rum(debug=True)

