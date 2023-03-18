.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit


The Django command tool for visualizing migration graphs
========================================================

How to Use
==========

1. Install
----------

Install the pip package locally or globally:

.. code:: shell

    pip install [--user] django-migration-vis

2. Activate
-----------

Enable the Django management command by extending your Django project
settings:

.. code:: python

    INSTALLED_APPS += ("django_migration_vis", )

3. Apply
--------

.. code:: shell

    python manage.py visualizemigrations \
                     --comment 'captions for the picture' \
                     example.gv
