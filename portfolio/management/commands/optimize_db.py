from django.core.management.base import BaseCommand
from django.db import connection
from django.conf import settings

class Command(BaseCommand):
    help = 'Optimize database for production performance'

    def handle(self, *args, **options):
        if settings.DEBUG:
            self.stdout.write(
                self.style.WARNING('This command should only be run in production')
            )
            return

        with connection.cursor() as cursor:
            # Analyze tables for better query planning
            cursor.execute("ANALYZE;")
            self.stdout.write(
                self.style.SUCCESS('Database tables analyzed successfully')
            )

            # Create indexes for better performance
            try:
                # Index for experience ordering
                cursor.execute("""
                    CREATE INDEX IF NOT EXISTS idx_experience_start_date 
                    ON portfolio_experience(start_date DESC);
                """)
                
                # Index for featured projects
                cursor.execute("""
                    CREATE INDEX IF NOT EXISTS idx_project_featured 
                    ON portfolio_project(is_featured) WHERE is_featured = true;
                """)
                
                # Index for skill categories ordering
                cursor.execute("""
                    CREATE INDEX IF NOT EXISTS idx_skill_category_order 
                    ON portfolio_skillcategory("order");
                """)
                
                self.stdout.write(
                    self.style.SUCCESS('Database indexes created successfully')
                )
            except Exception as e:
                self.stdout.write(
                    self.style.WARNING(f'Some indexes may already exist: {e}')
                )

        self.stdout.write(
            self.style.SUCCESS('Database optimization completed successfully')
        ) 