from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
global Button
Button= 0

with open("test1.txt") as fo:
    read_text = fo.read()
    fo.close()


@app.route('/')
def home():
    with open("test1.txt") as fo:
        read_text = fo.read()
        fo.close()
    return render_template('home.html', Text = read_text)

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/text', methods=["POST"])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    with open("test1.txt", "a") as fo:
        fo.write("\n"+processed_text)
        fo.close()
    with open("test1.txt") as fo:
        read_text=fo.read()
        fo.close()

    return render_template("home.html", Text = read_text)

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
        return render_template("home.html", ButtonPressed = txt, Text = read_text)
    return redirect(url_for('button'))

if __name__ == '__main__':
    app.run()