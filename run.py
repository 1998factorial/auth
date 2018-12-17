from flask_script import Manager
from route import app

manager = Manager(app)

if __name__ == "__main__":
	app.run(debug=True,port=8888)