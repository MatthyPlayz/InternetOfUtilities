from flask import Flask


class Rndb():
    def __init__(self):
        DHOST='0.0.0.0'
        DPORT=int('8080')

    def helloworld():
        return 'Hello, World!'

    def run_app(self, host="0.0.0.0", port=8080, torun=helloworld, route="/"):
        app = Flask('app')

        @app.route(route)
        def rapp():
            return torun()
        
        app.run(host=host, port=port)

def test123():
    return 'heehehheeheehe'

rndb = Rndb()
rndb.run_app(host="localhost", port=8000, torun=test123, route="/")
