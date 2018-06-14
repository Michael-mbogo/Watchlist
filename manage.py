from app import create_app
from flask_script import Manager, Server

#creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

@manager.command
def test():
    '''Run the unittests'''
    import unittest
    tests = unittests.TestLoader().discover('tests')
    unittest.TextTextRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()
