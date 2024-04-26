import csv
import itertools
import os
from flask import Flask, render_template, session, copy_current_request_context
from flask_socketio import SocketIO, emit, disconnect, join_room, leave_room, Namespace
from threading import Lock
async_mode = None

app = Flask(__name__)
socket_ = SocketIO(app, async_mode=async_mode)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/basic')
def display_data():
    with open('./static/data/Kaggle_TwitterUSAirlineSentiment.csv', encoding='utf-8-sig') as csvfile:
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

@app.route('/report')
def report():
    return render_template("report.html")

@app.route('/websocket')
def websocket():
    return render_template("websocket.html",
                           sync_mode=socket_.async_mode)


@socket_.on('my_event', namespace='/test')
def test_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': message['data'], 'count': session['receive_count']})


@socket_.on('my_broadcast_event', namespace='/test')
def test_broadcast_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': message['data'], 'count': session['receive_count']},
         broadcast=True)


@socket_.on('disconnect_request', namespace='/test')
def disconnect_request():
    @copy_current_request_context
    def can_disconnect():
        disconnect()

    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': 'Disconnected!', 'count': session['receive_count']},
         callback=can_disconnect)
 
# app.run(host='0.0.0.0', port=81, debug=True)
# port = int(os.environ.get('PORT', 5000))
# socket_.run(app, host='0.0.0.0', port=port)

socket_.run(app, debug=True)