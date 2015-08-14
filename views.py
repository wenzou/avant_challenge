from flask import Flask, render_template, request, url_for
from objects import FactorManager

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        factor_manager = FactorManager()
        inputs = []
        #probably want some proper form validation later
        input1 = request.form['input1']
        list = input1.split(',')
        return_data = factor_manager.return_factor(map(int, list))
        return render_template('form_submit.html', error='', return_data=return_data)
    else:
        return render_template('form_submit.html')


if __name__ == '__main__':
    app.run()
