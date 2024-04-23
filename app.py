from flask import Flask, render_template
import csv
import itertools

app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome to CSC40088 Fundamentals of Computer Science!'


@app.route('/basic')
def display_data():
    with open('./static/data/TwitterUSAirlineSentiment.csv', encoding='utf-8-sig') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        firstline = True
        tweetData = []
        for row in itertools.islice(data, 41):
            if not firstline:
                tweetData.append({
                    "id": row[0],
                    "airline_sentiment": row[1],
                    "airline_sentiment_confidence": row[2],
                    "negative_reason": row[3],
                    "airline": row[4],
                    "name": row[5],
                    "text": row[6],
                    "tweet_created": row[7],
                    "tweet_location": row[8],
                })
            else:
                firstline = False

        # Sort the data by airline_sentiment_confidence
                
        tweetData.sort(key=lambda x: x["airline_sentiment_confidence"])
        
        # Return the data to the template
        return render_template('basic.html', tweetData=tweetData)


@app.route('/advanced')
def display_data_d3():
    return render_template("advanced.html")

@app.route('/creative')
def display_creative_data():
    return render_template("creative.html")


# app.run(host='0.0.0.0', port=81, debug=True)

app.run(port=81, debug=True)


