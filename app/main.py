from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from elo_calculator import calculate_elo
import player_database


app = Flask(__name__)

# Sample data structure to store player information and ratings
conn = sqlite3.connect('player_database.db', check_same_thread=False)
player_database.create_table(conn)
players = player_database.get_players(conn)

@app.route('/')
def home():
    #players = player_database.get_players(conn)
    return render_template('index.html', players=players)

@app.route('/record_result', methods=['POST'])
def record_result():
    winner = request.form.get('winner')
    loser = request.form.get('loser')

    # Retrieve the current ratings of the winner and loser from the database
    c = conn.cursor()
    c.execute('SELECT rating FROM players WHERE name=?', (winner,))
    winner_rating = c.fetchone()[0]
    c.execute('SELECT rating FROM players WHERE name=?', (loser,))
    loser_rating = c.fetchone()[0]

    # Calculate the new Elo ratings of the winner and loser
    winner_rating, loser_rating = calculate_elo(winner_rating, loser_rating)

    # Update the ratings of the winner and loser in the database
    c.execute('UPDATE players SET rating=? WHERE name=?', (winner_rating, winner))
    c.execute('UPDATE players SET rating=? WHERE name=?', (loser_rating, loser))
    conn.commit()

    return redirect(url_for('home'))
if __name__ == '__main__':
    app.run(debug=True, port=8000)