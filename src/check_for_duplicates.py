def check_for_duplicates(dataset):
    unique_ids = []
    cleaned_dataset = []

    for player in dataset:
        if player["ID"] not in unique_ids:
            unique_ids.append(player["ID"])
            cleaned_dataset.append(player)
        else:
            print(f"Player: {player['Name']} duplicated!")

    return cleaned_dataset