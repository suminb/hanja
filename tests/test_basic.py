# -*- coding: utf8 -*-
from __future__ import absolute_import

import pytest

import hanja
from hanja import hangul


def test_separation():
    assert hangul.separate(u"가") == (0, 0, 0)
    assert hangul.separate(u"까") == (1, 0, 0)
    assert hangul.separate(u"갸") == (0, 2, 0)
    assert hangul.separate(u"각") == (0, 0, 1)


def test_build():
    assert hangul.build(0, 0, 0) == u"가"


def test_is_hangul():
    assert hangul.is_hangul(u"한")
    assert not hangul.is_hangul("A")
    assert not hangul.is_hangul("1")
    assert not hangul.is_hangul(None)


def test_contains_hangul():
    assert hangul.contains_hangul(u"한국어")
    assert hangul.contains_hangul(u"한ABC국어")
    assert not hangul.contains_hangul(u"Yo, what's up bro?")
    assert not hangul.contains_hangul(u"1234567890")


def test_is_hanja():
    assert not hanja.is_hanja(u"한")
    assert not hanja.is_hanja("A")
    assert not hanja.is_hanja("1")
    assert not hanja.is_hanja(None)
    assert hanja.is_hanja(u"韓")


def test_split_hanja():
    corpora = list(hanja.split_hanja(u"大韓民國은 民主共和國이다."))
    assert len(corpora) == 4
    assert corpora[0] == u"大韓民國"
    assert corpora[1] == u"은 "
    assert corpora[2] == u"民主共和國"
    assert corpora[3] == u"이다."


def test_is_valid_mode():
    assert hanja.is_valid_mode("substitution")
    assert hanja.is_valid_mode("combination-text")
    assert hanja.is_valid_mode("combination-html")
    assert not hanja.is_valid_mode("combination-avro")


def test_translate_substitution_mode():
    mode = "substitution"
    assert hanja.translate(u"韓國語", mode=mode) == u"한국어"
    assert hanja.translate(u"한국어", mode=mode) == u"한국어"
    assert hanja.translate(u"利用해", mode=mode) == u"이용해"
    assert hanja.translate(u"連結된", mode=mode) == u"연결된"
    assert hanja.translate(u"1800年에", mode=mode) == u"1800년에"
    assert hanja.translate(u"그레고리曆", mode=mode) == u"그레고리력"
    assert hanja.translate(u"系列", mode=mode) == u"계열"


def test_translate_combination_text_mode():
    mode = "combination-text"
    assert hanja.translate(u"韓國語", mode=mode) == u"韓國語(한국어)"
    assert hanja.translate(u"利用해", mode=mode) == u"利用(이용)해"
    assert (
        hanja.translate(u"大韓民國은 民主共和國이다.", mode=mode) == u"大韓民國(대한민국)은 民主共和國(민주공화국)이다."
    )


@pytest.mark.parametrize("mode", ["combination-html", "combination"])
def test_translate_combination_html_mode(mode):
    assert (
        hanja.translate(u"韓國語", mode=mode)
        == u'<span class="hanja">韓國語</span><span class="hangul">(한국어)</span>'
    )
    assert (
        hanja.translate(u"利用해", mode=mode)
        == u'<span class="hanja">利用</span><span class="hangul">(이용)</span>해'
    )
    assert (
        hanja.translate(u"大韓民國은 民主共和國이다.", mode=mode)
        == u'<span class="hanja">大韓民國</span><span class="hangul">(대한민국)'
        u'</span>은 <span class="hanja">民主共和國</span><span class="hangul">'
        u"(민주공화국)</span>이다."
    )
