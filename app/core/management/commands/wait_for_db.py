"""
Django command to wait for the database to be available.
"""

import time
from typing import Any

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError

from psycopg2 import OperationalError as Psycopg2OpError


class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args: Any, **options: Any) -> Any:
        """Entrypoint for command."""
        self.stdout.write(self.style.NOTICE('Waiting for database...'))

        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write(self.style.WARNING(
                    'Database unavailable, waiting for 1 second...'))
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
