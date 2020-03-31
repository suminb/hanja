# -*- coding:utf-8 -*-

import warnings

from hanja.table import hanja_table


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


def is_valid_mode(mode):
    if mode in ("substitution", "combination-text", "combination-html"):
        return True
    elif mode == "combination":
        warnings.warn(
            "Translation mode 'combination' has been deprecated since 0.13.0. "
            "Use 'combination-html' instead."
        )
        return True
    else:
        return False


def get_format_string(mode, word):
    """
    :param mode: substitution | combination-text | combination-html
    """
    if not is_valid_mode(mode):
        raise ValueError("Unsupported translation mode: " + mode)

    if mode == "combination-text" and is_hanja(word[0]):
        return u"{word}({translated})"
    elif mode in ("combination-html", "combination") and is_hanja(word[0]):
        return u'<span class="hanja">{word}</span><span class="hangul">({translated})</span>'
    else:
        return u"{translated}"


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
