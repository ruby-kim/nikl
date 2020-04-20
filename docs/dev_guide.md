# Development Guide
nikl를 이용한 개발 가이드입니다.
<br><br>

## Requirement
<br>

## Quick Start
1. 변환을 원하는 국립국어원 언어정보나눔센터의 말뭉치 사전을 ```./data```폴더에 넣어주세요.
2. 아래의 명령어에서 대괄호[, ]에 원하는 ```파일명.txt```을 넣어서 사용하세요.<br>
코드가 정상적으로 작동 시, ```./data/```폴더에 ```파일이름_info.txt```, ```파일이름_content.txt```가 생성됩니다.
```bash
python main.py --filename [파일명.txt] --info --content --newline

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
```python
from nikl.loader.load_file import read_text_file

```
<br>

#### 2. 데이터 전처리하기
```python
from nikl.preprocessor.preprocess import preprocess
```
<br>

#### 3. 데이터 저장하기
* 해당 파일 정보 저장하기(information)
  ```python
  from nikl.target import infos
  ```
* 해당 파일 내용 저장하기(contents)
  ```python
  from nikl.target import contents
  ```