from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


# Mock data for clothes
products = [
    {"id": 1, "name": "T-shirt", "price": 15.99, "description": "A comfortable cotton t-shirt."},
    {"id": 2, "name": "Jeans", "price": 39.99, "description": "Stylish blue jeans."},
    {"id": 3, "name": "Jacket", "price": 59.99, "description": "A warm winter jacket."},
    {"id": 4, "name": "Shoes", "price": 49.99, "description": "Comfortable running shoes."},
]

@app.route('/')
def home():
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
