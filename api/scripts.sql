-- SQLite
SELECT * FROM django_migrations AS dm WHERE dm.app = "core";

DELETE FROM django_migrations AS dm WHERE dm.app = "core";