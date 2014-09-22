# -*- coding: utf8 -*-
import pytest
from hanja import hangul, hanja


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
