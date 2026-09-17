def check_for_duplicates(dataset):
    unique_player = []
    for player in dataset:
        if player not in unique_player:
            unique_player.append(player)
        else:
            print(f"Player: {player["Name"]} duplicated!")
            dataset.remove(player)
    return dataset
