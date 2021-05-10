# 패키지
# 도트(.)을 사용하여 모듈을 계층적(디렉터리 구조)으로 관리할 수 있게 해준다.
# ex) 모듈 이름이 A, B일 때 A는 패키지 이름, B는 A 패키지의 B모듈
from package.sound import echo
print(echo.echo_test())
from package.sound.echo import echo_test
print(echo_test())
# from과 import를 통한 패키지 사용
import package.sound.echo
print(package.sound.echo.echo_test())
# import를 통한 패키지 사용

# import package를 수행하면 package 디렉터리의 모듈 or __init__.py에 정의한 것만 참조 가능
# import할 때 가장 마지막 항목은 반드시 모듈 or 패키지

####################################################  __init__의 용도 ########################################################
# __init__.py 파일은 해당 디렉터리가 패키지의 일부임을 알려주는 역할
# 만약 package, sound, graphic등 패키지에 포함된 디렉터리에 __init__.py 파일이 없가면 패키지로 인식 X

from package.sound import *
print(echo.echo_test())
# 특정 디렉터리의 모듈을 *을 사용항 import할 때는 __init__.py 파일에 __all__ 변수를 설정
# 주의할 점
# from의 마지막 항목이 모듈인 경우에는 __all__을 사용할 필요X





# relative package -------> package.graphic.render.py 참조
from package.graphic.render import render_test
print(render_test())

