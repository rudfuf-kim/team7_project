from games.config import ADMIN_ID, ADMIN_PASSWORD, MAX_LOGIN_ATTEMPTS
from .login_manager import LoginManager

class GameManager:
    def __init__(self):
        self.login_manager = LoginManager(ADMIN_ID, ADMIN_PASSWORD, MAX_LOGIN_ATTEMPTS)
        self.player_hp = 10
        self.current_stage = 1

    def main_menu(self):
        while True:
            print("\n===== 탈출 게임 =====")
            print("1. 게임 시작")
            print("2. 랭킹 보드")
            print("3. 게임 종료")
            choice = input("선택지 입력")

            if choice == "1":
                self.start_game()
            elif choice == "2":
                print("\n(랭킹보드 준비 중...)")
            elif choice == "3":
                print("게임 프로그램을 종료합니다.")
                break
            else:
                print("잘못된 입력입니다.")

    def run(self):
        if not self.login_manager.login():
            return
        
        while True:
            self.main_menu()
    