# Import system modules
import datetime

# Import 3rd-party modules
import mysql.connector as mariadb

config = {
    'host': '127.0.0.1',
    'user': 'DBADMIN',
    'password': 'P@ssw0rd!',
    'database': 'chatbot_db',
}

def query_one(qry, var):
    """
    Function for executing `SELECT * FROM table WHERE var0=foo, var1=bar`
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
    Function for executing `SELECT * FROM table WHERE var0=foo, var1=bar`
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

def get_user(user_id):
    qry = "SELECT FROM cb_users (user_id)"

def logs(userid, message, sess):
    qry = """
        INSERT INTO cb_logs 
        (user_id, mess_text, timestamp) 
        VALUES (?, ?, ?)
    """
    time = datetime.datetime.now()
    update(conn, qry, (userid, message, time))

# Message logs
'''
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
'''