# Import the built-in unittest module
import unittest
from unittest import mock

from typing import List, Dict


class ConnectionDatabaseError(Exception):  # dit zo laten
    pass


class TestDbError(Exception):  # dit zo laten
    pass


# Function definition
def connect_to_db(connection_string: str):
    """
    Function that connects to the db.

    We will not give you access to the DB yet. So mock this function if you want to test it.

    TODO: add a unit test to verify that this function raises a ConnectionDatabaseError
    when a different connection string than 'test' is provided.
    TODO: add a unit test to verify that this function raises a TestDbError
    when a different connection string than 'test' is provided.
    """

    db = mock.MagicMock()  # mock db connection

    print("connection string: ", connection_string)
    if connection_string == "test":
        raise TestDbError("ERROR: YOU FORGOT TO MOCK connect_to_db")
    else:
        raise ConnectionDatabaseError("Can't connect to the database!")


def get_users_list_from_db(connection_string: str) -> List[Dict[str, str]]:
    """
    Function that gets the list of users from the database and returns them as a list of dict.
    Each user is formatted like that: { 'username': 'jonh Doe', 'birthday': '02/12/1985', 'role': 'admin' }
    The unit test should return at least 20 users.
    The unit test should check that all the users have a username, a birthday and a role.
    """
    db = connect_to_db(connection_string)
    users = [{'username': 'John Doe', 'birthday': '02/12/1985', 'role': 'admin'},
             {'username': 'Frank Sinatra', 'birthday': '04/09/1935', 'role': 'singer'},
             {'username': 'Regis Schulze', 'birthday': '31/12/1990', 'role': 'junior becodian'},
             {'username': 'Frederic de Reu', 'birthday': '20/06/1992', 'role': 'project manager'},
             {'username': 'Cedric Van Rensbergen', 'birthday': '21/12/1989', 'role': 'sales'},
             {'username': 'Eden Hazard', 'birthday': '08/06/1990', 'role': 'footballer'},
             {'username': 'Snoop Dogg', 'birthday': '16/05/1970', 'role': 'rapper'},
             {'username': 'Jessica Alba', 'birthday': '15/11/1972', 'role': 'actress'},
             {'username': 'Idris Elba', 'birthday': '02/08/1965', 'role': 'actor'},
             {'username': 'Joe Biden', 'birthday': '12/06/1945', 'role': 'president'},
             {'username': 'ELon Musk', 'birthday': '02/04/1971', 'role': 'genius'},
             {'username': 'Conor Mcgregor', 'birthday': '25/04/1988', 'role': 'fighter'},
             {'username': 'Julie Schulze', 'birthday': '24/06/1988', 'role': 'sister'},
             {'username': 'Jos Vermuilen', 'birthday': '09/08/1968', 'role': 'tennisplayer'},
             {'username': 'Pablo Picasso', 'birthday': '02/06/1910', 'role': 'artist'},
             {'username': 'Kendrick Lamar', 'birthday': '02/12/1986', 'role': 'rapper'},
             {'username': '50 Cent', 'birthday': '02/11/1975', 'role': 'rapper'},
             {'username': 'Jay Rock', 'birthday': '04/06/1981', 'role': 'rapper'},
             {'username': 'Mos Def', 'birthday': '29/04/1973', 'role': 'rapper'},
             {'username': 'jonh Doe II', 'birthday': '24/11/2011', 'role': 'future admin'}]
    return users


def add(num_1: int, num_2: int, num_3: int) -> int:
    """
    TODO: Add a unit test that tests ALL THE INT between 1 and 200. Every possibility should be tested! (your test can't use more than 10 lines)
    """
    return num_1 + num_2 + num_3


# Unit testing
class TestMathFunctions(unittest.TestCase):
    """Class that will test all the math related functions."""

    def test_connect_to_db(self):
        with self.assertRaises(TestDbError):  # verify if TestDbError is raised
            connect_to_db("test")
        with self.assertRaises(ConnectionDatabaseError):  # verify if ConnectionDatabaseError is raised
            connect_to_db("testing")

    def test_get_users_list_from_db(self):
        users = get_users_list_from_db("test users list")
        #print(f'users: {len(users)}')
        assert len(users) >= 20  # verify if number of users in database is at least 20
        for user in users:
            for j in user.values():
                #print(f'value:{j}')
                assert j != ''  # verify that each user has a username, birthday and role ==> each key has a value

    def test_add(self):
        """
        Function that will unit test the add function with all the int values between 1 and 200.
        - attribute i will have range(1,201) which will give all values from 1 -> 200
        - attribute j will have range(1,201) which will give all values from 1 -> 200
        - attribute k will have range(1,201) which will give all values from 1 -> 200
        by iterating over these attributes in nested for-loops all possibilities will be tested
        """
        for i in range(1, 201):
            for j in range(1, 201):
                for k in range(1, 201):
                    test = add(i, j, k)
                    # print(test)
                    assert test == i + j + k  # verify if add function returns correct values


if __name__ == "__main__":
    # In a .py file use:
    # unittest.main()
    # In jupyter notebook, we need a add some params:
    unittest.main(argv=['first-arg-is-ignored'], exit=False)