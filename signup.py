from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB Atlas
client = MongoClient('mongodb+srv://shaswata:707@pricepinion.vwosknx.mongodb.net/')
db = client['<dbname>']  # Replace '<dbname>' with your database name
users_collection = db['users_info']  # Collection to store user data

@app.route('/')
def signup_form():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():
    # Get form data
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    # Validate password
    if password != confirm_password:
        return 'Passwords do not match'

    # Check if user already exists
    if users_collection.find_one({'email': email}):
        return 'User already exists'

    # Insert new user into MongoDB
    users_collection.insert_one({'name': name, 'email': email, 'password': password})
    return 'User created successfully'

if __name__ == '__main__':
    app.run(debug=True)
