from flask import Flask, render_template, errorhandler

app=Flask(__name__)


#static route
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return "the contact is: 123-456-7890"

@app.route('/post/<int:post_id>')
def services(post_id):
    return "This is post number: {}".format(post_id)

@app.route('/name/<string:name>')
def blog(name):
    return "Hello, {}!".format(name)

def findme():
    return "This is a function that is not a route."

@app.route('/findme')
def findme_route():
    return findme()

@errorhandler(102)
def page_not_found(e):
    return "error found", 404




if __name__ == '__main__':
    app.run(debug=True) 


