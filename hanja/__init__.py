# -*- coding:utf-8 -*-
"""두음법칙에 관련된 내용은
http://ko.wikipedia.org/wiki/%EB%91%90%EC%9D%8C_%EB%B2%95%EC%B9%99 를 참고.
"""

import os
import warnings

import yaml


__author__ = "Sumin Byeon"
__email__ = "suminb@gmail.com"
__version__ = "0.12.3"


# Copied from https://wiki.python.org/moin/PythonDecoratorLibrary
def deprecated(func):
    """This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emitted
    when the function is used."""

    def new_func(*args, **kwargs):
        warnings.warn(
            "Call to deprecated function {}.".format(func.__name__),
            category=DeprecationWarning,
        )
        return func(*args, **kwargs)

    new_func.__name__ = func.__name__
    new_func.__doc__ = func.__doc__
    new_func.__dict__.update(func.__dict__)
    return new_func


def load_table(filename):
    """Loads the Hanja table."""
    try:
        from yaml import CLoader as Loader
    except ImportError:
        from yaml import BaseLoader as Loader
    with open(filename) as fin:
        table = yaml.load(fin.read(), Loader=Loader)

    return table


def translate_syllable(previous, current):
    """Translates a single syllable."""
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
                yield "".join(bucket)
                bucket = [ch]
            else:
                bucket.append(ch)

            prev_state = state

        yield "".join(bucket)


def get_format_string(mode, word):
    """
    :param mode: combination | substitution
    """
    if mode == "substitution":
        return "{translated}"
    elif mode == "combination":
        if is_hanja(word[0]):
            return '<span class="hanja">{word}</span><span class="hangul">({translated})</span>'
        else:
            return "{translated}"
    else:
        raise ValueError("Unsupported translation mode: " + mode)


def translate(text, mode):
    """Translates entire text."""
    words = list(split_hanja(text))
    return "".join(
        map(
            lambda w, prev: translate_word(w, prev, get_format_string(mode, w)),
            words,
            [None] + words[:-1],
        )
    )


def translate_word(word, prev, format_string):
    """Translates a single word.

    :param word: Word to be translated
    :param prev: Preceeding word
    """
    prev_char = prev[-1] if prev else u" "
    buf = []
    for c in word:
        new_char = translate_syllable(prev_char, c)
        buf.append(new_char)
        prev_char = new_char
    translated = "".join(buf)

    return format_string.format(word=word, translated=translated)


def is_hanja(ch):
    """Determines if a given character ``ch`` is a Chinese character."""
    return ch in hanja_table


basepath = os.path.abspath(os.path.dirname(__file__))
hanja_table = load_table(os.path.join(basepath, "table.yml"))
