# -*- coding: utf-8 -*-
"""5th June - full 10 carousel x 8 slide batch."""

from maker_loader import load_carousels

CAROUSELS = load_carousels()
CAROUSEL_MAP = {f"{i:02d}": CAROUSELS[i - 1] for i in range(1, len(CAROUSELS) + 1)}
