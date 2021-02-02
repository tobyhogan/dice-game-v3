import sqlite3
import Game.game_security as security
from Game.game_constants import *

# generic working password: Howard64!!@


def add_user(username, password, theme, volume):
    password = security.hash(password)

    conn = sqlite3.connect(USER_INFO_DB)
    c = conn.cursor()

    c.execute("INSERT INTO users VALUES (?, ?, ?, ?)", (username, password, theme, volume))

    conn.commit()
    conn.close()


def check_user(username, password):
    conn = sqlite3.connect(USER_INFO_DB)
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    try:
        valid = True if security.check_hash(password, c.fetchone()[1]) else False
    except:
        valid = False

    conn.commit()
    conn.close()

    return valid


def update_user_volume(user, update_to):
    conn = sqlite3.connect(USER_INFO_DB)
    c = conn.cursor()

    c.execute("UPDATE users SET volume = ? WHERE username = ?", (update_to, user))

    conn.commit()
    conn.close()


def update_user_theme(user, update_to):
    conn = sqlite3.connect(USER_INFO_DB)
    c = conn.cursor()

    c.execute("UPDATE users SET theme = ? WHERE username = ?", (update_to, user))

    conn.commit()
    conn.close()


def user_exists(username):
    conn = sqlite3.connect(USER_INFO_DB)
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    exists = False if c.fetchall() == [] else True

    conn.commit()
    conn.close()

    return exists


def get_user_details(username):
    conn = sqlite3.connect(USER_INFO_DB)
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    details = c.fetchone()

    conn.commit()
    conn.close()

    return details


def reveal_users_table():
    conn = sqlite3.connect(USER_INFO_DB)
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM users")
    print('____USERS TABLE____')
    for i in c.fetchall():
        print(i)

    conn.commit()
    conn.close()


def clear_users_table():
    conn = sqlite3.connect(USER_INFO_DB)
    c = conn.cursor()

    c.execute("DELETE FROM users")

    conn.commit()
    conn.close()



def add_highscore(username, highscore):
    conn = sqlite3.connect(HIGH_SCORES_DB)
    c = conn.cursor()

    c.execute("INSERT INTO scores VALUES (?, ?)", (username, highscore))

    conn.commit()
    conn.close()


def show_ten_highscores():
    conn = sqlite3.connect(HIGH_SCORES_DB)
    c = conn.cursor()

    c.execute("SELECT * FROM scores ORDER BY score DESC LIMIT 10")
    highscores = c.fetchall()
    highscores = [f'{i[0]}: {i[1]}' for i in highscores]

    conn.commit()
    conn.close()
    return highscores


def reveal_scores_table():
    conn = sqlite3.connect(HIGH_SCORES_DB)
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM scores")
    print('____HIGHSCORES TABLE____')
    for i in c.fetchall():
        print(i)

    conn.commit()
    conn.close()


conn = sqlite3.connect('Data/saved_games.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE saved_games (game_code text, player_one text, player_one_score integer, turn integer, player_two text, player_two_score integer, round integer)")

# cursor.execute("INSERT INTO customers VALUES ('John', 'Elder', 'john@codemy.com')")

cursor.commit()
cursor = conn.cursor()