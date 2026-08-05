"""Fraud prediction inference module."""

from typing import Iterable, List


def predict(data: Iterable[Iterable[float]]) -> List[int]:
    """Return a fraud label (0 or 1) for each input feature row.

    This is a placeholder implementation that flags any transaction whose
    first feature value exceeds 100 as fraudulent. The real model loader
    is wired in elsewhere in the deployment pipeline.
    """
    return [1 if row[0] > 100 else 0 for row in data]
