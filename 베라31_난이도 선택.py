import random

class BaskinRobbins31:
    def __init__(self):
        self.choices = ["가위", "바위", "보"]
        self.current_number = 0
        self.difficulty = "NORMAL" # 기본값

    def select_difficulty(self):  #게임 시작 전 난이도를 선택
        
        print("\n--- [난이도 선택] ---")
        print("1. EASY")     #순수 무작위: 컴퓨터가 스스로 패배할 수도 있습니다.
        print("2. NORMAL")   #안전 지향: 컴퓨터가 무작위로 하되 스스로 31을 부르진 않습니다.
        print("3. HARD")     #필승 전략: 컴퓨터가 체르멜로 정리에 기반하여 완벽하게 방어/공격합니다.

        while True:
            choice = input("난이도를 선택하세요 (1, 2, 3): ").strip()
            if choice == "1":
                self.difficulty = "EASY"
                break
            elif choice == "2":
                self.difficulty = "NORMAL"
                break
            elif choice == "3":
                self.difficulty = "HARD"
                break
            else:
                print(">> 잘못된 입력입니다. 1, 2, 3 중 하나를 입력해주세요.")
        print(f"\n>> [{self.difficulty}] 난이도로 게임을 진행합니다!")

    def determine_order(self) -> str:   #가위바위보를 통해 선공 플레이어 결정
        
        print("\n--- [선공 결정을 위한 가위바위보] ---")
        while True:
            user_choice = input("가위/바위/보 중 하나를 입력하세요: ").strip()
            if user_choice not in self.choices:
                print(">> 잘못된 입력입니다. '가위', '바위', '보' 중에서 입력해주세요.")
                continue

            computer_choice = random.choice(self.choices)
            print(f"컴퓨터의 선택: {computer_choice}")

            if user_choice == computer_choice:
                print("비겼습니다! 다시 안 내면 진 거 가위바위보!\n")
                continue

            if (user_choice == "가위" and computer_choice == "보") or \
               (user_choice == "바위" and computer_choice == "가위") or \
               (user_choice == "보" and computer_choice == "바위"):
                print("🎉 축하합니다! 가위바위보에서 이겨 선공(사용자)으로 시작합니다.")
                return "사용자"
            else:
                print("🤖 컴퓨터가 가위바위보에서 이겨 선공(컴퓨터)으로 시작합니다.")
                return "컴퓨터"

    def get_user_count(self) -> int:   #사용자로부터 선언할 숫자의 개수를 입력받음
        
        while True:
            try:
                count = int(input("\n몇 개의 숫자를 선언하시겠습니까? (1~3개): ").strip())
                if count in [1, 2, 3]:
                    return count
                print(">> 경고: 숫자는 1개, 2개 또는 3개만 선언할 수 있습니다.")
            except ValueError:
                print(">> 경고: 올바른 정수(1, 2, 3)를 입력해 주세요.")

    def get_computer_count(self) -> int:
        
        # 1. EASY 모드: 앞뒤 가리지 않고 1~3개 중 무작위 선택 (31을 넘지 않는 선에서)

        if self.difficulty == "EASY":
            limit = min(3, 31 - self.current_number)
            return random.randint(1, limit)

        # 2. NORMAL 모드: 무작위로 선택하되, 30을 넘기면 무조건 자멸하므로 스스로 31을 부르지 않게 방어

        elif self.difficulty == "NORMAL":
            max_safe_count = 30 - self.current_number
            if max_safe_count <= 0:  # 이미 30이라서 31을 부를 수밖에 없는 상황
                return 1
            limit = min(3, max_safe_count)
            return random.randint(1, limit)

        # 3. HARD 모드: 체르멜로 정리(Zermelo's theorem) 필승 전략 적용
        # 사용자가 31을 부르게 하려면 30을 선점해야 함.
        # 역산하면 필승 포인트는 30, 26, 22, 18, 14, 10, 6, 2 (4n + 2 형태)

        elif self.difficulty == "HARD":
            winning_targets = [2, 6, 10, 14, 18, 22, 26, 30]
            
            for target in winning_targets:
                if target > self.current_number:
                    required_count = target - self.current_number

                    # 다음 필승 포인트에 1~3개의 숫자를 불러서 도달할 수 있다면 무조건 도달

                    if required_count <= 3:
                        return required_count
                    else:
                        break
            
            # 만약 사용자가 이미 필승 포인트를 선점하여 컴퓨터가 도달할 수 없다면,
            # NORMAL 모드와 동일하게 버티기 모드로 무작위(안전 지향) 선언

            max_safe_count = 30 - self.current_number
            if max_safe_count <= 0:
                return 1
            limit = min(3, max_safe_count)
            return random.randint(1, limit)

    def run(self, life: int) -> int:  #메인 메뉴로부터 life변수를 전달받아 라운드 진행 후, 종료 시 변경된 life값을 반환함.
         
        print("\n====================================")
        print(f"  🍦 베스킨라빈스 31 라운드 시작! (남은 life: {life})")
        print("====================================")
        
        # 난이도 선택 및 선공 결정

        self.select_difficulty()
        current_turn = self.determine_order()
        self.current_number = 0

        # 게임 메인 루프

        while self.current_number < 31:
            if current_turn == "사용자":
                print(f"\n[ 현재 숫자: {self.current_number} ]")
                count = self.get_user_count()
                
                print("사용자 선언:")
                for _ in range(count):
                    self.current_number += 1
                    print(f"👉 {self.current_number}")
                    if self.current_number == 31:
                        break
                
                if self.current_number == 31:
                    print("\n😭 당신이 마지막 숫자 31을 외쳤습니다. 컴퓨터 승리!")
                    life -= 1  # 패배 시 Life 1 차감
                    print(f"💔 Life가 1 차감되었습니다. (현재 Life: {life})")
                    break
                
                current_turn = "컴퓨터"

            else:
                print(f"\n[ 현재 숫자: {self.current_number} ]")
                print("컴퓨터가 생각 중입니다...")
                count = self.get_computer_count()
                
                print("컴퓨터 선언:")
                for _ in range(count):
                    self.current_number += 1
                    print(f"🤖 {self.current_number}")
                    if self.current_number == 31:
                        break
                
                if self.current_number == 31:
                    print("\n🎉 컴퓨터가 마지막 숫자 31을 외쳤습니다. 사용자 승리!")
                    print(f"💖 승리하여 Life를 지켜냈습니다! (현재 Life: {life})")
                    break
                
                current_turn = "사용자"
        
        # 게임 종료 후 메인 메뉴로 life 값 반환
        return life

# ==========================================
# 통합 시스템(메인 메뉴) 연동 시뮬레이션
# ==========================================

if __name__ == "__main__":
    print("--- 🎮 통합 메인 메뉴 시스템 ---")
    player_life = 10  # 최초 부여된 life 변수
    
    # 1. 객체 생성
    round_br31 = BaskinRobbins31()
    
    # 2. 게임 실행 및 반환된 life 변수 업데이트
    player_life = round_br31.run(player_life)
    
    print("\n--- 메인 메뉴로 복귀 ---")
    print(f"최종 갱신된 플레이어 Life: {player_life}")