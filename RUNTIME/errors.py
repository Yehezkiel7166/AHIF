"""Runtime failure types."""


class RuntimeContractError(ValueError):
    """A caller supplied an input that cannot enter the AHIF pipeline."""
