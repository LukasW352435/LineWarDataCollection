from html.parser import HTMLParser
from Player import Player

class LineWarHTMLParser(HTMLParser):
    players = None
    table_header = None
    update_time = ""

    def __init__(self, players, table_header):
        super().__init__()
        self.players = players
        self.table_header = table_header

    found_leaderboard = False
    leaderboard_has_data = False

    in_table_leaderboard = False

    in_head = False
    in_head_col = False

    in_body = False
    in_body_row = False
    in_body_col = False
    in_win_streak = False

    found_heading = False
    updated_time_next = False
    in_p_update_time = False

    adding_new_player_counter = 0
    current_player = None

    def handle_starttag(self, tag, attrs):
        if tag == "table":
            if len(attrs) > 0 and attrs[0][0] == "class" and attrs[0][1] == "rankTable":
                self.found_leaderboard = True
                self.in_table_leaderboard = True

        if self.in_table_leaderboard and tag == "thead":
            self.in_head = True
        if self.in_head and tag == "th":
            self.in_head_col = True

        if self.in_table_leaderboard and not self.in_head and tag == "tr":
            self.in_body_row = True
            self.leaderboard_has_data = True
            self.adding_new_player_counter = 0
            self.current_player = Player()
        if self.in_body_row and tag == "td":
            self.in_body_col = True
            if len(attrs) > 0 and attrs[0][0] == "title":
                self.current_player.skill_true = attrs[0][1]
        if self.in_body_col and tag == "img":
            if len(attrs) > 0 and attrs[0][0] == "class" and attrs[0][1] == "win-streak":
                self.in_win_streak = True
                self.current_player.extra = attrs[2][1]

        if tag == "h2":
            self.found_heading = True
        if self.updated_time_next and tag == "p":
            self.in_p_update_time = True

    def handle_endtag(self, tag):
        if self.in_head_col and tag == "tr":
            self.in_head_col = False
        if self.in_head and tag == "thead":
            self.in_head = False
        if self.in_table_leaderboard and tag == "table":
            self.in_table_leaderboard = False

        if self.in_body_row and tag == "tr":
            self.in_body_row = False
            self.players.append(self.current_player)
        if self.in_body_col and tag == "td":
            self.in_body_col = False
        if self.in_win_streak and tag == "img":
            self.in_win_streak = False

        if self.in_p_update_time and tag == "p":
            self.found_heading = False
            self.updated_time_next = False
            self.in_p_update_time = False

    def handle_data(self, data):
        if self.in_head_col and not data.isspace():
            self.table_header.append(data)
        if self.in_body_col and not data.isspace():
            if self.adding_new_player_counter == 0:
                self.current_player.rank = int(data.replace("#", ""))
            if self.adding_new_player_counter == 1:
                self.current_player.name = data
            if self.adding_new_player_counter == 2:
                self.current_player.skill = float(data)
            if self.adding_new_player_counter == 3:
                self.current_player.wins = int(data)
            if self.adding_new_player_counter == 4:
                self.current_player.loses = int(data)

            self.adding_new_player_counter += 1

        if self.found_heading and data == "LEADERBOARD":
            self.updated_time_next = True
        if self.in_p_update_time:
            self.update_time = data
