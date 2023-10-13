import sqlite3

def create_table(conn):
    """
    Creates a new table called 'players' in the database.
    """
    #conn = sqlite3.connect('player_database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS players
                 (id INTEGER PRIMARY KEY,
                 name TEXT NOT NULL,
                 elo INTEGER NOT NULL);''')
    conn.commit()
    conn.close()


def add_player(conn, name, elo):
    """
    Adds a new player to the 'players' table or updates their Elo rating if they already exist.
    Args: conn (sqlite3.Connection), name (str), elo (int)
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM players WHERE name=?", (name,))
    player = cursor.fetchone()
    if player:
        # Player already exists, update their Elo rating
        cursor.execute("UPDATE players SET elo=? WHERE id=?", (elo, player[0]))
    else:
        # Player doesn't exist, insert a new row
        cursor.execute("INSERT INTO players (name, elo) VALUES (?, ?)", (name, elo))
    conn.commit()


def delete_player(conn, player_id):
    """
    Deletes a player from the 'players' table.
    Args: conn (sqlite3.Connection), player_id (int)
    """
    conn.execute("DELETE FROM players WHERE id=?", (player_id,))
    conn.commit()


def get_players(conn):
    """
    Returns a list of all players in the 'players' table.
    Args: conn (sqlite3.Connection)
    Returns: List of tuples containing (id, name, elo)
    """
    cursor = conn.execute("SELECT * FROM players")
    players = cursor.fetchall()
    return players


def get_elo(conn, player_id):
    """
    Returns the Elo rating of a player.
    Args: conn (sqlite3.Connection), player_id (int)
    Returns: Elo rating (int)
    """
    cursor = conn.execute("SELECT elo FROM players WHERE id=?", (player_id,))
    elo = cursor.fetchone()[0]
    return elo


def update_elo(conn, player_id, elo):
    """
    Updates the Elo rating of a player.
    Args: conn (sqlite3.Connection), player_id (int), elo (int)
    """
    conn.execute("UPDATE players SET elo=? WHERE id=?", (elo, player_id))
    conn.commit()


