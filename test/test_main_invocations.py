from typing import reveal_type


def test_top_level_import():
    import ops

    reveal_type(ops.main)
    assert ops.main() == 42


def test_submodule_import():
    import ops.main

    reveal_type(ops.main)
    assert ops.main() == 42


def test_function_import():
    from ops import main

    reveal_type(main)
    assert main() == 42
