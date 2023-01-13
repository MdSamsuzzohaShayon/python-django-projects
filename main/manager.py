from main import app, db
from flask_migrate import Migrate
from flask_script import Manager
from flask_cli import FlaskCLI

FlaskCLI(app)

# migrate = Migrate(app, db)
migrate = Migrate(app, db, command='migrate')
manager = Manager(app)


# manager.add_command("db", MigrateCommand)
@app.cli.command()
def mycmd():
    # flask db init
    # flask db migrate - m "Initial migration."
    # flask db upgrade
    pass


if __name__ == "__main__":
    manager.run()