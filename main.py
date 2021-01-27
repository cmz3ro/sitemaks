from flask import Flask, render_template, url_for, request, flash, session, redirect, abort

app = Flask(__name__,static_url_path='/static')
app.config['SECRET_KEY'] = 'fdgdfgdfggf786hfg6hfg6h7f'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact-us')
def contact_us():
    return render_template('contact-us.html')


if __name__ == "__main__":
    app.run(debug=True,host='localhost')