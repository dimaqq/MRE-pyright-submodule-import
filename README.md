# MRE pyright submodule import

- Positive test case: `ops/__init__.py` + `test_ops_use.py`
- Negative test case: `nops/__init__.py` + `test_nops_use.py`


`ops.main` is a callable module, see `ops/__init__.py`


```py
  def test_top_level_import():
      import ops

      assert ops.main() == 42


  def test_submodule_import():
      import ops.main

E     assert ops.main() == 42 # E: Module is not callable


  def test_function_import():
      from ops import main

      assert main() == 42
```

All three invocations styles work correctly at run time.

Pyright thinks differently, it gathers that `ops.main` is:
- a submodule if imported as `ops.main`
- a callable if `ops` is imported and `main` attribute is resolved

Pyright sees `sys.modules["ops.main"]()` while the runtime uses `sys.module["ops"].main()`.




Note that in the negative case (nops.main exists but is not imported by nops), pyright issues exact same 1 warning, even though 2 invocation alternatives fail at runtime.
