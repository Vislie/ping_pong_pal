import sys
import pytest
from pathlib import Path

src_name = "app"

this_file = Path(__file__)
tests_folder = this_file.parent
project_folder = tests_folder.parent
code_folder = project_folder.joinpath(src_name)

sys.path.insert(0, str(code_folder))

from elo_calculator import calculate_elo

def test_calculate_elo():
    # Test case 1: Winner has higher elo than loser
    winner_start_elo = 1200
    loser_start_elo = 1000
    winner_new_elo, loser_new_elo = calculate_elo(winner_start_elo, loser_start_elo)
    assert winner_new_elo > winner_start_elo
    assert loser_new_elo < loser_start_elo

    # Test case 2: Loser has higher elo than winner
    winner_start_elo = 1000
    loser_start_elo = 1200
    winner_new_elo, loser_new_elo = calculate_elo(winner_start_elo, loser_start_elo)
    assert winner_new_elo > winner_start_elo
    assert loser_new_elo < loser_start_elo

    # Test case 3: Winner and loser have equal elo
    winner_start_elo = 1000
    loser_start_elo = 1000
    winner_new_elo, loser_new_elo = calculate_elo(winner_start_elo, loser_start_elo)
    assert winner_new_elo > winner_start_elo
    assert loser_new_elo < loser_start_elo
    assert loser_new_elo < winner_new_elo

    # Test case 4: Winner and loser have very different elos
    winner_start_elo = 2400
    loser_start_elo = 1000
    winner_new_elo, loser_new_elo = calculate_elo(winner_start_elo, loser_start_elo)
    assert winner_new_elo > winner_start_elo
    assert loser_new_elo < loser_start_elo