import pandas as pd
import matplotlib.pyplot as plt

chess_dataframe = pd.read_csv('C:/Users/48512/Desktop/python_projects/winter23/found_online/11/games.csv')

def generate_turns_histograms(chess_dataframe):

    resigned_games = chess_dataframe[chess_dataframe['victory_status'] == 'resign']

    drawn_games = chess_dataframe[chess_dataframe['victory_status'] == 'draw']

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.hist(resigned_games['turns'], bins=20, color='skyblue', edgecolor='black')
    plt.title('Histogram of Turns for Resigned Games')
    plt.xlabel('Number of Turns')
    plt.ylabel('Frequency')

    plt.subplot(1, 2, 2)
    plt.hist(drawn_games['turns'], bins=20, color='lightcoral', edgecolor='black')
    plt.title('Histogram of Turns for Drawn Games')
    plt.xlabel('Number of Turns')
    plt.ylabel('Frequency')

    plt.tight_layout()
    plt.show()

generate_turns_histograms(chess_dataframe)
