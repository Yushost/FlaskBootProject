from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    return 'this is my homepage!'

@app.route('/yuseon')
def yuseon():
    return render_template('intro.html')

if __name__ == '__main__':
    app.run()
