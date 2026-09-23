from tests.converters import converters
from tests.duplicates import duplicates
from tests.nulls import nulls

def tests():
    converters()
    duplicates()
    nulls()
    print("Tests passed!")