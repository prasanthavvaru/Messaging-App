# views.py
import datetime
from app import app
from flask import jsonify,request,abort

#storage solution used: list of dictionaries
#list of texts
texts = [
    {
        'id': 558,
        'username': 'promaster',
        'text': 'Hey everyone!',
        'expiration_date': '2018-10-12 06:22:52',
        'timeout':None
    },
    {
        'id': 559,
        'username': 'james',
        'text': 'This is the best platform ever...',
        'expiration_date': '2018-11-12 08:20:02',
        'timeout':None
    },
    {
        'id': 560,
        'username': 'daniel',
        'text': 'Python programming is fun',
        'expiration_date': '2018-11-12 03:27:00',
        'timeout':None
    },
    {
        'id': 561,
        'username': 'daniel',
        'text': 'Python programming is fun',
        'expiration_date': '2018-12-12 03:27:00',
        'timeout':None
    }
]

#Endpoint to that creates a new text message for passed in username
@app.route('/chat', methods=['POST'])
def create_message():
    if (not request.json or not 'username' in request.json or not
     'text' in request.json):
        abort(400) #Bad request
    timeout = 60
    if 'timeout' in request.json:
        timeout = request.json['timeout']

    now = datetime.datetime.now() + datetime.timedelta(seconds=timeout)
    chat ={
            'id': texts[-1]['id']+1,
            'username': request.json['username'],
            'text': request.json['text'],
            'expiration_date':str(now)[:19],
            'timeout': timeout
        }
    texts.append(chat)
    return jsonify({'id':texts[-1]['id']}),201 #Created

#Endpoint that returns the message object for the given id
@app.route('/chat/<int:id>', methods=['GET'])
def get_message(id):
    msg = [text for text in texts if text['id'] == id]
    if len(msg) == 0:
        abort(404) #Not found
    message = {
        "username": msg[0]['username'],
        "text": msg[0]['text'],
        "expiration_date": msg[0]['expiration_date']
    }
    return jsonify({"Message": message}),200 #OK

'''Endpoint that returns a list of all unexpired texts for the user
with the given username'''
@app.route('/chat/<string:username>', methods=['GET'])
def get_messages(username):
    msg = [text for text in texts if (text['username'] == username and
    text['expiration_date'] > str(datetime.datetime.now())[:19])]
    if len(msg) == 0:
        abort(404) #Not found
    message = []
    for eachmsg in msg:
        message.append({"id": eachmsg['id'],"text": eachmsg['text']})
    return jsonify({"Messages":message})
