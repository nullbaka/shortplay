from flask import Flask
from flask_socketio import SocketIO
from flask_talisman import Talisman


csp = {
    'style-src': [
            'https://shortplay.herokuapp.com',
            'https://maxcdn.bootstrapcdn.com',
        ],
}

app = Flask(__name__, static_url_path='', 
            static_folder='static')
talisman = Talisman(app, content_security_policy=csp,
                    content_security_policy_nonce_in=['style-src', 'script-src'])
socketio = SocketIO(app, engineio_logger=True)


from app import routes


if __name__ == '__main__':
    socketio.run(app)
