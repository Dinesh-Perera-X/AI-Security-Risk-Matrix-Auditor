from typing import Dict, Any, List

class ThreatModeler:
    """
    Maps organizational and AI assets to specific threat vectors and attack surfaces,
    including AI/LLM-specific risks.
    """

    THREAT_DATABASE = {
        "AI Model Endpoint": {
            "primary_threat": "Indirect Prompt Injection & Model Extraction",
            "owasp_mapping": "LLM01: Prompt Injection / LLM10: Model Theft",
            "likelihood": "HIGH"
        },
        "Relational Database": {
            "primary_threat": "SQL Injection & Unauthorized Data Exfiltration",
            "owasp_mapping": "A03:2021-Injection",
            "likelihood": "MEDIUM"
        },
        "Jupyter Server": {
            "primary_threat": "Unauthenticated RCE & Credential Harvesting",
            "owasp_mapping": "A05:2021-Security Misconfiguration",
            "likelihood": "CRITICAL"
        }
    }

    @classmethod
    def profile_asset_threats(cls, asset: Dict[str, Any]) -> Dict[str, Any]:
        asset_type = asset.get("type", "Generic IT Asset")
        threat_info = cls.THREAT_DATABASE.get(asset_type, {
            "primary_threat": "General Network Enumeration & Compromise",
            "owasp_mapping": "A04:2021-Insecure Design",
            "likelihood": "MEDIUM"
        })

        profiled = dict(asset)
        profiled.update(threat_info)
        return profiled

    @classmethod
    def evaluate_threats(cls, assets: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        return [cls.profile_asset_threats(asset) for asset in assets]
