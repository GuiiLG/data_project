import src.clean_data as cd
def converters():
    player = {'photoUrl': 'https://cdn.sofifa.com/players/158/023/21_60.png', 'LongName': 'Lionel Messi', 'playerUrl': 'http://sofifa.com/player/158023/lionel-messi/210005/', 'Nationality': 'Argentina', 'Positions': 'RW ST CF', 'Name': 'L. Messi', 'Age': 33, '↓OVA': 93, 'POT': 93, 'Team & Contract': 'FC Barcelona 2004 ~ 2021', 'ID': 158023, 'Height': "5'7", 'Weight': "159lbs", 'foot': 'Left', 'BOV': 93, 'BP': 'RW', 'Growth': 0, 'Joined': 'Jul 1, 2004', 'Loan Date End': None, 'Value': "€67.5M", 'Wage': "€560K", 'Release Clause': "€138.4M", 'Attacking': 429, 'Crossing': 85, 'Finishing': 95, 'Heading Accuracy': 70, 'Short Passing': 91, 'Volleys': 88, 'Skill': 470, 'Dribbling': 96, 'Curve': 93, 'FK Accuracy': 94, 'Long Passing': 91, 'Ball Control': 96, 'Movement': 451, 'Acceleration': 91, 'Sprint Speed': 80, 'Agility': 91, 'Reactions': 94, 'Balance': 95, 'Power': 389, 'Shot Power': 86, 'Jumping': 68, 'Stamina': 72, 'Strength': 69, 'Long Shots': 94, 'Mentality': 347, 'Aggression': 44, 'Interceptions': 40, 'Positioning': 93, 'Vision': 95, 'Penalties': 75, 'Composure': 96, 'Defending': 91, 'Marking': 32, 'Standing Tackle': 35, 'Sliding Tackle': 24, 'Goalkeeping': 54, 'GK Diving': 6, 'GK Handling': 11, 'GK Kicking': 15, 'GK Positioning': 14, 'GK Reflexes': 8, 'Total Stats': 2231, 'Base Stats': 466, 'W/F': 4, 'SM': 4, 'A/W': 'Medium', 'D/W': 'Low', 'IR': 5, 'PAC': 85, 'SHO': 92, 'PAS': 91, 'DRI': 95, 'DEF': 38, 'PHY': 65, 'Hits': 372}
    cd.convert_height(player, "Height")
    cd.convert_weight(player, "Weight")
    cd.convert_money(player, "Value")
    cd.convert_money(player, "Wage")
    cd.convert_money(player, "Release Clause")
    assert player["Height"] == 1.70
    assert player["Weight"] == 72.12
    assert player["Value"] == 67500000
    assert player["Wage"] == 560000
    assert player["Release Clause"] == 138400000
