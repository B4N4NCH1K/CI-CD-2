from flask import Flask

web=Flask(__name__)

@web.route("/healthz")
def ok():
    return 'OHIO'

if __name__=="__main__":
    web.run(host="0.0.0.0", port="5555")
