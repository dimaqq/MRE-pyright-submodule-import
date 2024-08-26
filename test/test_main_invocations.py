from typing import reveal_type

from ops import CharmBase


def test_top_level_import():
    import ops

    reveal_type(ops.main)
    ops.main(CharmBase)


def test_submodule_import():
    import ops.main

    reveal_type(ops.main)
    ops.main(CharmBase)


def test_function_import():
    from ops import main

    reveal_type(main)
    main(CharmBase)
