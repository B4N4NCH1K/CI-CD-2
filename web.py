from flask import Flask

web=Flask(__name__)

@web.route("/healthz")
def ok():
    return '''
    <html>
        <body>
            <h1>In case I don't see ya, good afternoon, good evening, and good night!</h1>
            <img src="static/truman.png" width="640" height="360">
        </body>
    </html>
    '''

if __name__=="__main__":
    web.run(host="0.0.0.0", port="5555")
