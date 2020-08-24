# Import 3rd-party modules
import click
import sqlite3
from flask import current_app, g
from flask.cli import with_appcontext

# Import system modules
import datetime, re

# Connect to DB
def connect_db(path):
    try:
        conn = sqlite3.connect(path)
    except Error as e:
        print(e)

    return conn

# Function factory
def query(conn, qry):
    c = conn.cursor()
    c.execute(qry)
    rows = c.fetchall()
    return rows

def var_query(conn, qry, var):
    c = conn.cursor()
    c.execute(qry, var)
    rows = c.fetchall()
    return rows

def update(conn, qry, var):
    c = conn.cursor()
    c.execute(qry, var)
    conn.commit()

def drop(conn, qry, var):
    c = conn.cursor()
    c.execute(qry, var)

# User queries
def check_user(userid, message, sess):
    # Initialize Database
    path = 'medbot.db'
    conn = connect_db(path)

    # Check user in DB
    qry = """SELECT * FROM mb_user WHERE line_id=?"""
    result = var_query(conn, qry, (userid,))

    # New userid detected
    if not result and userid not in sess.status:
        sess.add_status(userid)
        return 'r0'
    # Get user Chinese name
    elif not result and sess.status[userid]['sess_status'] == 'r0':
        if re.match(r'[\u4e00-\u9fff]{2,4}', message):
            sess.status[userid]["user_name"] = message
            sess.status[userid]['sess_status'] = 'r1'
            return 'r1'
        else:
            return "error"
    # Get user birthdate
    elif not result and sess.status[userid]['sess_status'] == 'r1':
        year = int(message[0:4])
        month = int(message[4:6])
        day = int(message[6:8])
        birth = str(year) + '-' + str(month) + '-' + str(day) 
        if len(message)==8 and year <= current_year and 1<=month<=12 and 1<=day<=31:
            sess.status[userid]["user_bday"] = birth
            sess.status[userid]['sess_status'] = 'r2'
            return 'r2'
        else:
            return "error"
    # Get user nric [:-4]
    elif not result and sess.status[userid]['sess_status'] == 'r2':
        if len(message)==4 and re.match(r'[\d]', message):
            name = sess.status[userid]["user_name"]
            birth = sess.status[userid]["user_bday"]
            sess.status[userid]["user_nric"] = message
            nric = message
            qry = "INSERT INTO mb_user (line_id, name, birth, nric) VALUES (?, ?, ?, ?)"
            update(conn, qry, (userid, name, birth, nric))
            sess.status[userid]['sess_status'] = 'r3'
            return 'r3'
        else:
            return "error"

def logs(userid, message, sess):
    qry = "INSERT INTO mb_logs (user_id, mess_text, timestamp) VALUES (?, ?, ?)"
    time = datetime.datetime.now()
    time = time.strftime("%Y.%m.%d %H:%M:%S")
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