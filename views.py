from flask import Flask, render_template, request, url_for
from objects import FactorManager
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        factor_manager = FactorManager()
        #probably want some proper form validation later
        input1 = request.form['input1']
        list = input1.split(',')
        try:
            return_data = factor_manager.return_factor(map(int, list))
            return render_template('form_submit.html', error='', return_data=return_data)
        except Exception as e:
            return render_template('form_submit.html', error='Error has occurred', return_data='')

    else:
        return render_template('form_submit.html')


# Run the app :)
port = int(os.environ.get('PORT', 5000))

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=port)