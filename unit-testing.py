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
        raise ConnectionDatabaseError("Can't connect to the databse!")


def get_users_list_from_db(connection_string: str) -> List[Dict[str, str]]:
    """
    Function that gets the list of users from the database and returns them as a list of dict.
    Each user is formatted like that: { 'username': 'jonh Doe', 'birthday': '02/12/1985', 'role': 'admin' }
    The unit test should return at least 20 users.
    The unit test should check that all the users have a username, a birthday and a role.
    """
    db = connect_to_db(connection_string)
    users = db.get_user()
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

        pass

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