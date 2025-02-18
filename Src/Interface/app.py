from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    image = None
    if request.method == "POST":
        image = request.files['image']
        image.save('./static/images/img.jpg')

    return render_template('index.html', image=image)

if __name__ == '__main__':
    app.run(debug=True)