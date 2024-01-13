import pandas as pd

df = pd.read_csv('C:/Users/48512/Desktop/python_projects/winter23/found_online/11/games.csv')

def count_fractions(x, y):
    return round(100 * x/y, 2)

def funk(dataframe):
    all_games = len(dataframe['id'])
    print('Number of games in .csv: ', all_games)

    whites_win = 0
    blacks_win = 0
    others = 0

    for win in dataframe['winner']:
        if 'white' == win:
            whites_win += 1
        elif 'black' == win:
            blacks_win += 1
        else:
            others += 1

    print(f"Number of games white won: {whites_win}")
    print(f"Percent of games won by whites: {count_fractions(whites_win, all_games)}")
    print(f"Number of games black won: {blacks_win}")
    print(f"Percent of games won by whites: {count_fractions(blacks_win, all_games)}")
    print(f"Number of games ended other way: {others}")
    print(f"Percent of games ended other way: {count_fractions(others, all_games)}")

funk(df)