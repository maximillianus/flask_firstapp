from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
	user_agent = request.headers.get('User-Agent')
	return render_template('index.html.j2', user_agent=user_agent)
	#return "<p>Your Browser is: %s</p>" % user_agent

## If running with 'python hello.py' command
# if __name__ == '__main__':
# 	app.run()