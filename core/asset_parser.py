import json
import os
from typing import List, Dict, Any

class AssetParser:
    """
    Ingests organizational IT and AI asset inventories for risk scoring
    and CIA triad security evaluation.
    """

    DEFAULT_INVENTORY_PATH = "data/asset_inventory.json"

    @classmethod
    def load_inventory(cls, filepath: str = DEFAULT_INVENTORY_PATH) -> List[Dict[str, Any]]:
        if not os.path.exists(filepath):
            return []
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get("assets", [])
        except Exception:
            return []
