import os
from app import create_app, db
from app.models import User, Article

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Article': Article }

@app.cli.command()
def test():
    """Runt the unit tests"""
    import unittest
    tests = unittest.TestLoader().discover('app/tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    