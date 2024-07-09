import click
from flask_sqlalchemy import SQLAlchemy
from flask.cli import with_appcontext

db = SQLAlchemy()

def init_db():
    db.create_all()

@click.command('init-recipe-db')
@with_appcontext
def init_db_command():
    try:
        init_db()
        click.echo('Initialized the Recipe database.')
    except Exception as e:
        click.echo(f'Couldnt initialze database: {e}')

def init_app(app):
    db.init_app(app)
    app.cli.add_command(init_db_command)


