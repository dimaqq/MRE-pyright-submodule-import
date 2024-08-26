# Copyright 2020 Canonical Ltd.
from types import ModuleType

from . import main as _main

# Support old and new style main calls at run time and for type checking
# - ops.main.main()
# - ops.main()
class _CallableMainModule(ModuleType):
    __call__ = main = staticmethod(_main.main)

main = _CallableMainModule('ops.main', _main.__doc__)

__all__ = ['main']
