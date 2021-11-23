"""
This script runs the Postin application using a development server.
"""


from os import environ
from Postin import app


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, debug=True)


#    HOST = environ.get('SERVER_HOST', 'localhost')
#    try(
#    PORT = int(environ.get('SERVER_PORT', '443'))
#    except ValueError:
#    PORT = 443
#    app.run(HOST, PORT)