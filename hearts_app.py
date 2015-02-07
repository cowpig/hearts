from itertools import ifilter
from flask import Flask
from flask.ext.socketio import SocketIO, emit

live_doc_managers = []

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/hearts/<int:doc_id>')
def get_hearts_doc(doc_id):
    clear_dead_docs()
    print 'hello'
    # return get_doc_manager(doc_id).doc
    return '''<script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/socket.io/0.9.16/socket.io.min.js"></script>
              <script type="text/javascript" charset="utf-8">
                  var socket = io.connect('http://127.0.0.1:5000');
                  socket.on('connect', function() {
                      socket.emit('my event', {data: 'I\'m connected!'});
                  });
              </script>
              '''

@socketio.on('connect', namespace='/chat')
def test_connect():
    print 'connected!'
    emit('my response', {'data': 'Connected'})


def get_doc_manager(doc_id):
    doc_manager = next(ifilter(lambda manager: manager.doc.id == doc_id, live_doc_managers), None)
    if not doc_manager:
        doc_manager = DocManager(get_doc_from_db(doc_id))
        live_doc_managers.append(doc_manager)
    doc_manager.connections.append('''something''')
    return doc_manager


def clear_dead_docs():
    for manager in live_doc_managers:
        if not manager.connections:
            live_doc_managers.remove(manager)

app.run()