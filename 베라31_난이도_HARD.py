import random

class BaskinRobbins31:
    def __init__(self):
        self.current_number = 0
        self.choices = ["가위", "바위", "보"]

    def determine_order(self) -> str:    #가위바위보를 통해 선공 플레이어를 결정합니다.
        
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
                print("🎉 가위바위보 승리! 선공(사용자)으로 시작합니다.")
                return "사용자"
            else:
                print("🤖 가위바위보 패배. 선공(컴퓨터)으로 시작합니다.")
                return "컴퓨터"

    def get_user_count(self) -> int:   #사용자에게 몇 개의 숫자를 부를지 입력받고 검증
        
        while True:
            try:
                count = int(input("\n몇 개의 숫자를 부르시겠습니까? (1~3개): ").strip())
                if count in [1, 2, 3]:
                    return count
                print(">> 경고: 숫자는 1개, 2개 또는 3개만 부를 수 있습니다.")
            except ValueError:
                print(">> 경고: 올바른 정수(1, 2, 3)를 입력해 주세요.")

    def get_computer_count(self) -> int:    #컴퓨터의 숫자 개수를 결정 (31을 피하기 위한 인공지능 로직 내장)
    
        # 베스킨라빈스 31 필승 전략 포인트: 2, 6, 10, 14, 18, 22, 26, 30
        # 컴퓨터는 다음 턴에 무조건 '30'을 선점하여 승리하려고 함.

        target = 30
        while target > self.current_number:
            target -= 4
        target += 4  # 현재 숫자보다 큰 가장 가까운 핵심 포인트를 잡음

        # 핵심 포인트를 잡기 위해 필요한 개수 계산

        required_count = target - self.current_number
        
        if required_count in [1, 2, 3]:
            return required_count
        else:
            # 포인트를 잡을 수 없는 상황이라면 무작위(1~3개)로 선택하되, 31을 넘지 않도록 제어

            max_possible = min(3, 31 - self.current_number)
            return random.randint(1, max_possible)

    def play(self, life: int) -> int:    #메인 시스템으로부터 life를 전달받아 게임을 진행하고, 결과에 따라 life를 차감한 뒤 반환

        print("\n====================================")
        print("    🍦 베스킨라빈스 31 게임 시작! 🍦")
        print(f"    [ 현재 보유 중인 라이프: {life} ]")
        print("====================================")
        
        # 1. 선공 결정

        first_turn = self.determine_order()
        self.current_number = 0
        current_turn = first_turn

        # 2. 본 게임 루프

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
                    print("\n😭 당신이 마지막 숫자 31을 외쳤습니다. (패배)")
                    life -= 1  # 패배 시 라이프 차감
                    print(f"❌ 라이프가 1 차감되었습니다. (남은 라이프: {life})")
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
                    print("\n🎉 컴퓨터가 마지막 숫자 31을 외쳤습니다. (승리!)")
                    print(f"✨ 라이프가 보호되었습니다. (남은 라이프: {life})")
                    break
                current_turn = "사용자"

        # 3. 게임 종료 후 결과(life) 반환

        return life

# ==========================================
# 통합 시스템(메인 메뉴) 시뮬레이션용 테스트 코드
# ==========================================

if __name__ == "__main__":
    print("--- 🎮 통합 메인 메뉴 시뮬레이터 ---")
    total_life = 10  # 메인 메뉴에서 부여된 초기 라이프
    
    # 베스킨라빈스 31 라운드 진입

    br31_round = BaskinRobbins31()
    
    # play() 메서드에 total_life를 넘겨주고, 끝난 후의 값을 다시 받아옴

    total_life = br31_round.play(total_life)
    
    print("\n--- 🏠 메인 메뉴로 복귀 ---")
    print(f"최종 업데이트된 라이프: {total_life}")