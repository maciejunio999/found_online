import pandas as pd

chess_dataframe = pd.read_csv('C:/Users/48512/Desktop/python_projects/winter23/found_online/11/games.csv')

def filter_chess_games(dataframe, criteria):

    if 'min_rating' in criteria:
        dataframe = dataframe[dataframe['white_rating'] >= criteria['min_rating']]
        dataframe = dataframe[dataframe['black_rating'] >= criteria['min_rating']]

        dataframe = dataframe[dataframe['white_rating'] <= criteria['max_rating']]
        dataframe = dataframe[dataframe['black_rating'] <= criteria['max_rating']]

    if 'victory_status' in criteria:
        dataframe = dataframe[dataframe['victory_status'] == criteria['victory_status']]

    subset_filename = 'C:/Users/48512/Desktop/python_projects/winter23/found_online/11/games_subset.csv'
    dataframe.to_csv(subset_filename, index=False)

    return dataframe


filter_criteria = {
    'min_rating': 1500,
    'max_rating': 2000,
    'victory_status': 'outoftime'
}

filtered_games = filter_chess_games(chess_dataframe, filter_criteria)
