from typing import Dict, Any, List

class RiskCalculator:
    """
    Computes quantitative risk scores (0-100) based on CIA triad requirements
    and asset network exposure vectors.
    """

    CIA_WEIGHTS = {
        "LOW": 1,
        "MEDIUM": 2,
        "HIGH": 3,
        "CRITICAL": 4
    }

    EXPOSURE_MULTIPLIERS = {
        "INTERNAL_VPC": 1.0,
        "PARTNER_NETWORK": 1.2,
        "PUBLIC_INTERNET": 1.5
    }

    @classmethod
    def calculate_asset_risk(cls, asset: Dict[str, Any]) -> Dict[str, Any]:
        c_score = cls.CIA_WEIGHTS.get(asset.get("confidentiality_req", "LOW"), 1)
        i_score = cls.CIA_WEIGHTS.get(asset.get("integrity_req", "LOW"), 1)
        a_score = cls.CIA_WEIGHTS.get(asset.get("availability_req", "LOW"), 1)
        
        base_sum = c_score + i_score + a_score
        exposure = asset.get("exposure", "INTERNAL_VPC")
        multiplier = cls.EXPOSURE_MULTIPLIERS.get(exposure, 1.0)

        raw_score = (base_sum * multiplier) / 18.0 * 100.0
        final_score = round(min(100.0, raw_score), 1)

        if final_score >= 75.0:
            rating = "CRITICAL"
        elif final_score >= 50.0:
            rating = "HIGH"
        elif final_score >= 25.0:
            rating = "MEDIUM"
        else:
            rating = "LOW"

        scored_asset = dict(asset)
        scored_asset.update({
            "risk_score": final_score,
            "risk_rating": rating
        })
        return scored_asset

    @classmethod
    def evaluate_inventory(cls, assets: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        return [cls.calculate_asset_risk(asset) for asset in assets]
