from flask import Flask,render_template,request

app = Flask(__name__, template_folder='templates', static_folder="static")

@app.route('/')
def home():
    return render_template('index.html')

# test


if __name__=='__main__':
    app.run(debug=True)
