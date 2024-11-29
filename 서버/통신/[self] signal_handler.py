# signal_test.py
import time
import signal

def handler(signum, frame): # signum: 발생한 신호의 숫자, frame: 프로그램 실행 스텍 프레임
    print("Ctrl+C 신호를 수신했습니다.")

# 처리할 신호 유형, 실행할 함수
signal.signal(signal.SIGINT, handler)

while True:
    print('대기중...')
    time.sleep(10)