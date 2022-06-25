from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    db.create_all()
    app.run(host='0.0.0.0', port=port, debub=True)
    manager.run()