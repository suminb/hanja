# -*- coding: utf8 -*-
from __future__ import absolute_import

import pytest

import hanja
from hanja import hangul


def test_separation():
    assert hangul.separate("가") == (0, 0, 0)
    assert hangul.separate("까") == (1, 0, 0)
    assert hangul.separate("갸") == (0, 2, 0)
    assert hangul.separate("각") == (0, 0, 1)


def test_build():
    assert hangul.build(0, 0, 0) == "가"


def test_is_hangul():
    assert hangul.is_hangul("한")
    assert not hangul.is_hangul("A")
    assert not hangul.is_hangul("1")
    assert not hangul.is_hangul(None)


def test_contains_hangul():
    assert hangul.contains_hangul("한국어")
    assert hangul.contains_hangul("한ABC국어")
    assert not hangul.contains_hangul("Yo, what's up bro?")
    assert not hangul.contains_hangul("1234567890")


def test_is_hanja():
    assert not hanja.is_hanja("한")
    assert not hanja.is_hanja("A")
    assert not hanja.is_hanja("1")
    assert not hanja.is_hanja(None)
    assert hanja.is_hanja("韓")


def test_split_hanja():
    corpora = list(hanja.split_hanja("大韓民國은 民主共和國이다."))
    assert len(corpora) == 4
    assert corpora[0] == "大韓民國"
    assert corpora[1] == "은 "
    assert corpora[2] == "民主共和國"
    assert corpora[3] == "이다."


def test_is_valid_mode():
    assert hanja.is_valid_mode("substitution")
    assert hanja.is_valid_mode("combination-text")
    assert hanja.is_valid_mode("combination-html")
    assert not hanja.is_valid_mode("combination-avro")


def test_translate_substitution_mode():
    mode = "substitution"
    assert hanja.translate("韓國語", mode=mode) == "한국어"
    assert hanja.translate("한국어", mode=mode) == "한국어"
    assert hanja.translate("利用해", mode=mode) == "이용해"
    assert hanja.translate("連結된", mode=mode) == "연결된"
    assert hanja.translate("1800年에", mode=mode) == "1800년에"
    assert hanja.translate("그레고리曆", mode=mode) == "그레고리력"
    assert hanja.translate("系列", mode=mode) == "계열"


def test_translate_combination_text_mode():
    mode = "combination-text"
    assert hanja.translate("韓國語", mode=mode) == "韓國語(한국어)"
    assert hanja.translate("利用해", mode=mode) == "利用(이용)해"
    assert (
        hanja.translate("大韓民國은 民主共和國이다.", mode=mode)
        == "大韓民國(대한민국)은 民主共和國(민주공화국)이다."
    )


@pytest.mark.parametrize("mode", ["combination-html", "combination"])
def test_translate_combination_html_mode(mode):
    assert (
        hanja.translate("韓國語", mode=mode)
        == '<span class="hanja">韓國語</span><span class="hangul">(한국어)</span>'
    )
    assert (
        hanja.translate("利用해", mode=mode)
        == '<span class="hanja">利用</span><span class="hangul">(이용)</span>해'
    )
    assert (
        hanja.translate("大韓民國은 民主共和國이다.", mode=mode)
        == '<span class="hanja">大韓民國</span><span class="hangul">(대한민국)'
        '</span>은 <span class="hanja">民主共和國</span><span class="hangul">'
        "(민주공화국)</span>이다."
    )


def test_translate_with_invalid_mode():
    with pytest.raises(ValueError):
        hanja.translate("Some text", mode="invalid")
