# Migrations
 - [Tutorial](https://www.youtube.com/watch?v=N4gjiJumTZg)

 - [Migrations](https://docs.djangoproject.com/en/5.0/topics/migrations/) are Django’s way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema. They’re designed to be mostly automatic, but you’ll need to know when to make migrations, when to run them, and the common problems you might run into.

## The Commands
There are several commands which you will use to interact with migrations and Django’s handling of database schema:

 - `migrate`, which is responsible for applying and unapplying migrations.
 - `makemigrations`, which is responsible for creating new migrations based on the changes you have made to your models.
 - `sqlmigrate`, which displays the SQL statements for a migration. E.G. See all command made behind the scene `./manage.py sqlmigrate blog 0001`
 - `showmigrations`, which lists a project’s migrations and their status.