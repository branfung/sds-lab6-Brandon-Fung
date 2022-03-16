# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# ---- YOUR APP STARTS HERE ----

#LAB6 MEMBERS:
#Brandon Fung Rivera
#Aman Singh

# -- Import section --
from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from model import capitals_output

states_capitals = {'FL': ('Florida', 'Tallahassee'), 'NY': ('NewYork', 'Albany'), 'WA': ('Washington', 'Olympia'), 'CA': ('California', 'Sacramento'), 'NV': ('Nevada', 'Carson city')}

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/results', methods=['GET', 'POST'])
def results():

    if request.method == "GET":
        return redirect('/index')

    answers = {
        'NY': request.form['New York'],
        'CA': request.form['California'],
        'FL': request.form['Florida'],
        'WA': request.form['Washington'],
        'NV': request.form['Nevada']
    }
    # return model.capitals_output(answers)
    # TODO: Create a results.html page that is rendered when the /results route is used in app.py.
    #         Use Jinja templating to include the output of the function in model.py as part of the results.html page.

    #         In app.py, use render_template to send the user to results.html when the form has been filled out (POST request).
    #         Make sure to display to the user which answers are correct and which answers are wrong.
    #         If the form has not been completed (GET request), return a string explaining that they need to go back to the form.


    return render_template('results.html', answers=capitals_output(answers), state = states_capitals)


