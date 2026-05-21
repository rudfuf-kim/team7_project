### 게임규칙
# 컴퓨터가 서로 다른 3개의 정수를 선택해 3자리 숫자 조합
# 사용자에게 서로 다른 3개의 정수 조합을 입력받아 비교
# 숫자와 자릿수가 모두 일치하면 strike
# 숫자는 포함되어있으나, 자릿수가 다르면 ball
# 숫자도 자릿수도 모두 틀리면 out
# 총 10회의 답변기회가 부여되고, 주어진 답변기회 안에 3strike를 맞추면 다음 stage 진출가능
# 주어진 답변기회 안에 3strike를 맞추지 못하면 life 하나 잃음

import random 

class Baseball_game():

    def __init__(self):
        self.qnumloc = {}

    def asking(self):

        self.qnumloc = {}
        used_nums = []
        i = 0

        while len(self.qnumloc) < 3:

            qnum = random.randint(1,9)

            if qnum not in used_nums:
                i += 1
                self.qnumloc[i] = qnum
                used_nums.append(qnum)
        
        return self.qnumloc
    
    
    def answering(self):

        answer = []

        try:

            ans = input("1부터 9까지의 정수 중 서로 다른 숫자 3개를 선택해 입력해주세요. ")

            if len(ans) == 3:

                for i in range(3):
                    anum = int(ans[i])
                    anumloc = {"loc" : i+1, "num" : anum}
                    answer.append(anumloc)
            
            else :
                print("숫자를 3개만 입력해주세요.")
   
        except ValueError:
            
            print("숫자만 입력할 수 있습니다.")
        
        return answer
    

    def play(self):

        qnumloc = self.asking()
        n = 0
        
        for i in range(10):

            anumloc = self.answering()
            n += 1
            results = []

            for i in range(3):

                if qnumloc[i+1] == anumloc[i]["num"] :
                    result = "strike"
                    results.append(result)
                
                elif anumloc[i]["num"] in qnumloc.values():
                    result = "ball"
                    results.append(result)
                
                else:
                    result = "out"
                    results.append(result)
        
            
            sn = results.count("strike")
            bn = results.count("ball")
            on = results.count("out")

            if sn == 3:
                print("3 strike로 승리하였습니다.")
                return True

            elif sn < 3:
                print(f"{n}회 도전 : strike : {sn}, ball : {bn}, out : {on}")

        
        print("답변기회가 더이상 존재하지 않습니다. 패배하였습니다.")
        return False

    def run(self):
        return self.play()