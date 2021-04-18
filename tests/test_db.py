# -*- coding: UTF-8 -*-
# Import system modules
import unittest

# Import 3rd-party modules
import mysql.connector as mariadb

class MockDB(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Only run once before all the tests
        """
        # Drop database if exists

        # Create database


        pass

    @classmethod
    def tearDownClass(cls):
        """Only run once after all tests are done
        """
        conn = mysql.connector.connect(
            host="",
            user="",
            password="",
        )
        cursor = conn.cursor(dictionary=True)
        qry = f"""
            DROP DATABASE {}
        """

        # Drop database
        try:
            cursor.execute(qry)
            conn.commit()
            cursor.close()
        except mysql.connector.Error as err:
            print(f"Failed to drop database {}")

        conn.close()
