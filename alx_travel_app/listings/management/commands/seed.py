from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        # Delete all listings first to avoid duplicates
        Listing.objects.all().delete()

        # Create a sample user to assign listings to
        user, created = User.objects.get_or_create(username='testuser')
        if created:
            user.set_password('password123')
            user.save()

        # Sample listings data
        listings_data = [
            {
                'title': 'Cozy Cottage',
                'description': 'A lovely small cottage in the countryside.',
                'price_per_night': 75.00,
                'location': 'Countryside',
                'owner': user,
            },
            {
                'title': 'Beachfront Villa',
                'description': 'Luxury villa with stunning ocean views.',
                'price_per_night': 250.00,
                'location': 'Beach',
                'owner': user,
            },
            {
                'title': 'City Apartment',
                'description': 'Modern apartment in the city center.',
                'price_per_night': 120.00,
                'location': 'City Center',
                'owner': user,
            },
        ]

        for listing_data in listings_data:
            Listing.objects.create(**listing_data)

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
