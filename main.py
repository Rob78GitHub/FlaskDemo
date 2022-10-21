from flask import Flask, render_template, request, redirect, url_for

import plotly.express as px

import plotly.express as px
df = px.data.gapminder().query("continent == 'Oceania'")
fig = px.line(df, x='year', y='lifeExp', color='country', markers=True)
#fig.show()
fig.write_html("Templates\plot.html")

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

    return render_template("home.html", Text = read_text, ButtonPressed=0)


@app.route("/button", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('action1') == 'VALUE1':
            pass
            ButtNumber="Button1 pressed"
            fig.show()
        elif request.form.get('action2') == 'VALUE2':
            pass
            ButtNumber="Button2 pressed"
        elif request.form.get('action3') == 'VALUE3':
            pass
            ButtNumber = "Button3 pressed"
        else:
            pass  # unknown
    elif request.method == 'GET':
        return render_template('home.html', form=form)

    return render_template('home.html', Text = read_text, ButtonPressed=ButtNumber)



if __name__ == '__main__':
    app.run()