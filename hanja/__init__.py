# -*- coding:utf-8 -*-
"""두음법칙에 관련된 내용은
http://ko.wikipedia.org/wiki/%EB%91%90%EC%9D%8C_%EB%B2%95%EC%B9%99 를 참고.
"""

import warnings


__author__ = 'Sumin Byeon'
__email__ = 'suminb@gmail.com'
__version__ = '0.11.0'


# Copied from https://wiki.python.org/moin/PythonDecoratorLibrary
def deprecated(func):
    '''This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emitted
    when the function is used.'''
    def new_func(*args, **kwargs):
        warnings.warn("Call to deprecated function {}.".format(func.__name__),
                      category=DeprecationWarning)
        return func(*args, **kwargs)
    new_func.__name__ = func.__name__
    new_func.__doc__ = func.__doc__
    new_func.__dict__.update(func.__dict__)
    return new_func


def translate_syllable(previous, current):
    from hanja.pairs import table as hanja_table
    from hanja.hangul import dooeum
    if current in hanja_table:
        return dooeum(previous, hanja_table[current])

    return current


def split_hanja(text):
    """주어진 문장을 한자로 된 구역과 그 이외의 문자로 된 구역으로 분리"""

    # TODO: Can we make this a bit prettier?
    if len(text) == 0:
        yield text
    else:
        ch = text[0]
        bucket = [ch]
        prev_state = is_hanja(ch)

        for ch in text[1:]:
            state = is_hanja(ch)

            if prev_state != state:
                yield ''.join(bucket)
                bucket = [ch]
            else:
                bucket.append(ch)

            prev_state = state

        yield ''.join(bucket)


def translate(text, mode):
    words = list(split_hanja(text))
    return ''.join(map(lambda w, prev: translate_word(w, prev, mode),
                   words, [None] + words[:-1]))


def translate_word(word, prev, mode,
                   format='<span class="hanja">%s</span><span class="hangul">'
                          '(%s)</span>'):
    """
    :param mode: combination | substitution
    """
    prev_char = prev[-1] if prev else u' '
    translated = []
    for c in word:
        new_char = translate_syllable(prev_char, c)
        translated.append(new_char)
        prev_char = new_char
    tw = ''.join(translated)

    if mode == 'combination' and is_hanja(word[0]) == 1:
        return format % (word, tw)
    else:
        return tw


def is_hanja(ch):
    """Determines if a given character ``ch`` is a Chinese character."""
    from hanja.pairs import table as hanja_table
    return ch in hanja_table
