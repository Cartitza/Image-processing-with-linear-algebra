from flask import Flask, render_template, request, send_file
from Src.Image_Editing.Shear_Mirror import *
from Src.Image_Editing.Rotation import rotate_image
import os
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    image = None
    if request.method == "POST" and not os.path.exists('./static/images/img.png'):
        image = request.files['image']
        image.save('./static/images/img.png')

    if request.method == "POST" and os.path.exists('./static/images/img.png'):
        shear_value_up = request.form.get('shear_up')
        shear_value_down = request.form.get('shear_down')
        shear_value_left = request.form.get('shear_left')
        shear_value_right = request.form.get('shear_right')

        y_axis = request.form.get('y_axis')
        x_axis = request.form.get('x_axis')

        rotation_degrees = request.form.get('rotation_degrees')

        if shear_value_up and shear_value_left:
            image = shear_image('img', float(shear_value_up), float(shear_value_left))
            image.save('./static/images/img.png')

        elif shear_value_up:
            image = shear_image('img', float(shear_value_up), 0)
            image.save('./static/images/img.png')

        elif shear_value_left:
            image = shear_image('img', 0, float(shear_value_left))
            image.save('./static/images/img.png')

        if shear_value_down:
            image = shear_image_down('img', float(shear_value_down))
            image.save('./static/images/img.png')

        if shear_value_right:
            image = shear_image_right('img', float(shear_value_right))
            image.save('./static/images/img.png')

        if y_axis:
            image = mirror_image('img', 'y')
            image.save('./static/images/img.png')

        if x_axis:
            image = mirror_image('img', 'x')
            image.save('./static/images/img.png')

        if rotation_degrees:
            image = rotate_image('img', float(rotation_degrees))
            image.save('./static/images/img.png')


        #return render_template('index.html', image=edited_image)

    return render_template('index.html', image=image)

@app.route('/download')
def download():
    path = './static/images/img.png'
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    if os.path.exists('./static/images/img.png'):
        os.remove('./static/images/img.png')
    app.run(debug=True)