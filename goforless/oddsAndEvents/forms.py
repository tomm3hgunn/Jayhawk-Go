from django import forms

from django.contrib.auth.models import User
from .models import Preferences

# TEAMS = ['Buffalo Bills', 'Miami Dolphins', 'New England Patriots', 'New York Jets',
#          'Baltimore Ravens', 'Cincinnati Bengals', 'Cleveland Browns', 'Pittsburgh Steelers',
#          'Houston Texans', 'Indianapolis Colts', 'Jacksonville Jaguars', 'Tennessee Titans',
#          'Denver Broncos', 'Kansas City Chiefs', 'Las Vegas Raiders', 'Los Angeles Chargers',
#          'Dallas Cowboys', 'New York Giants', 'Philadelphia Eagles', 'Washington Commanders',
#          'Chicago Bears', 'Detroit Lions', 'Green Bay Packers', 'Minnesota Vikings',
#          'Atlanta Falcons', 'Carolina Panthers', 'New Orleans Saints', 'Tampa Bay Buccaneers',
#          'Arizona Cardinals', 'Los Angeles Rams', 'San Francisco 49ers', 'Seattle Seahawks']

TEAMS = [('Buffalo Bills', 'Buffalo Bills'), ('Miami Dolphins', 'Miami Dolphins'),
         ('New England Patriots',
          'New England Patriots'), ('New York Jets', 'New York Jets'),
         ('Baltimore Ravens', 'Baltimore Ravens'), ('Cincinnati Bengals',
                                                    'Cincinnati Bengals'),
         ('Cleveland Browns', 'Cleveland Browns'), ('Pittsburgh Steelers',
                                                    'Pittsburgh Steelers'),
         ('Houston Texans', 'Houston Texans'), ('Indianapolis Colts', 'Indianapolis Colts'),
         ('Jacksonville Jaguars',
          'Jacksonville Jaguars'), ('Tennessee Titans', 'Tennessee Titans'),
         ('Denver Broncos', 'Denver Broncos'), ('Kansas City Chiefs', 'Kansas City Chiefs'),
         ('Las Vegas Raiders', 'Las Vegas Raiders'), ('Los Angeles Chargers',
                                                      'Los Angeles Chargers'),
         ('Dallas Cowboys', 'Dallas Cowboys'), ('New York Giants', 'New York Giants'),
         ('Philadelphia Eagles', 'Philadelphia Eagles'), ('Washington Commanders',
                                                          'Washington Commanders'),
         ('Chicago Bears', 'Chicago Bears'), ('Detroit Lions', 'Detroit Lions'),
         ('Green Bay Packers', 'Green Bay Packers'), ('Minnesota Vikings',
                                                      'Minnesota Vikings'),
         ('Atlanta Falcons', 'Atlanta Falcons'), ('Carolina Panthers', 'Carolina Panthers'),
         ('New Orleans Saints', 'New Orleans Saints'), ('Tampa Bay Buccaneers',
                                                        'Tampa Bay Buccaneers'),
         ('Arizona Cardinals',
          'Arizona Cardinals'), ('Los Angeles Rams', 'Los Angeles Rams'),
         ('San Francisco 49ers', 'San Francisco 49ers'), ('Seattle Seahawks', 'Seattle Seahawks')]


class UpdatePreferencesForm(forms.ModelForm):
    favteam = forms.ChoiceField(label='favteam', choices=TEAMS)

    class Meta:
        model = Preferences
        fields = ['favteam']
