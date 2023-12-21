import pandas as pd


firstfilepath= '/Users/murathankarasu/PycharmProjects/CSV_Editor/output.csv'


secondfilepath = '/Users/murathankarasu/PycharmProjects/CSV_Editor/games.csv'


data = pd.read_csv(firstfilepath, nrows=1000)


data.to_csv(secondfilepath, index=False)


print(f'{secondfilepath} completed')
