import os
from flask import Flask, render_template
from flask import url_for
from flask import redirect  
from flask import request
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "./static/img"

@app.route('/')
def home():
   return render_template('index.html')
"""@app.route('/about')
def about():
   return render_template('about.html')"""

@app.route('/app_scanner')
def app_scanner():
   return render_template('app_scanner.html')

@app.route('/scan', methods=['POST'])
def scan():
   if request.method == 'POST':
      img_o = request.files['imagen_original']
      filename=secure_filename(img_o.filename)
      full_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
      img_o.save(full_filename)
      c = "imagen cargado"
      return c

if __name__ == '__main__':
    app.run(debug=True)


