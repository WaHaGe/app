from heroku import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/main', methods=['GET', 'POST'])
def hello_world():
    return render_template('index.md')

if __name__ == '__main__':
    app.run()