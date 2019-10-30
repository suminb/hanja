hanja: 한자-한글 변환 라이브러리
================================

|Travis CI| |Coveralls|

`한자-한글 변환기`__\ 에서 사용되는 모듈입니다.

__ http://hanja.suminb.com

.. |Travis CI| image:: https://travis-ci.org/suminb/hanja.svg?branch=develop
  :target: https://travis-ci.org/suminb/hanja
.. |Coveralls| image:: https://coveralls.io/repos/github/suminb/hanja/badge.svg?branch=master
  :target: https://coveralls.io/github/suminb/hanja?branch=develop


Improve Hanja Library
---------------------

사용 하시다가 빠진 한자 또는 틀린 독음을 발견하시면 `이 링크
<https://docs.google.com/forms/d/e/1FAIpQLScAtw6ylAhy1t0hMn5K25ZbN1vSNPlRdUtebS9PVtKeLQRfvw/viewform>`_\
를 통해 제보해주세요. 확인 후 반영하도록 하겠습니다. GitHub을 통해 직접 PR을
보내주셔도 좋습니다.


Installation
------------

.. code-block:: console

   pip install hanja


Usage
------

필요한 모듈 import 하기
```````````````````````

>>> import hanja
>>> from hanja import hangul

한글 초성, 중성, 종성 분리
``````````````````````````

>>> hangul.separate('가')
(0, 0, 0)
>>> hangul.separate('까')
(1, 0, 0)

튜플(tuple)의 마지막 원소가 0이면 종성이 없는 글자라고 판단할 수 있다.

>>> hangul.separate('한')
(18, 0, 4)

'ㅎ'은 19번째 자음, 'ㅏ'는 첫번째 모음, 'ㄴ'은 다섯번째 자음이라는 것을 알 수 있다.


초성, 중성, 종성을 조합하여 한 글자를 만듦
``````````````````````````````````````````

>>> hangul.build(0, 0, 0)
'가'


주어진 글자가 한글인지의 여부를 판별
````````````````````````````````````

>>> hangul.is_hangul('가')
True
>>> hangul.is_hangul('a')
False


한글로 된 부분과 한자로 된 부분을 분리
``````````````````````````````````````

리스트가 아닌 제네레이터(generator)를 반환한다.

>>> '|'.join(hanja.split_hanja('大韓民國은 民主共和國이다.'))
大韓民國|은 |民主共和國|이다.

>>> [x for x in hanja.split_hanja('大韓民國은 民主共和國이다.')]
['大韓民國', '은 ', '民主共和國', '이다.']

주어진 글자가 한자인지의 여부를 판별
````````````````````````````````````

>>> hanja.is_hanja('韓')
True

>>> hanja.is_hanja('한')
False

문장 변환
`````````

치환 모드 변환:

>>> hanja.translate('大韓民國은 民主共和國이다.', 'substitution')
'대한민국은 민주공화국이다.'

혼용 모드 변환 (text):

>>> hanja.translate('大韓民國은 民主共和國이다.', 'combination-text')
'大韓民國(대한민국)은 民主共和國(민주공화국)이다.'

혼용 모드 변환 (HTML):

>>> hanja.translate(u'大韓民國은 民主共和國이다.', 'combination-html')
'<span class="hanja">大韓民國</span><span class="hangul">(대한민국)</span>은 <span class="hanja">民主共和國</span><span class="hangul">(민주공화국)</span>이다.'
