from flask import Flask, request, redirect, url_for
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/result/<string:acc_key>/<string:query>/<string:observation_time>/<string:temperature>/<string:precipitation>/<string'
           ':humidity>/<string:visibility>')
def result_current(acc_key, query, observation_time, temperature, precipitation, humidity, visibility):
    return "<h3>Query: {};  <br>Observation Time: {}; <br>Temperature: {}; <br> Precipitation: {}; <br> Humidity: {" \
           "};<br>Visibility: {};<br>Your Access Key:{} </h3>".format(query, observation_time, temperature,
                                                                      precipitation, humidity, visibility, acc_key)


@app.route('/current', methods=['GET', 'POST'])
def current():
    if request.method == 'GET':
        return '''<h1>Please fill out the parameters</h1>
                    <form method="POST" action="/current">
                    <input type="text" name="acc_key">
                    <input type="text" name="query">
                    <input type="submit" value="Request">
                </form>'''
    else:
        acc_key = request.form['acc_key']
        query = request.form['query']

        req = requests.get('http://api.weatherstack.com/current?access_key=' + acc_key + '&query=' + query)
        response = req.json()

        observation_time = response['current']['observation_time']
        temperature = response['current']['temperature']
        precipitation = response['current']['precip']
        humidity = response['current']['humidity']
        visibility = response['current']['visibility']

        return redirect(
            url_for('result_current', acc_key=acc_key, query=query, observation_time=observation_time, temperature=temperature,
                    precipitation=precipitation, humidity=humidity, visibility=visibility))


if __name__ == '__main__':
    app.run()
