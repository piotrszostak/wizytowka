from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/me', methods=['GET'])
def me():
    print("We received GET")
    return render_template("me.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        print(request.form['message'])
    return render_template("contact.html")


