import random

class BaskinRobbins31Round:
    def __init__(self):
        self.choices = ["가위", "바위", "보"]
        self.current_number = 0

    def select_difficulty(self) -> str:   #게임의 난이도를 선택.
        
        print("\n--- [난이도 선택] ---")
        print("1. EASY") 
        print("2. NORMAL")
        print("3. HARD")
        
        while True:
            choice = input("난이도를 선택하세요 (1/2/3): ").strip()
            if choice == "1": return "EASY"
            elif choice == "2": return "NORMAL"
            elif choice == "3": return "HARD"
            print(">> 올바른 번호를 입력해 주세요.")

    def determine_order(self) -> str:   #가위바위보를 통해 선공 플레이어를 결정.
        
        print("\n--- [선공 결정을 위한 가위바위보] ---")
        while True:
            user_choice = input("가위/바위/보 중 하나를 입력하세요: ").strip()
            if user_choice not in self.choices:
                print(">> 잘못된 입력입니다. '가위', '바위', '보' 중에서 입력해주세요.")
                continue

            computer_choice = random.choice(self.choices)
            print(f"컴퓨터의 선택: {computer_choice}")

            if user_choice == computer_choice:
                print("비겼습니다! 다시!\n")
                continue

            if (user_choice == "가위" and computer_choice == "보") or \
               (user_choice == "바위" and computer_choice == "가위") or \
               (user_choice == "보" and computer_choice == "바위"):
                print("🎉 사용자가 선공입니다.")
                return "사용자"
            else:
                print("🤖 컴퓨터가 선공입니다.")
                return "컴퓨터"

    def get_user_count(self) -> int:
        while True:
            try:
                count = int(input("\n몇 개의 숫자를 부르시겠습니까? (1~3개): ").strip())
                if count in [1, 2, 3]:
                    return count
                print(">> 1개, 2개 또는 3개만 부를 수 있습니다.")
            except ValueError:
                print(">> 정수(1, 2, 3)를 입력해 주세요.")

    def get_computer_count(self, difficulty: str) -> int:   #선택된 난이도에 따라 컴퓨터가 부를 숫자의 개수를 반환.
        
        # 남은 숫자 한계점 (31을 넘어서 부를 수는 없음)
        max_possible = min(3, 31 - self.current_number)

        if difficulty == "EASY":
            # 승패 고려 없이 단순히 1~3개(최대 한도 내) 무작위 선택
            return random.randint(1, max_possible)

        elif difficulty == "NORMAL":
            # 자신이 31을 부르지 않도록 방어
            max_safe = 30 - self.current_number
            if max_safe <= 0:
                return 1  # 이미 30이라 강제로 31을 불러야 하는 상황
            return random.randint(1, min(3, max_safe))

        elif difficulty == "HARD":
            # 체르멜로 정리: 4n + 2 포인트를 선점 (2, 6, 10, 14, 18, 22, 26, 30)
            target = 30
            while target > self.current_number:
                target -= 4
            target += 4  # 현재 숫자보다 큰 가장 가까운 필승 포인트

            required = target - self.current_number
            
            # 필승 포인트를 잡을 수 있는 상황
            if 1 <= required <= 3:
                return required
            # 이미 사용자가 필승 포인트를 점유하여 컴퓨터가 불리한 상황 (최대한 버티기)
            else:
                max_safe = 30 - self.current_number
                if max_safe <= 0:
                    return 1
                return random.randint(1, min(3, max_safe))

    def play_single_game(self, difficulty: str) -> bool:   #단일 게임 로직 (승리하면 True, 패배하면 False 반환)
        
        self.current_number = 0
        current_turn = self.determine_order()

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
                    print("\n😭 마지막 숫자 31을 외쳤습니다. (패배)")
                    return False
                current_turn = "컴퓨터"

            else:
                print(f"\n[ 현재 숫자: {self.current_number} ]")
                print("컴퓨터가 생각 중입니다...")
                count = self.get_computer_count(difficulty)
                
                print("컴퓨터 선언:")
                for _ in range(count):
                    self.current_number += 1
                    print(f"🤖 {self.current_number}")
                    if self.current_number == 31:
                        break
                
                if self.current_number == 31:
                    print("\n🎉 컴퓨터가 31을 외쳤습니다. (승리)")
                    return True
                current_turn = "사용자"

    def run(self, life: int) -> int:
       
        print("\n====================================")
        print(f"  🍦 베스킨라빈스 31 라운드 진입! (현재 Life: {life})")
        print("====================================")
        
        difficulty = self.select_difficulty()

        while life > 0:
            is_win = self.play_single_game(difficulty)

            if is_win:
                print(f"\n✅ 라운드 클리어! 다음 라운드로 진출합니다. (남은 Life: {life})")
                return life
            else:
                life -= 1
                print(f"\n💔 라운드 실패! Life가 1 차감되었습니다. (남은 Life: {life})")
                
                if life == 0:
                    print("💀 Life가 모두 소진되어 게임 오버 처리됩니다.")
                    return 0
                
                print("🔄 해당 라운드를 다시 시작합니다...")
        
        return life

# ==========================================
# 테스트용 메인 시스템 시뮬레이션
# ==========================================

if __name__ == "__main__":
    global_life = 10
    print(f"--- 🎮 메인 메뉴 (초기 Life: {global_life}) ---")
    
    br31_round = BaskinRobbins31Round()
    
    # 실패 시 내부에서 반복 후 최종 결과(Life)만 리턴받음
    global_life = br31_round.run(global_life)
    
    if global_life > 0:
        print(f"\n--- 2라운드로 이동 준비 (현재 Life: {global_life}) ---")
        # next_round.run(global_life)
    else:
        print("\n--- 게임 오버. 메인 메뉴로 강제 귀환 ---")