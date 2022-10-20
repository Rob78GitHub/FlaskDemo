from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
global Button
Button= 0

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/button', methods=["GET", "POST"])
def button():
    if request.method == "GET":
        global Button


        if Button==0:
         f = open("Static/test.txt", "r")
         txt=f.read()
         f.close()
         Button=1
        else:
            Button==1
            txt=""
            Button=0

        return render_template("home.html", ButtonPressed = txt)
    return redirect(url_for('button'))



if __name__ == '__main__':
    app.run()