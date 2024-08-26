# Copyright 2020 Canonical Ltd.
from types import ModuleType


class _CallableMainModule(ModuleType):
    def __call__(self):
        return 42

main = _CallableMainModule("ops.main", "some doc")

__all__ = ["main"]
