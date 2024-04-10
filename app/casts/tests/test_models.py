"""
Test for the Cast Models
"""
from django.test import TestCase
from casts.models import Cast, Award, AwardReceived


def create_cast(role):
    """
    Helper function to create a Cast
    """
    return Cast.objects.create(
        name="Abimbola Ronald",
        well_known_as="Techno Utopian",
        age=180,
        gender="M",
        bio="If not me then who will replace Elon Musk?",
        role=role,
    )


def create_award():
    """
    Helper function to create an award
    """
    return Award.objects.create(
        name="AACTA Awards",
        category="Male Actor of the year",
        description="This award goes to the most active \
            and creative male Actor",
    )


class CastTestCases(TestCase):
    """
    Cast App Models Tests
    """

    def test_creating_an_actor(self):
        """
        Test that creating an actor is successful
        """
        actor = create_cast(role='actor')

        self.assertEqual(str(actor), actor.name)
        self.assertEqual(actor.role, 'actor')
        self.assertEqual(Cast.objects.count(), 1)
        actor_exists = Cast.objects.filter(
            id=actor.id,
            name=actor.name,
        ).exists()
        self.assertTrue(actor_exists)

    def test_creating_a_director(self):
        """
        Test that creating a director is successful
        """
        director = create_cast(role='director')

        self.assertEqual(str(director), director.name)
        self.assertEqual(director.role, 'director')
        self.assertEqual(Cast.objects.count(), 1)
        director_exists = Cast.objects.filter(
            id=director.id,
            name=director.name,
        ).exists()
        self.assertTrue(director_exists)

    def test_creating_an_award(self):
        """
        Test that creating an award is successful
        """
        award = create_award()

        self.assertEqual(str(award), f"{award.name} - {award.category}")
        self.assertEqual(Award.objects.count(), 1)
        award_exists = Award.objects.filter(
            name=award.name,
            category=award.category,
        ).exists()
        self.assertTrue(award_exists)

    def test_giving_an_actor_an_award(self):
        """
        Test that giving an actor an award is suceessful
        """
        actor = create_cast(role='actor')
        award = create_award()

        received_award = AwardReceived.objects.create(
            recipient=actor,
            award=award,
            year_received=2024,
        )

        self.assertEqual(str(received_award), f"{actor.name} - {award.name}")
        self.assertEqual(AwardReceived.objects.count(), 1)
        received_award_exists = AwardReceived.objects.filter(
            id=received_award.id,
            recipient=actor,
            award=award,
            year_received=2024,
        ).exists()
        self.assertTrue(received_award_exists)
        self.assertEqual(actor.awards.count(), 1)
        self.assertEqual(actor.awards.first(), award)
