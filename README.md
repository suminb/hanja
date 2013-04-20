hanja: 한자-한글 변환 라이브러리
=====

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

조금 더 복잡한 형태의 한글도 분리할 수 있다.

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
