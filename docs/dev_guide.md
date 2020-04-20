# Development Guide
nikl를 이용한 개발 가이드입니다.
<br><br>

## Requirement
<br>

## Quick Start
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
<br>

## Tools
#### 1. 데이터 읽어오기
* .txt 형식의 데이터를 읽어옵니다. 국립국어원 파일 기준으로 작성되었기 때문에 **utf-16** 기준으로 읽어옵니다.
* parameter:
  * input: type(str)
    * filename: 파일명
  * output: type(str)
    * 해당 파일명 안의 내용물 반환
```python
>>> from nikl.loader.loadfile import read_text_file
>>> filename = "test.txt" # 안!!녕#$하%$세요~\n만]나|서\반가&워%^@요
>>> result = read_text_file(filename)
>>> result
>>> "['안!!녕#$하%$세요~\n', '만]나|서\\반가&워%^@요']"
```
<br>

#### 2. 데이터 전처리하기
* 각 함수마다 특정한 데이터를 제거합니다.
  * ```prep_special_char(text)```: 특수문자를 제거합니다.
    * input: type(list)
      * text: 전처리 할 list
    * output: type(list)
    ```python
    >>> from nikl.preprocessor.specificChar import prep_special_char
    >>> text = ['안!!녕#$하%$세요~\n', '만]나|서\\반가&워%^@요']
    >>> result = prep_special_char(text)
    >>> result
    >>> ['안녕하세요', '만나서반가워요']
    ```
  * 다양한 전처리 함수는 후에 업데이트 할 예정입니다.
<br>

#### 3. 데이터 저장하기: 파일 정보 저장 (information)
* ```<teiHeader></teiHeader>``` 사이의 내용을 전처리하여 ```data/파일명_info.txt``` 형태로 저장합니다.
* 파일 구조는 [[docs/info structure.md]](https://github.com/study-artificial-intelligence/nikl/blob/master/docs/info%20structure.md)에서 확인하세요.
* parameter
  * input: type(str), type(str)
    * filename: 파일명
    * raw_text: 전처리 전의 파일 전체 내용. 해당 과정에서 전처리가 자동으로 이루어집니다.
  * output: .txt file
```python
>>> from nikl.target.infos import get_info
>>> from nikl.loader.loadfile import read_text_file
>>> filename = "./data/8CM00002.txt"
>>> raw_text = read_text_file(filename)     # txt 파일 읽고 변수에 저장
>>> get_info(filename, raw_text)            # 전처리 후 data/파일명_info.txt 로 저장
>>> # 파일 저장 완료
```
<br>

#### 4. 데이터 저장하기: 파일 내용 저장 (contents)
* ```<text></text>``` 사이의 내용을 전처리하여 ```data/파일명_content.txt``` 형태로 저장합니다.
* 파일 구조는 [[docs/content structure.md]](https://github.com/study-artificial-intelligence/nikl/blob/master/docs/content%20structure.md)에서 확인하세요.
* parameter
  * input: type(str), type(str), type(bool)
    * filename: 파일명
    * raw_text: 전처리 전의 파일 전체 내용. 해당 과정에서 전처리가 자동으로 이루어집니다.
    * newline: 문장별로 저장 시 개행문자(\n)를 같이 저장할지 선택할 수 있습니다. True를 선택할 시 개행문자를 포함해 내용을 저장할 수 있습니다.
  * output: .txt file
```python
>>> from nikl.target.contents import get_content
>>> from nikl.loader.loadfile import read_text_file
>>> filename = "./data/8CM00002.txt"
>>> newline = True
>>> raw_text = read_text_file(filename)     # txt 파일 읽고 변수에 저장
>>> get_content(filename, raw_text, newline)            # 전처리 후 data/파일명_info.txt 로 저장
>>> # 파일 저장 완료
```