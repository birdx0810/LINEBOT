# -*- coding: UTF-8 -*-
# Import system modules
import datetime

# Import 3rd-party modules
import mysql.connector as mariadb

def query_one(qry, var):
    """
    Function for executing `SELECT * FROM table WHERE var0=foo, var1=bar` where
    the result is a single row.
    """
    row = None

    try:
        conn = mariadb.connect(**config)
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(qry, var)
            row = cursor.fetchone()
        except Exception as err:
            print(err)
            print(traceback.format_exc())
        finally:
            cursor.close()
    except Exception as err:
        print(err)
        print(traceback.format_exc())
    finally:
        conn.close()

    if row is None:
        print("Query result is empty")

    return row

def query_all(qry, var):
    """
    Function for executing `SELECT * FROM table WHERE var0=foo, var1=bar` where 
    the result is a list of rows
    """
    rows = []

    try:
        conn = mariadb.connect(**config)
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(qry, var)
            rows = cursor.fetchall()
        except Exception as err:
            print(err)
            print(traceback.format_exc())
        finally:
            cursor.close()
    except Exception as err:
        print(err)
        print(traceback.format_exc())
    finally:
        conn.close()

    if rows == []:
        print("Query result is empty")

    return rows

def update(qry, var):
    """
    Function for updating rows DB (No INSERT)
    """
    is_success = False
    try:
        conn = mariadb.connect(**config)
        conn.autocommit = False
        conn.start_transaction()
        try:
            cursor = conn.cursor()
            cursor.execute(qry, var)
            is_success = True
        except mariadb.Error as err:
            print(err)
            print(traceback.format_exc())
        finally:
            cursor.close()

    except mariadb.Error as err:
        conn.rollback()
        print(err)
        print(traceback.format_exc())
    else:
        conn.commit()
        print("Update successful")
    finally:
        conn.close()

    return is_success

def insert(qry, var):
    """
    Function for inserting rows into DB
    """
    last_row_id = None
    try:
        conn = mariadb.connect(**config)
        conn.autocommit = False
        conn.start_transaction()
        try:
            cursor = conn.cursor()
            cursor.execute(qry, var)
            last_row_id = cursor.lastrowid
        except mariadb.Error as err:
            print(err)
            print(traceback.format_exc())
        finally:
            cursor.close()

    except mariadb.Error as err:
        conn.rollback()
        print(err)
        print(traceback.format_exc())
    else:
        conn.commit()
        print("Insert successful")
    finally:
        conn.close()

    return last_row_id

def log_msg(userid, message, sess):
    qry = """
        INSERT INTO cb_logs 
        (user_id, mess_text, timestamp) 
        VALUES (?, ?, ?)
    """
    time = datetime.datetime.now()
    last_row_id = insert(conn, qry, (userid, message, time))
