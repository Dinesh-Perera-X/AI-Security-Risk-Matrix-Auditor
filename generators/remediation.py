from typing import Dict, Any, List

class RemediationGenerator:
    """
    Generates automated security remediation controls and hardening guidelines
    based on asset threat profiles and risk ratings.
    """

    REMEDIATION_DATABASE = {
        "AI Model Endpoint": [
            "Implement prompt injection guardrails (e.g., Llama Guard / NeMo Guardrails)",
            "Enforce strict rate limiting and output validation",
            "Enable API token rotation and zero-trust perimeter access"
        ],
        "Relational Database": [
            "Enable automated encryption at rest and in transit (TLS 1.3)",
            "Apply least-privilege IAM database roles and query parameterization",
            "Schedule continuous vulnerability scanning and audit logging"
        ],
        "Jupyter Server": [
            "Disable unauthenticated public access and enforce OAuth/SAML SSO",
            "Isolate interactive notebooks within ephemeral secure containers",
            "Remove unnecessary administrative tools from production VPCs"
        ]
    }

    @classmethod
    def generate_remediations(cls, asset: Dict[str, Any]) -> Dict[str, Any]:
        asset_type = asset.get("type", "Generic IT Asset")
        controls = cls.REMEDIATION_DATABASE.get(asset_type, [
            "Enforce multi-factor authentication (MFA) across all access points",
            "Conduct routine network exposure audits and patch management"
        ])

        remediated = dict(asset)
        remediated["remediation_steps"] = controls
        return remediated

    @classmethod
    def evaluate_remediations(cls, assets: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        return [cls.generate_remediations(asset) for asset in assets]
