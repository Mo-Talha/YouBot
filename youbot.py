from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')
@app.route('/dashboard')
def defaultTemplate():
    return render_template('dashboard.html')

@app.route('/process_image', methods=["POST"])
def processImage():
    print(request.files['file']);

if __name__ == '__main__':
    app.debug = True
    app.run()

