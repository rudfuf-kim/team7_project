import random

class BaskinRobbins31:
    def __init__(self):
        self.choices = ["가위", "바위", "보"]
        self.current_number = 0

    def determine_order(self) -> str:   #가위바위보를 통해 선공 플레이어를 결정
        
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

    def get_user_count(self) -> int:   #사용자에게 부를 숫자의 개수를 입력받음
        
        while True:
            try:
                count = int(input("\n몇 개의 숫자를 부르시겠습니까? (1~3개): ").strip())
                if count in [1, 2, 3]:
                    return count
                print(">> 경고: 숫자는 1개, 2개 또는 3개만 부를 수 있습니다.")
            except ValueError:
                print(">> 경고: 올바른 정수(1, 2, 3)를 입력해 주세요.")

    def get_computer_count(self) -> int:  
        
        #컴퓨터의 숫자 선언 로직. 무작위(1~3개)로 선택하되, 31을 자의로 외치지 않도록 제한 범위를 설정 
       
        max_safe_count = 30 - self.current_number
        
        # 이미 30에 도달하여 피할 수 없는 경우 31을 부름 (1개)

        if max_safe_count <= 0:
            return 1
            
        # 31을 넘지 않는 안전한 범위 내에서 1~3개 중 무작위 선택

        limit = min(3, max_safe_count)
        return random.randint(1, limit)

    def run(self, life: int) -> int: #메인 메뉴로부터 life 변수를 전달받아 라운드를 진행하고, 종료 후 변경된 life 값을 반환
        
        print("\n====================================")
        print(f"  🍦 베스킨라빈스 31 라운드 시작! (남은 Life: {life})")
        print("====================================")
        
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
# 통합 시스템(메인 메뉴) 시뮬레이션용 코드
# ==========================================

if __name__ == "__main__":
    print("--- 🎮 통합 메인 메뉴 시스템 ---")
    player_life = 10  # 최초 게임 시작 시 부여되는 생명값
    
    # 해당 라운드의 객체를 생성

    round_br31 = BaskinRobbins31()
    
    # 생명값을 인자로 넘겨주고, 게임 결과를 다시 player_life에 덮어씀

    player_life = round_br31.run(player_life)
    
    print("\n--- 메인 메뉴로 복귀 ---")
    print(f"최종 갱신된 플레이어 Life: {player_life}")