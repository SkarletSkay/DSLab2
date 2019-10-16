from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def ind():
    return render_template('index.html')


@app.route('/article')
def art():
    return render_template('article.html')


@app.route('/mem')
def mem():
    return render_template('memes.html')


if __name__ == '__main__':
    app.run()
