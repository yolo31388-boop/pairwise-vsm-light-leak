import pytest
import graphics.variance_shadow as mod

CASES = [
    ("moment_precision_comp", (1,)),
    ("mip_penumbra_kernel", (1,)),
    ("shadow_double_buffer_gen", (1,)),
    ("cascade_edge_weight", (1,)),
    ("transparent_mask_split", (1,)),
    ("shadow_page_clear", (1,)),
    ("load_shadow_vsm", (1,)),
    ("build_moments", (1,)),
    ("sample_shadow", (1,)),
    ("present_vsm", (1,)),
    ("validate_vsm", (1,)),
    ("metrics_vsm", (1,)),
    ("audit_vsm", (1,)),
    ("fallback_vsm", (1,)),
    ("determinism_vsm", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
