# Copyright 2020 Canonical Ltd.
from types import ModuleType

# Note, `.main` import is required
from . import main as _main

class _CallableMainModule(ModuleType):
    def __call__(self):
        return 42

main = _CallableMainModule("ops.main", "some doc")

__all__ = ["main", "_main"]
