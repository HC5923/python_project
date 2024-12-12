'''
VS Code의 Extension으로 설치한 pygame은 Python 모듈을 설치한 것이 아닙니다.
Extensions는 개발 환경 설정에 도움을 줄 수 있지만, 실제 Python 실행 환경에서 필요한 모듈(pygame)은 Python의 패키지 관리자(pip)를 통해 설치해야 합니다.

즉, Extension에서 pygame을 설치했다고 해서 Python 코드에서 바로 사용할 수 있는 것은 아닙니다.

현재 해야 할 작업
1. Python 패키지로 pygame 설치 필요
앞서 설명한 방법 중 하나를 선택해 pygame을 설치해야 합니다.
 가장 추천하는 방법은 **가상 환경(Virtual Environment)**입니다.
1) 가상 환경 설정
python3 -m venv venv

2) 가상 환경 활성화
source venv/bin/activate

3) pygame 설치
python -m pip install pygame

2. VS Code에서 올바른 Python 인터프리터 선택
설치 후, VS Code에서 Python 인터프리터를 가상 환경으로 설정해야 합니다.
- 좌측 하단의 Python 인터프리터 설정: 클릭하고, venv로 설정한 Python 인터프리터를 선택하세요.

1) 확인
설치 완료 후 pygame이 제대로 설치되었는지 확인하려면 다음 명령어를 실행하세요.
python -m pip show pygame

Extension과 패키지 설치의 차이
    Extension: 개발 환경에서 코드 자동 완성, 문법 하이라이트 등의 도움을 줍니다.
    pip로 설치한 Python 패키지: Python 코드 실행 시 실제로 사용하는 모듈입니다.

즉, 둘은 역할이 다르며, Extension만 설치해서는 Python 코드에서 pygame 모듈을 사용할 수 없습니다.
'''