from Game1 import Game1
import sympy as sp
import random
import concurrent.futures
class Run:
    def run():
        my_game = Game1()
        life = 0
        print(" [ 탈출 1단계, 연산 게임 시작! ] ")


        while True:
            print("원하시는 난이도를 선택해주세요.")
            d = my_game.ft_difficulty()

            print(f'선택하신 난이도는 {d}입니다!')
            
            
            if d == '1':
                my_game.game_1()
            elif d == '2':
                my_game.game_2()
            elif d == '3':
                my_game.game_3()
            #elif choice == 'Q':
            #    print("게임을 종료합니다. 수고하셨습니다!")
            #    break
            else:
                print("잘못된 입력입니다.")
    # app.py를 직접 실행했을 때만 run_game()이 작동하도록 설정
    #if __name__ == "__main__":
    run()