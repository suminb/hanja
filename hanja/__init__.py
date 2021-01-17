# -*- coding:utf-8 -*-
"""두음법칙에 관련된 내용은
http://ko.wikipedia.org/wiki/%EB%91%90%EC%9D%8C_%EB%B2%95%EC%B9%99 를 참고.
"""

import warnings


__all__ = ["is_hanja", "is_valid_mode", "split_hanja", "translate"]
__author__ = "Sumin Byeon"
__email__ = "suminb@gmail.com"
__version__ = "0.13.3"


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


def lazily_import(import_string):
    import_path, func_name = import_string.split(":")

    def load_and_call(*args, **kwargs):
        mod = __import__(import_path)
        for mod_name in import_path.split(".")[1:]:
            mod = getattr(mod, mod_name)
        func = getattr(mod, func_name)
        globals()[func_name] = func
        return func(*args, **kwargs)

    globals()[func_name] = load_and_call


lazily_import("hanja.impl:is_hanja")
lazily_import("hanja.impl:is_valid_mode")
lazily_import("hanja.impl:split_hanja")
lazily_import("hanja.impl:translate")
