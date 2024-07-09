import click
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def init_db():
    db.create_all()


@click.command("init-auth-db")
@with_appcontext
def init_db_command():
    try:
        init_db()
        click.echo("Initialized the authentication database.")
    except Exception as e:
        click.echo(f"Couldnt initialize database {e}")


def init_app(app):
    db.init_app(app)
    app.cli.add_command(init_db_command)