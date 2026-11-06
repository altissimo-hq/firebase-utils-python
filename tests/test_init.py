"""Tests for the altissimo.firebase_utils public API surface."""

from __future__ import annotations


class TestPublicAPI:
    """Verify that the public API is importable and consistent."""

    def test_version_exists(self) -> None:
        from altissimo.firebase_utils import __version__

        assert isinstance(__version__, str)
        assert len(__version__) > 0

    def test_all_is_accurate(self) -> None:
        import altissimo.firebase_utils as mod

        for name in mod.__all__:
            assert hasattr(mod, name), f"__all__ lists '{name}' but it is not defined"
