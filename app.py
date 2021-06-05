from heroku import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/main')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
