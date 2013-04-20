hanja: 한자-한글 변환 라이브러리
=====

[한자-한글 변환기](http://hanja.suminb.com)에서 사용되는 모듈입니다.

Installation
------------

    sudo pip install hanja


Usage
------

### 한글 초성, 중성, 종성 분리

    >>> Hangul.separate(u'가')
    (0, 0, 0)
    >>> Hangul.separate(u'까')
    (1, 0, 0)

튜플(tuple)의 마지막 원소가 0이면 종성이 없는 글자라고 판단할 수 있다.

    >>> Hangul.separate(u'한')
    (18, 0, 4)

'ㅎ'은 19번째 자음, 'ㅏ'는 첫번째 모음, 'ㄴ'은 다섯번째 자음이라는 것을 알 수 있다.

### 초성, 중성, 종성을 조합하여 한 글자를 만듦

    >>> Hangul.synthesize(0, 0, 0)
    u'\uac00'
    >>> print Hangul.synthesize(0, 0, 0)
    가

### 주어진 글자가 한글인지의 여부를 판별

    >>> Hangul.is_hangul(u'가')
    True
    >>> Hangul.is_hangul(u'a')
    False


### 한글로 된 부분과 한자로 된 부분을 분리

리스트가 아닌 제네레이터(generator)를 반환한다.

    >>> '|'.join(Hanja.split_hanja(u'大韓民國은 民主共和國이다.'))
    大韓民國|은 |民主共和國|이다.

    >>> [x for x in Hanja.split_hanja(u'大韓民國은 民主共和國이다.')]
    [u'\u5927\u97d3\u6c11\u570b', u'\uc740 ', u'\u6c11\u4e3b\u5171\u548c\u570b', u'\uc774\ub2e4.']

### 주어진 글자가 한자인지의 여부를 판별

    >>> Hanja.is_hanja(u'韓')
    True

    >>> Hanja.is_hanja(u'한')
    False

### 문장 변환

치환 모드 변환:

    >>> Hanja.translate(u'大韓民國은 民主共和國이다.', 'substitution')
    대한민국은 민주공화국이다.

혼용 모드 변환:

    >>> Hanja.translate(u'大韓民國은 民主共和國이다.', 'combination')
    <span class="hanja">大韓民國</span><span class="hangul">(대한민국)</span>은 <span class="hanja">民主共和國</span><span class="hangul">(민주공화국)</span>이다.
