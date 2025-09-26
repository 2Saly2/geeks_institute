from flask import Flask, render_template
from routes.menu_routes import menu_bp

app = Flask(__name__)

app.register_blueprint(menu_bp)


@app.route('/')
def home():
    return render_template('home.html') 

if __name__ == "__main__":
    app.run(debug=True)

 


