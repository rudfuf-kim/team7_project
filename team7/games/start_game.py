class start_game:
    def __init__(self):
        self.player_hp = 10
        self.current_stage = 1
        self.stories = {
            "opening": """
======================================================================
차가운 시멘트 바닥의 감촉에 눈이 떠졌다.
머리가 깨질 듯이 아프고, 내가 누구인지, 왜 여기 있는지 아무것도 기억나지 않는다.
벽면의 모니터에 불이 들어오며 [남은 기회: 10회]라는 글자가 붉게 빛난다.
방 한가운데에는 기괴하게 생긴 첫 번째 장치가 작동하기 시작했다.
======================================================================
""",
            "stage1_clear": """
======================================================================
철컥-! 첫 번째 장치가 해제되며 굳게 닫혀있던 철문이 열렸다.
문 너머로 넘어가자, 더 복잡한 기계들이 가득한 두 번째 방이 나타난다.
혼란을 추스를 새도 없이, 두 번째 보안 장치가 경고음을 울리며 가동된다.
======================================================================
""",
            "stage2_clear": """======================================================================
삐-빅! 두 번째 문이 열리고, 마침내 지상으로 이어지는 계단이 보인다.

"마지막이다. 내 손으로 완성한 시스템을 깨고 여기서 나간다."
최종 방화벽이 작동하며 화면에 마지막 문제가 떠오른다.
======================================================================
""" ,
            "clear": """======================================================================
지상의 환한 햇빛이 지하 계단으로 쏟아져 들어온다.

탈출에 성공하셨습니다! 당신의 이름을 랭킹보드에 기록하세요.
======================================================================
""",
            "gameover": """======================================================================
푸슈우우-... 방 안으로 차가운 수면 가스가 차오르기 시작한다.
점점 의식이 흐려지며 시스템의 마지막 음성이 멀어지듯 들려온다.

당신은 영원히 이 방을 나가지 못할 것입니다.
======================================================================
"""
        }

#스토리 출력 함수
    def print_story(self, scene_key):
        print(self.stories[scene_key])
        input("\n[Enter 키를 누르면 진행됩니다]")

#
    def start(self):
        #1. 오프닝 출력
        self.print_story("opening")

        #2. 첫번쨰 게임
        game1 = Game1()
        while self.current_stage == 1:
            if game1.play():
                self.current_stage += 1
                self.print_story("stage1_clear")
            else:
                self.handle_failure()
                if self.player_hp <= 0:
                    return 0
        
        #3. 두번째 게임
        game2 = Game2()
        while self.current_stage == 2:
            if game2.play():
                self.current_stage += 1
                self.print_story("stage2_clear")
            else:
                self.handle_failure()
                if self.player_hp <= 0:
                    return 0
                
        #4. 세번쨰 게임
        game3 = Game3()
        while self.current_stage == 3:
            if game3.play():
                self.current_stage += 1
                self.print_story("clear")
            else:
                self.handle_failure()
                if self.player_hp <= 0:
                    return 0
                
        return self.player_hp
    
    def handle_failure(self):
        self.player_hp -= 1
        print(f"\n실패! 목숨이 차감되었습니다. (남은 목숨: {self.player_hp}/10)")
        if self.player_hp <= 0:
            self.print_story("gameover")
