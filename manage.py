from flask.cli import FlaskGroup
from project import app, db

# Instance
cli = FlaskGroup(app)

@cli.command()
def recreate_db():
    """Recreate Database"""
    db.drop_all()
    db.create_all()
    db.session.commit()

if __name__ == '__main__':
    cli()
