from player_database import get_elo, update_elo 

def calculate_elo(winner_start_elo, loser_start_elo):
    """
    Calculates the new elo of the players after a match.
    Args: winner_start_elo (int), loser_start_elo (int)
    Returns: Tuple containing the new elo of the winner and loser
    """
    winner_expected_score = 1 / (1 + 10 ** ((loser_start_elo - winner_start_elo) / 400))
    loser_expected_score = 1 / (1 + 10 ** ((winner_start_elo - loser_start_elo) / 400))
    winner_new_elo = winner_start_elo + 32 * (1 - winner_expected_score)
    loser_new_elo = loser_start_elo + 32 * (0 - loser_expected_score)
    return (winner_new_elo, loser_new_elo)




