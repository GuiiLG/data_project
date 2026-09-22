def check_for_duplicates(dataset):
    unique_player = []
    for player in dataset:
        if player["ID"] not in unique_player:
            unique_player.append(player["ID"])
        else:
            print(f"Player: {player["Name"]} duplicated!")
            dataset.remove(player)
    return dataset
