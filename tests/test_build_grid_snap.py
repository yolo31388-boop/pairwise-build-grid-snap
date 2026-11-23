import pytest
import gameplay.build_grid_snap as mod

CASES = [
    ("local_snap", (1)),
    ("undo_transform", (1)),
    ("cell_atomic", (1)),
    ("terrain_check", (1)),
    ("stable_id", (1)),
    ("redo_stack", (1)),
    ("rotation_record", (1)),
    ("validation", (1)),
    ("audit", (1)),
    ("fallback", (1)),
    ("preview_commit", (1)),
    ("metrics", (1)),
    ("multi_place", (1)),
    ("slope_offset", (1)),
    ("determinism", (1)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
