from flask.ext.script import Manager, prompt_bool

from thermos import app,db
from thermos.models import User

manager = Manager(app)


@manager.command
def initdb():
    db.create_all()
    db.session.add(User(username="carlos", email="carlos.hcrespo@gmail.com", password="1234"))
    db.session.add(User(username="ana", email="anacavalcantics@gmail.com", password="1234"))
    db.session.commit()
    print('initialized the database')


@manager.command
def dropdb():
    if prompt_bool(
            "are you sure you want to lose all your date?"):
        db.drop_all()
        print("dropped the database")


if __name__ == '__main__':
    manager.run()
