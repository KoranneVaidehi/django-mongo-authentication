#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://Vaidehi:Vaidehi09@bdconnectioo.sdnwbgg.mongodb.net/?appName=bdconnectioo"
)

try:
    client.admin.command("ping")
    print("MongoDB connected successfully ✅")
except Exception as e:
    print("MongoDB connection failed ❌", e)


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'databaseConnection.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
