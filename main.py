class Player:
    def __init__(self, name, team):
        self.name = name
        self.xp = 1500
        self.team = team
    def introduce(self):
        print(f"Hello! I'm {self.name} and I play for {self.team}")
class Team:
    def __init__(self, team_name):
        self.name = team_name
        self.players = []

    def show_player(self):
        for player in self.players:
            player.introduce()
    def add_player(self, name):
        new_player = Player(name, self.name)
        self.players.append(new_player)

    def show_total_team_xp(self):
        total_xp = 0
        for player in self.players:
            total_xp = total_xp + player.xp
        print(f"Team {self.name}'s total xp is {total_xp}")


    def delete_player(self, name):
        player_to_remove = None
        for player in self.players:
            if player.name == name:
                player_to_remove = player
                break

        if player_to_remove:
            self.players.remove(player_to_remove)
            print(f"{name}이(가) 팀에서 제거되었습니다.")
        else:
            print(f"{name}이(가) 리스트에 없습니다.")


team_nto = Team("Team NTO")
team_pure = Team("Team pure")
team_nto.add_player("namjun")
team_nto.add_player("aman")
team_nto.show_player()
team_nto.show_total_team_xp()
team_nto.delete_player("aman")


team_pure.add_player("jungKyu")

team_nto.show_player()
#print(team_nto.players[0].name)