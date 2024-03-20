from flask import Flask, render_template
import csv
import itertools

app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome to CSC40088 Fundamentals of Computer Science!'

@app.route('/basic')
def display_data():
    with open('data/Kaggle_TwitterUSAirlineSentiment.csv', encoding='utf-8-sig') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        firstline = True
        tweetData = []
        for row in itertools.islice(data, 51):
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
        return render_template('basic.html', tweetData=tweetData)


app.run(host='0.0.0.0', port=81)
