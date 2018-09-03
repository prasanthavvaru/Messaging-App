<h1> Simple ephemeral text message service</h1>
 A production-grade horizontally scalable service that implements
 a simple ephemeral text message service. 

<h2>Endpoints</h2>
<table>
  <tr>
    <th>Functionality</th>
    <th>Method</th>
    <th>Endpoint</th>
  </tr>
  <tr>
    <td>Creates a new text message for passed in username</td>
    <td>POST</td>
    <td>/chat</td>
  </tr>
  <tr>
    <td>Returns the message object for the given id.</td>
    <td>GET</td>
    <td>/chat/id></td>
  </tr>
  <tr>
    <td>Returns a list of all unexpired texts for the user with the given username.</td>
    <td>GET</td>
    <td>/chat/username</td>
  </tr>
</table>

<h2>Requirements</h2>
<a href="https://www.python.org/">Python3</a> (programming language)
<a href="http://flask.pocoo.org/">Flask</a> (Python webframework)
<a href="https://virtualenv.pypa.io/en/stable/">Virtualenv</a>(To isolate Api modules)

<h2> Instructions on how to compile the service </h2>
<h3> Set up Python3 and Virtualenv in your machine</h3>
1.sudo install python3
2.pip install virtualenv

<h3>Clone this repository:</h3>
git clone<a> https://github.com/prasanthavvaru/Messaging-app.git</a>

cd Messaging-App/

<h3>Create a virtual environment in the root directory:</h3>
virtualenv [name of virtualenv]

<h3>Activate the virtualenv:</h3>
source [name of virtualenv]/bin/activate

<h3>Install other important modules</h3>
pip install -r requirements.txt to install the modules

<h3>On your terminal run:</h3>
export FLASK_APP=run.py
expot FLASK_ENV=development

<h2>Instructions on how to run the service locally<h2>
<h3>Run the following command on your terminal</h3>
flask run

<h3>Creates a new text message for passed in username</h3>
Open another instance of your terminal and run the following command
``curl -X POST -H "Content-Type: application/json" -d '{
"username": "Type a your username here",
"text": "Type your message here",
"timeout": "Enter timeout duration without quoters"
}' http://localhost:5000/chat``

<h3>Return a message object for the given id</h3>
Enter the following URL on your browser with the message id
``http://127.0.0.1:5000/chat/id``

<h3>Returns a list of all unexpired texts for the user with the given username.</h3>
Enter the following URL on your browser with the user's username
``http://127.0.0.1:5000/chat/usename``

<h2>The decisions made</h2>
<br>I decided to use the following to accomplish the task<br>
<br>1. Flask : a Python micro webframework<br>
<br>2. List of dictionaries: as storage solution<br>
<br>3. Virtualenv: used to isolate API modules<br>

<h2>Limitations</h2>
<br>1. No authentication needed.<br>
<br>2. Data added when application is running are held temporary.<br> 
<br>3. It is meant only for technical users.<br>

<h2>What i would do if am given more time</h2>
<br>1. Add more endpoints for deleting and updating messages.<br>
<br>2. Implement authentication features.<br>
<br>3. Use a permanent storage solution.<br>
<br>4. Add some tools for testing e.g Pytest<br>

<h2>How to scale it in the future</h2>
By using database which will allow new users and more messages to be saved.

