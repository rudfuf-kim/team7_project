from games.config import ADMIN_ID, ADMIN_PASSWORD, MAX_LOGIN_ATTEMPTS
from .login_manager import LoginManager
from games.ranking_board import RankingBoard
from games.start_game import Start_game

class GameManager:
    def __init__(self):
        self.login_manager = LoginManager(ADMIN_ID, ADMIN_PASSWORD, MAX_LOGIN_ATTEMPTS)
        self.ranking_board = RankingBoard()
        self.start_game = Start_game()
        self.life = 10
        self.current_stage = 1

    def print_menu(self):
        print("\n===== 탈출 게임 =====")
        print("1. 게임 시작")
        print("2. 랭킹 보드")
        print("3. 게임 종료")

    def input_menu(self):
        while True:
            try:
                choice = input("선택지 입력")
                return choice
            except ValueError:
                print("숫자만 입력해주세요.")


    def run(self):
        if not self.login_manager.login():
            return
        
        while True:
            self.print_menu()
            choice = self.input_menu()

            if choice == "1":
                nickname, life = self.start_game.main_game()
                self.ranking_board.add_record(nickname, life)
            elif choice == "2":
                self.ranking_board.show_ranking()
            elif choice == "3":
                print("게임 프로그램을 종료합니다.")
                break
            else:
                print("잘못된 입력입니다.")
    