from typing import reveal_type


def test_top_level_import():
    import nops

    reveal_type(nops.main)
    assert nops.main() == 42


def test_submodule_import():
    import nops.main

    reveal_type(nops.main)
    assert nops.main() == 42


def test_function_import():
    from nops import main

    reveal_type(main)
    assert main() == 42
