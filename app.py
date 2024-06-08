# from flask import Flask, render_template
# import requests

# app = Flask(__name__, template_folder='templates')

# @app.route("/")
# # @app.route('/home')
# def hello():
#     return render_template('first day practice.html')
# @app.route("/firstdaypractice",methods=["POST","GET"])
# def firstdaypractice():
#     if requests.method=="post":
#         name=requests.form.get('name')
#         password=requests.form.get('password')
#         return render_template("result.html",name=name,password=password)
   




# # @app.route('/about')
# # def about():
# #     return '<h1>about</h1>'
# # @app.route('/contact')
# # def contact():
# #     return '<h1>contact</h1>'
# # @app.route('/users/<name>')
# # def user(name):
# #     return '<h1>hello {}</h1>'.format(name)
# # if __name__ == '__main__':
# app.run(debug=True)


from flask import Flask, render_template, request
app = Flask(__name__, template_folder='templates')
@app.route("/")
def hello():
    return render_template('firstdaypractice.html')
def firstdaypractice():
    if request.method == "POST":
        name = request.form.get('./name')
        password = request.form.get('password')
        return render_template("result.html", name=name, password=password)
    else:
        return render_template('result.html')  
if __name__ == "__main__":
    app.run(debug=True)

