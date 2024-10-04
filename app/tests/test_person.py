from datetime import date, datetime, timedelta
from unittest import TestCase, main
from app.models import Person

class PersonTest:
    person = Person()
    person.set_random()

    def test_age(self):
        """
        To open a bank account, one must be older (or exactly) 18 years old.
        In this case, our client can't be younger than 18 years.
        """

        assert self.person.birth - timedelta(days=18*365) >= 0
    
    def test_cpf(self):
        a=1