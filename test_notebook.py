import pytest
from notebook import *
import numpy as np


def test_common_parameters():
    computed, expected = common_parameters()

    # Iterate over each variable in expected values and compare with computed ones
    for key in expected:
        expected_val = expected[key]['value']
        computed_val = computed[key]['value']
        atol = expected[key]['atol']
        if computed_val is None or not np.allclose(expected_val, computed_val, atol=atol):
            raise AssertionError(f"Mismatch in {key}. Your {key} value is different from the one expected.")


def test_signals():
    computed, expected = signals()

    # Iterate over each variable in expected values and compare with computed ones
    for key in expected:
        expected_val = expected[key]['value']
        computed_val = computed[key]['value']
        atol = expected[key]['atol']

        if computed_val is None or not np.allclose(expected_val, computed_val, atol=atol):
            raise AssertionError(f"Mismatch in {key}. Your {key} value is different from the one expected.")


def test_signals_second():
    computed, expected = signals_second()

    # Iterate over each variable in expected values and compare with computed ones
    for key in expected:
        print(key)
        expected_val = expected[key]['value']
        computed_val = computed[key]['value']
        atol = expected[key]['atol']

        if computed_val is None or not np.allclose(expected_val, computed_val, atol=atol):
            raise AssertionError(f"Mismatch in {key}. Your {key} value is different from the one expected.")

# This will run the test if the file is run directly
if __name__ == "__main__":
    pytest.main()
