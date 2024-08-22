import os
from django.core.management import BaseCommand, call_command
from datetime import datetime, timedelta

class Command(BaseCommand):
    def handle(self, *args, **options):
        backup_dir = 'backups'
        self.stdout.write('Cleaning up old backups...')
        self.delete_old_backups(backup_dir, hours=72)
        
        self.stdout.write('Waiting for database dump...')
        backup_file = os.path.join(
            backup_dir, 
            f'database-{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.json'
        )
        call_command(
            'dumpdata',
            '--natural-foreign',
            '--natural-primary',
            '--exclude=contenttypes',
            '--exclude=admin.logentry',
            '--indent=4',
            f'--output={backup_file}'
        )

    def delete_old_backups(self, directory, hours=72):
        """Delete files in the directory older than the specified number of hours."""
        now = datetime.now()
        cutoff = now - timedelta(hours=hours)
        
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                file_creation_time = datetime.fromtimestamp(os.path.getctime(file_path))
                if file_creation_time < cutoff:
                    os.remove(file_path)
                    self.stdout.write(f'Deleted old backup: {filename}')
