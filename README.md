# NIKL
국립국어원(**N**ational **I**nstitute of **K**orean **L**anguage) 언어정보나눔터: 말뭉치 파일 전처리 코드
<br>

## Installation
* Pypi: 배포 여부 확인 후 가능하다면 pypi에 올려서 패키지화 예정
  ```bash
  pip install nikl
  ```
* Terminal
  ```bash
  git clone https://github.com/study-artificial-intelligence/nikl.git
  cd nikl
  python setup.py install
  ```
<br>

## Requirements
* beautifulsoup4

다음 명령어를 통해 필요한 패키지들을 설치할 수 있습니다: ```pip install -r requirements.txt```  
(bs4만 필요할 경우 requirements.txt 삭제 예정. 그럴 시 pip install beautifulsoup4 입력으로 대처)
<br>

## Getting Started
1. 변환을 원하는 국립국어원 언어정보나눈센터의 말뭉치 사전을 ```./data```폴더에 넣어주세요.
2. 아래의 명령어에서 대괄호[, ]에 원하는 ```파일명.txt```을 넣어서 사용하세요.<br>
코드가 정상적으로 작동 시, ```./data/```폴더에 파일이름_info.txt, 파일이름_content.txt가 생성됩니다.
```bash
python main.py --filename [파일명.txt] --info --content --newline

# ex1) python main.py --filename test.txt --content --newline
#      test.txt에서 단락 내용만 개행문자를 포함해서 data/test_content.txt 파일 생성
# ex2) python main.py --filename test2.txt test3.txt --info --content
#      text2.txt와 text3.txt에서 파일의 정보와 단락 내용을 각각 저장 후 data/test2_info.txt, test2_content.txt 
#                                                                   data/test3_info.txt, test3_content.txt 파일 생성
```
* filename: 1개 이상의 파일명.txt 형식으로 입력해주세요. 국립국어원 말뭉치 파일 특성 상 txt파일만 지원하고 있습니다.
* info: 해당 파일의 [전반적인 정보](https://github.com/study-artificial-intelligence/nikl/blob/master/docs/info%20structure.md)를 출력할지에 대한 여부를 나타냅니다. 기본값은 False 입니다.
* content: 해당 파일의 [내용](https://github.com/study-artificial-intelligence/nikl/blob/master/docs/content%20structure.md)를 출력할지에 대한 여부를 나타냅니다. 기본값은 False 입니다.
* newline: 본문 내용을 전처리 할 때, 개행문자('\n') 삽입 여부를 나타냅니다. 삽입 시 문단 별로 결과물이 출력됩니다. 기본값은 False 입니다.
