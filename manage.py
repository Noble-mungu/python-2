from app import create_app
from flask_script import Manager,Server
#Flask-Script is a command line for creating startup configuration
#Manager initialize the flask script extension
#Server helps us launch the Server
#Creating the app instance

app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

@manager.command
def test():
	'''
	Run the unit tests
	'''
	import unittest
	tests = unittest.TestLoader().discover('test')
	unittest.textTestRunner(verbosity=2).run(test)


if __name__ == '__main__':
	manager.run()