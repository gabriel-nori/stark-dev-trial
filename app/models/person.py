from datetime import date, datetime, timedelta
import random

class Person:
    name: str = None
    birth: date = None
    cpf: str = None

    def __init__(
            self,
            name: str = None,
            birth: date = None,
            cpf: str = None
        ) -> None:

        self.name = name
        self.birth = birth
        self.cpf = cpf
    
    def set_random(self):
        self.name = f'{random.choice(first_names)} {random.choice(last_names)}'
        self.birth = self.__get_random_date()
        self.cpf = self.__generate_cpf()


    def __get_random_date(self):
        max_expected_age = 105
        min_accepted_age = 18

        min_expected_birth_date = datetime.now() - timedelta(days=max_expected_age*365)
        max_acceptable_birth_date = datetime.now() - timedelta(days=min_accepted_age*365)

        delta = max_acceptable_birth_date - min_expected_birth_date
        days = random.randint(0, delta.days)
        return min_expected_birth_date + timedelta(days=days)
    
    def __generate_cpf(self): ### Gerador de CPF do Lucascnr                                           
        cpf = [random.randint(0, 9) for x in range(9)]                              
                                                                                    
        for _ in range(2):                                                          
            val = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11      
                                                                                    
            cpf.append(11 - val if val > 1 else 0)                                  
                                                                                    
        return '%s%s%s.%s%s%s.%s%s%s-%s%s' % tuple(cpf)

def validate_cpf(cpf: str):
    cpf = ''.join(filter(str.isdigit, cpf))
    ''' Expects a numeric-only CPF string. '''
    if len(cpf) != 11:
        return False    
    
    if cpf in [s * 11 for s in [str(n) for n in range(10)]]:
        return False
    
    calc = [i for i in range(1, 10)]
    d1= (sum([int(a)*b for a,b in zip(cpf[:-2], calc)]) % 11) % 10
    d2= (sum([int(a)*b for a,b in zip(reversed(cpf[:-2]), calc)]) % 11) % 10
    return str(d1) == cpf[-2] and str(d2) == cpf[-1]

first_names = [
    "Amelia",
    "Benjamin",
    "Clara",
    "David",
    "Eleanor",
    "Felix",
    "Grace",
    "Henry",
    "Isla",
    "Jack",
    "Kayla",
    "Leo",
    "Mia",
    "Noah",
    "Olivia",
    "Paul",
    "Quinn",
    "Rose",
    "Samuel",
    "Tessa",
    "Uma",
    "Victor",
    "Willow",
    "Xavier",
    "Yara",
    "Zoe",
    "Alexander",
    "Beatrice",
    "Charlie",
    "Delilah",
    "Ethan",
    "Freya",
    "Gabriel",
    "Hazel",
    "Isaac",
    "Jasmine",
    "Kyle",
    "Lila",
    "Max",
    "Nina",
    "Oscar",
    "Piper",
    "Quinn",
    "Ryan",
    "Sienna",
    "Thomas",
    "Ursula",
    "Vance",
    "Wren",
    "Xena",
    "Adrian",
    "Bianca",
    "Caleb",
    "Daphne",
    "Elijah",
    "Fiona",
    "George",
    "Holly",
    "Ian",
    "Julia",
    "Kieran",
    "Luna",
    "Miles",
    "Nora",
    "Owen",
    "Penelope",
    "Riley",
    "Sebastian",
    "Taylor",
    "Uma",
    "Vincent",
    "Wendy",
    "Xavier",
    "Yasmine",
    "Zachary",
    "Alice",
    "Brandon",
    "Chloe",
    "Derek",
    "Eva",
    "Finn",
    "Gemma",
    "Holden",
    "Ingrid",
    "Jasper",
    "Kira",
    "Leo",
    "Matilda",
    "Nathan",
    "Ophelia",
    "Preston",
    "Quinn",
    "Rosa",
    "Silas",
    "Talia",
    "Ulysses",
    "Vanessa",
    "Wyatt",
    "Xander",
    "Zola",
]

last_names = [
    "Anderson",
    "Baker",
    "Carter",
    "Davis",
    "Edwards",
    "Foster",
    "Garcia",
    "Harris",
    "Johnson",
    "Kim",
    "Lee",
    "Martinez",
    "Nguyen",
    "O’Brien",
    "Patel",
    "Robinson",
    "Smith",
    "Taylor",
    "Upton",
    "Vasquez",
    "Williams",
    "Young",
    "Zhang",
    "Allen",
    "Bennett",
    "Clark",
    "Diaz",
    "Evans",
    "Fox",
    "Green",
    "Hill",
    "Ingram",
    "Jackson",
    "King",
    "Lewis",
    "Miller",
    "Nelson",
    "Ortiz",
    "Perez",
    "Quinn",
    "Ramirez",
    "Scott",
    "Turner",
    "Underwood",
    "Valdez",
    "Walker",
    "Xu",
    "Yates",
    "Zuniga",
    "Armstrong",
    "Bailey",
    "Collins",
    "Douglas",
    "Edwards",
    "Fisher",
    "Gomez",
    "Howard",
    "Ibrahim",
    "James",
    "Knight",
    "Lopez",
    "Martinez",
    "Nash",
    "Owen",
    "Price",
    "Reed",
    "Sanders",
    "Thomas",
    "Uribe",
    "Vincent",
    "Washington",
    "Xu",
    "Yang",
    "Zimmerman",
    "Alvarado",
    "Brooks",
    "Chen",
    "Davidson",
    "Ewing",
    "Flynn",
    "Graham",
    "Hughes",
    "Jacobson",
    "Kimball",
    "Little",
    "McDonald",
    "Novak",
    "Palmer",
    "Quintero",
    "Roberts",
    "Smithson",
    "Timmons",
    "Vance",
    "Walton",
    "Yates",
    "Zeller",
    "Abdi",
    "Black",
    "Coates",
    "Driscoll",
]
