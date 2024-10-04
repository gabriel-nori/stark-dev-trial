from datetime import date, datetime, timedelta
from app.models.person import validate_cpf
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

    def test_cpf_validator(self):
        assert validate_cpf("302.208.800-00") == True
        assert validate_cpf("077.000.600-02") == True
        assert validate_cpf("027.000.450-02") == False
        assert validate_cpf("450-02") == False
    
    def test_cpf(self):
        assert validate_cpf(self.person.cpf) == True