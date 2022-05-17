from LineWarHTMLParser import LineWarHTMLParser


class ParseAndSave:
    players = []
    table_header = []
    save_file = ""
    update_time = ""
    finished = False

    def __init__(self, save_file):
        self.save_file = save_file

    def parse(self, file_To_Parse):
        print("Start parsing " + file_To_Parse)

        self.table_header = []

        f = open(file_To_Parse, "r", encoding='utf-8')
        parser = LineWarHTMLParser(self.players, self.table_header)
        parser.feed(f.read())
        parser.close()

        self.update_time = parser.update_time

        if not parser.found_leaderboard:
            raise NameError("Leaderboard not found.")
        if not parser.leaderboard_has_data:
            self.finished = True
        f.close()
        print("Parsing success.")

    def no_more_data(self):
        return self.finished

    def save(self):
        print("Start saving.")

        self.extract_update_time()

        f = open(self.save_file, "w", encoding='utf-8')
        f.write(self.update_time + "; " + "\n")

        header_line = ""
        for i in self.table_header:
            header_line += i + "; "
        header_line += "Wins in a row; Skill increase; "
        f.write(header_line + "\n")

        for p in self.players:
            f.write(str(p) + "\n")
        f.close()
        print("Saving success.")

    def extract_update_time(self):
        self.update_time = self.update_time.strip()
        if self.update_time.startswith("Ranks last updated "):
            dot = self.update_time.index(".")
            self.update_time = self.update_time[len("Ranks last updated "):dot]
        else:
            print("Could not find update time.")

