import pandas as pd
from prettytable import PrettyTable


# discord ids corresponding to specific people
ids_dict = {237337567534514176: 0, 274757752398544899: 1, 172980261192073217: 2, 852134374673088533: 3, 
358219168757317633: 4, 745771097957466223: 5, 566438950592315426: 6}


def updatecsv(author_id):
    df = pd.read_csv("score.csv")
    df.loc[ids_dict[author_id], "Score"] += 1
    df.to_csv("score.csv", index=False)


def print_leaderboard():
    leaderboard = PrettyTable()
    leaderboard.field_names = ["Player", "Score"]
    with open('score.csv') as f:
        next(f)
        line = f.readline()
        while line:
            leaderboard.add_row(line.rstrip().split(','))
            line = f.readline()
    return leaderboard

if __name__ == '__main__':
    updatecsv(237337567534514176)
    print(print_leaderboard())
