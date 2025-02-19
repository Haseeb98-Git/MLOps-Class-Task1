import flask
app = flask.Flask(__name__)
@app. route("/")

def hello_world(): 
	return "Deploying Flask App At Vercel"

if __name__ == '__main__':
    app.run()