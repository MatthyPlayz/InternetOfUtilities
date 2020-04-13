from flask import Flask


class Rndb():
    def __init__(self):
        DHOST='0.0.0.0'
        DPORT=int('8080')

    def helloworld(self):
        return 'Hello, World!'

    def run_app(host="0.0.0.0", port=8080, torun=helloworld, route="/"):
        app = Flask('app')

        @app.route(route)
        def rapp(self):
            return torun()
        
        app.run(host='0.0.0.0', port=8080)

def test123():
    return 'heehehheeheehe'

Rndb().run_app(torun=test123)
