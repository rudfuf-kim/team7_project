import sympy as sp
import random
import concurrent.futures


class Game1:
    
    def __init__(self):
        self.num0 = random.randint(1,4)
        self.num1 = random.randint(1,9)
        self.num2 = random.randint(1,9)

#랜던값 반아줌
    def get_random(self, start=1, end=9):   
        return random.randint(start, end)

#난이도 고르기
    def difficulty(self):
        print('난이도를 선택합니다)')
        user_abcd = input('A, B, C 중 하나를 골라주세요 : ')
        self.difficulty = self.get_random(1, 3)
        print(f'선택하신 난이도는 {self.difficulty}입니다!')

#정답 입력 타이머, 시간초과 되면 탈락
    def get_answer(self):
        return input('정답을 입력하세요 (5초 제한) : ')


    def ask_with_timeout(self, time_limit=5):
        executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
        future = executor.submit(self.get_answer)
        try:
            answer = future.result(timeout=time_limit)
            return answer
        
        except concurrent.futures.TimeoutError:
            #print('땡!🔔 시간 초과!')
            return None

#난이도 1 (구구단, 두자릿수 덧셈 뺄셈)
    def game_1(self):
        print(' [ 난이도 1 연산이 시작됩니다 ]')
        
        # 랜덤 연산자
        operator = random.choice(['+', '-', '*'])
        
        if operator == '*':
            # 구구단
            num1 = self.get_random(2, 9)
            num2 = self.get_random(1, 9)
            correct_answer = num1 * num2
        else:
            # 두 자릿수와 세 자릿수 문제
            num1 = self.get_random(10, 99) 
            num2 = self.get_random(10, 99)   
            
            if operator == '+':
                correct_answer = num1 + num2
            else: #뺄셈
                correct_answer = num1 - num2

        # 문제 출력
        print(f"문제: {num1} {operator} {num2} = ?")
        
        while True:
            # 5초 타이머 
            user_ans = self.ask_with_timeout(5)
            
            # 결과 판별
            if user_ans is None:
                print(f" 땡🔔 시간 초과! 정답은 {correct_answer} 였습니다.")
                return False
                
            try:
                if int(user_ans) == correct_answer:
                    print("딩동댕🎵 정답입니다!")
                    return True
                else:
                    print(f"틀렸습니다! 정답은 {correct_answer} 였습니다.")
                    return False
                
            except ValueError:
                print(f"숫자만 다시 입력해주세요.")


    #난이도 2 (구구단, 두자릿수 덧셈 뺄셈)
    def game_2(self):
        print(' [ 난이도 2 연산이 시작됩니다 ]')
        
        # 랜덤 연산자
        operator = random.choice(['+', '-', '*'])
        
        if operator == '*':

            num1 = self.get_random(10, 99)
            num2 = self.get_random(0, 9)
            correct_answer = num1 * num2
        else:
            # 세자리수, 두자리수
            num1 = self.get_random(100, 999) 
            num2 = self.get_random(10, 99)   
            
            if operator == '+':
                correct_answer = num1 + num2
            else: #뺄셈
                correct_answer = num1 - num2

        # 문제 출력
        print(f"문제: {num1} {operator} {num2} = ?")
        
        while True:
            # 5초 타이머 
            user_ans = self.ask_with_timeout(5)
            
            # 결과 판별
            if user_ans is None:
                print(f" 땡🔔 시간 초과! 정답은 {correct_answer} 였습니다.")
                return False
                
            try:
                if int(user_ans) == correct_answer:
                    print("딩동댕🎵 정답입니다!")
                    return True
                else:
                    print(f"틀렸습니다! 정답은 {correct_answer} 였습니다.")
                    return False
                
            except ValueError:
                print(f"숫자만 다시 입력해주세요.")

    #난이도 3 게임
    def game_3(self):
        print('[ 난이도 3 연산이 시작됩니다. ]')
                
        x = sp.Symbol('x')
        
        # 2: sin, 3: cos, 4: tan, 5: log, 6: exp
        f_type = random.randint(1, 6)
        
        #if f_type == 1:
            # 5차 이하 다항함수
        #    degree = random.randint(2, 5)
        #    expr = 0
        #    for d in range(1, degree + 1):
        #        coeff = random.randint(-5, 5)
        #        expr += coeff * (x**d)
            # 상수가 0일 때 예외
        #    if expr == 0: 
        #        expr = x**2
        #else:
            
        coeff = random.randint(1, 5)
        if f_type == 2: expr = coeff * sp.sin(x)
        elif f_type == 3: expr = coeff * sp.cos(x)
        elif f_type == 4: expr = coeff * sp.tan(x)
        elif f_type == 5: expr = coeff * sp.log(x)
        elif f_type == 6: expr = coeff * sp.exp(x)

        # 
        correct_answer = sp.diff(expr, x)

        # 3. 문제 출력
        print("다음 함수를 x에 대해 미분하세요.")
        sp.pprint(sp.Eq(sp.Symbol('f(x)'), expr))
        print("(입력 예시: 3*x**2, 2*cos(x), exp(x), 5/x 등)")
        
        # 4. 입력 및 채점
        while True:
            # 시간 제한 10초
            user_ans = self.ask_with_timeout(10)
            
            if user_ans is None:
                correct_answer_p = sp.pprint(correct_answer)
                print(f" 땡🔔 시간 초과! 정답은 {correct_answer_p} 였습니다.")
                #sp.pprint(correct_answer)
                return False
                
            try:
                # 사용자가 입력한 문자열을 SymPy 수식 객체로 변환
                user_expr = sp.sympify(user_ans)
                
                # 수학적 동치 확인 (예: 2*x + 2*x 라고 입력해도 4*x와 같게 판정)
                if user_expr.equals(correct_answer):
                    print("딩동댕🎵 정답입니다!")
                    return True
                else:
                    correct_answer_p = sp.pprint(correct_answer)
                    print(f"틀렸습니다! 정답은 {correct_answer_p} 였습니다.")
                    return False
                    
            except sp.SympifyError:
                print("수식 기호가 잘못되었습니다! 다시 입력해주세요.")
                print("※ 주의: 곱하기는 *, 거듭제곱은 ** 로 써야 합니다. (예: 3*x**2)")









#난이도 1 (구구단, 두자릿수 덧셈 뺄셈)

#난이도 2 (세자리수 이상)

#난이도 3 (괄호 사칙연산)

#난이도 4 (미분)

#5초 타이머

my_game = Game1()
#my_game.ft_ask_with_timeout()
my_game.game_3()