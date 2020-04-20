# NIKL
[![Python](https://img.shields.io/pypi/pyversions/nikl.svg?style=plastic)](https://badge.fury.io/py/nikl)
[![PyPI](https://badge.fury.io/py/nikl.svg)](https://badge.fury.io/py/nikl)  
국립국어원(**N**ational **I**nstitute of **K**orean **L**anguage) 언어정보나눔터: 말뭉치 파일 전처리 코드
<br><br>

## Installation
* Pypi
  ```bash
  pip install nikl
  ```
* Source Code
  ```bash
  git clone https://github.com/study-artificial-intelligence/nikl.git
  cd nikl
  python setup.py install
  ```
<br>

## Requirements
* beautifulsoup4 &nbsp;&nbsp;&nbsp; (```pip install beautifulspul4```로 설치)
<br>

## Getting Started
1. 변환을 원하는 국립국어원 언어정보나눔센터의 말뭉치 사전을 ```./data```폴더에 넣어주세요.
2. 아래의 명령어에서 대괄호[, ]로 묶여있는 것들 중 선택해서 사용하세요.<br>단, ```--filename```에는 반드시 한 개 이상의 파일명이 들어가야 합니다.
3. 코드가 정상적으로 작동 시, ```./data/```폴더에 ```파일이름_info.txt```, ```파일이름_content.txt```가 생성됩니다.
```bash
python main.py --filename [파일명.txt] [--info] [--content] [--newline]

# ex1) python preprocess.py --filename test.txt --content --newline
#      test.txt에서 단락 내용만 개행문자를 포함해서 data/test_content.txt 파일 생성
# ex2) python preprocess.py --filename test2.txt test3.txt --info --content
#      text2.txt와 text3.txt에서 파일의 정보와 단락 내용을 각각 저장 후 data/test2_info.txt, test2_content.txt 
#                                                                    data/test3_info.txt, test3_content.txt 파일 생성
```
* filename: 1개 이상의 파일명.txt 형식으로 입력해주세요. 국립국어원 말뭉치 파일 특성 상 txt 파일만 지원하고 있습니다.
* info: 해당 파일의 [전반적인 정보](https://github.com/study-artificial-intelligence/nikl/blob/master/docs/info%20structure.md)를 출력할지에 대한 여부를 나타냅니다. 기본값은 False 입니다.
* content: 해당 파일의 [내용](https://github.com/study-artificial-intelligence/nikl/blob/master/docs/content%20structure.md)를 출력할지에 대한 여부를 나타냅니다. 기본값은 False 입니다.
* newline: 본문 내용을 전처리 할 때, 개행문자('\n') 삽입 여부를 나타냅니다. 삽입 시 문단 별로 결과물이 출력됩니다. 기본값은 False 입니다.
