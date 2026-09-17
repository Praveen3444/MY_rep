from flask import Flask, render_template

app = Flask(__name__) # This helps flask to find our files and directories

@app.route('/')
def index():
    return render_template("index.html")


 
@app.route('/user/<name>')
def user(name):
    return ("<h1> Hello{}!</h1>".format(name))


if __name__ == '__main__':
    app.run(debug=True) # debug=True will help us to see the errors in the browser
     

    

 

