from random import randint



class Tank():
    tank_logo = "| T |"
    target_logo = "| X |"
    x = 4
    y = 4
    score = 100
    direction = "N"
    shoots = 0
    target_hit = 0
    shoot_directions = {"N": 0, "S": 0, "E": 0, "W": 0}
    top_list = []

    def go_up(self):
        self.y -= 1
        self.score -= 10
        self.direction = "N"

    def go_down(self):
        self.y += 1
        self.score -= 10
        self.direction = "S"

    def go_left(self):
        self.x -= 1
        self.score -= 10
        self.direction = "W"

    def go_right(self):
        self.x += 1
        self.score -= 10
        self.direction = "E"

    def create_target(self):
        self.target_y = randint(0, 8)
        self.target_x = randint(0, 8)
        return self.target_y, self.target_x

    def show_location_and_info(self):
        print(f"Tank is at coordinates: y: {self.y}, x: {self.x}")
        print(f"Direction of the tank: {self.direction}")
        print(f"Made shoots: {self.shoots}")
        print(f"Made shoots by directions: {self.shoot_directions}")

    def draw_battlefield(self):
        self.battlefield = [["|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|"],
                            ["|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|"],
                            ["|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|"],
                            ["|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|"],
                            ["|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|"],
                            ["|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|"],
                            ["|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|"],
                            ["|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|"],
                            ["|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|", "|___|"]
                           ]
        self.battlefield[self.y][self.x] = self.tank_logo
        self.battlefield[self.target_y][self.target_x] = self.target_logo
        for line in self.battlefield:
            print(line)

    def shoot(self):
        self.shoots += 1
        self.shoot_directions[self.direction] += 1
        if self.direction == "N":
            if self.y == self.target_y + 1:
                print("Hit made")
                self.score += 100
                self.target_hit += 1
                self.create_target()
            else:
                self.score -= 10
                print("You missed")
                print("Wrong direction or target to far")

        elif self.direction == "S":
            if self.y == self.target_y - 1:
                print("Hit made")
                self.score += 100
                self.target_hit += 1
                self.create_target()
            else:
                self.score -= 10
                print("You missed")
                print("Wrong direction or target to far")

        elif self.direction == "W":
            if self.x == self.target_x + 1:
                print("Hit made")
                self.score += 100
                self.target_hit += 1
                self.create_target()
            else:
                self.score -= 10
                print("You missed")
                print("Wrong direction or target to far")

        elif self.direction == "E":
            if self.x == self.target_x - 1:
                print("Hit made")
                self.score += 100
                self.target_hit += 1
                self.create_target()
            else:
                self.score -= 10
                print("You missed")
                print("Wrong direction or target to far")

    def check_score(self):
        return self.score

    def check_both_locations(self):
        if (self.x, self.y) == (self.target_x, self.target_y):
            print("///// You drove on target /////")


tankas = Tank()
tankas.create_target()

while True:
    tankas.draw_battlefield()
    tankas.check_both_locations()
    if tankas.check_score() == 0:
        print("End of the game")
        print(f"Shoots made: {tankas.shoots}")
        print(f"Destroyed targets : {tankas.target_hit}")
        name = input("Enter Your Name:  ")
        result = (name, tankas.target_hit)
        tankas.top_list.append(result)
        tankas.x = 4
        tankas.y = 4
        tankas.score = 100
        tankas.direction = "N"
        tankas.shoots = 0
        tankas.target_hit = 0
        tankas.shoot_directions = {"N": 0, "S": 0, "E": 0, "W": 0}
        tankas.draw_battlefield()

    print("Let The Game Begin")
    Choose = input("Choose your actions: "
                   "\n\rMove the Tank (M):"
                   "\n\rMake a Shoot (A): "
                   "\n\rShow tank Info (I): "
                   "\n\rShow score (P): "
                   "\n\rFinish Game (F)"
                   "\n\rShow Top List (T)"
                   "\n\rExit The Game (Q): "
                   )

    if Choose.upper() == "M":
        direction = input("Which direction to move (N,S,W,E): ")
        if direction.upper() == "N":
            tankas.go_up()
        elif direction.upper() == "S":
            tankas.go_down()
        elif direction.upper() == "W":
            tankas.go_left()
        elif direction.upper() == "E":
            tankas.go_right()

    elif Choose.upper() == "A":
        tankas.shoot()

    elif Choose.upper() == "I":
        tankas.show_location_and_info()

    elif Choose.upper() == "P":
        print(tankas.check_score())

    elif Choose.upper() == "T":
        print("//// Score list ////")
        highest_first = tankas.top_list
        highest_first.sort(key=lambda x: x[1], reverse=True)
        for player in highest_first:
            print(player)
        print("/////////////////////")

    elif Choose.upper() == "F":
        tankas.score = 0

    elif Choose.upper() == "Q":
        print("Have a nice day")
        break

    else:
        print("Wrong button, try again")


