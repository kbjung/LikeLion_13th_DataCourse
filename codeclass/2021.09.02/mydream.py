# 변수, 클래스, 함수

likecolor = 'orange'

def yourdream(a):
    return a + "너를 응원해"

class myact:
    step = 5000

    def run(self):
        action = "달리기."
        return action

    def play(self):
        action = "놀기."
        return action

# __name__ : 내부적으로 생성되는 변수. 파일을 실행시키면(python mydream.py) __main__으로 적용된다.
# import하면 모듈의 파일명으로 적용된다. 따라서 if문 실행안된다.

if __name__ == "__main__":
    print('mydream 시작')