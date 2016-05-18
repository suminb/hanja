# -*- coding: utf8 -*-
from __future__ import absolute_import

import hanja
from hanja import hangul


def test_separation():
    assert hangul.separate(u'가') == (0, 0, 0)
    assert hangul.separate(u'까') == (1, 0, 0)
    assert hangul.separate(u'갸') == (0, 2, 0)
    assert hangul.separate(u'각') == (0, 0, 1)


def test_build():
    assert hangul.build(0, 0, 0) == u'가'


def test_is_hangul():
    assert hangul.is_hangul(u'한') == True
    assert hangul.is_hangul('A') == False
    assert hangul.is_hangul('1') == False
    assert hangul.is_hangul(None) == False


def test_contains_hangul():
    assert hangul.contains_hangul(u'한국어') == True
    assert hangul.contains_hangul(u'한ABC국어') == True
    assert hangul.contains_hangul(u"Yo, what's up bro?") == False
    assert hangul.contains_hangul(u'1234567890') == False


def test_is_hanja():
    assert hanja.is_hanja(u'한') == False
    assert hanja.is_hanja('A') == False
    assert hanja.is_hanja('1') == False
    assert hanja.is_hanja(None) == False
    assert hanja.is_hanja(u'韓') == True


def test_split_hanja():
    corpora = list(hanja.split_hanja(u'大韓民國은 民主共和國이다.'))
    assert len(corpora) == 4
    assert corpora[0] == u'大韓民國'
    assert corpora[1] == u'은 '
    assert corpora[2] == u'民主共和國'
    assert corpora[3] == u'이다.'


def test_translate():
    assert hanja.translate(u'韓國語', mode='substitution') == u'한국어'
    assert hanja.translate(u'한국어', mode='substitution') == u'한국어'
    assert hanja.translate(u'利用해', mode='substitution') == u'이용해'
    assert hanja.translate(u'連結된', mode='substitution') == u'연결된'
    assert hanja.translate(u'1800年에', mode='substitution') == u'1800년에'
    assert hanja.translate(u'그레고리曆', mode='substitution') == u'그레고리력'
    assert hanja.translate(u'系列', mode='substitution') == u'계열'
