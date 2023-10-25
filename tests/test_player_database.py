import pytest
import sqlite3

from app.player_database import add_player, delete_player, get_players, get_elo, update_elo


@pytest.fixture
def database():
    """
    Fixture that creates a new in-memory database for each test.
    """
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS players
                 (id INTEGER PRIMARY KEY,
                 name TEXT NOT NULL,
                 elo INTEGER NOT NULL);''')
    yield conn
    conn.close()


def test_add_player(database):
    add_player(database, 'Alice', 1000)
    add_player(database, 'Bob', 1200)
    add_player(database, 'Charlie', 800)
    assert get_players(database) == [(1, 'Alice', 1000), (2, 'Bob', 1200), (3, 'Charlie', 800)]


def test_update_elo(database):
    add_player(database, 'Alice', 1000)
    update_elo(database, 1, 1100)
    assert get_elo(database, 1) == 1100


def test_delete_player(database):
    add_player(database, 'Alice', 1000)
    add_player(database, 'Bob', 1200)
    delete_player(database, 1)
    assert get_players(database) == [(2, 'Bob', 1200)]


def test_get_players(database):
    add_player(database, 'Alice', 1000)
    add_player(database, 'Bob', 1200)
    assert get_players(database) == [(1, 'Alice', 1000), (2, 'Bob', 1200)]
