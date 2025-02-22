import json
from datetime import datetime
from flask import Flask, render_template, request, redirect, flash, url_for


def loadClubs():
    with open('clubs.json') as c:
        listOfClubs = json.load(c)['clubs']
        return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
        listOfCompetitions = json.load(comps)['competitions']
        return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()
datenow = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
PpP = 3


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def showSummary():
    try:
        club = [club for club in clubs if club['email']
                == request.form['email']][0]
    except:
        flash("Unknown email, please try again.")
        return render_template('index.html')
    return render_template('welcome.html', club=club, competitions=competitions, datenow=datenow)


@app.route('/book/<competition>/<club>')
def book(competition, club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template('booking.html', club=foundClub, competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions, datenow=datenow)


@app.route('/purchasePlaces', methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name']
                   == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    if int(club['points']) < (placesRequired * PpP):
        flash("You doesnt have enough points.")
        return render_template('booking.html', club=club, competition=competition)
    if placesRequired > 12:
        flash("You cannot book more than 12 places.")
        return render_template('booking.html', club=club, competition=competition)
    else:
        for comp in competitions:
            if comp['name'] == competition['name']:
                index = competitions.index(comp)
                competitions[index]['numberOfPlaces'] = int(
                    competition['numberOfPlaces']) - placesRequired
        club['points'] = int(club['points']) - (placesRequired * PpP)
        flash('Great-booking complete!')
        return render_template('welcome.html', club=club, competitions=competitions, datenow=datenow)


# TODO: Add route for points display
@app.route('/board', methods=['GET'])
def board():
    return render_template('board.html', clubs=clubs)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
