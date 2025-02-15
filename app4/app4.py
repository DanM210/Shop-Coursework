from flask import Flask, render_template

app = Flask(__name__)

technologies = [

    {"name": "PS5", "price": "£500", "description": "The PS5 is the latest console from Sony.", "image": "PS5.jpg"},
    {"name": "Xbox Series X", "price": "£450", "description": "The Xbox Series X is the latest console from Microsoft.","image":"xbox.jpg"},
    {"name": "Nintendo Switch", "price": "£300", "description": "The Nintendo Switch is a hybrid console from Nintendo.", "image":"nintendo.jpg"},
]

@app.route('/')
def galleryPage():
    return render_template('index.html',technologies = technologies)

@app.route('/tech/<int:techId>')
def singleProductPage(techId):
    return render_template('SingleTech.html', technology = technologies[techId])

if __name__ == '__main__':
    app.run(debug=True)
