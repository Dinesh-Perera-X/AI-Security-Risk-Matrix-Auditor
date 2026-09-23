import json
import os
from typing import List, Dict, Any

class Reporter:
    """
    Generates SIEM-compatible JSON export logs and executive HTML risk dashboards
    for organizational and AI asset audits.
    """

    @classmethod
    def export_siem_json(cls, assets: List[Dict[str, Any]], filepath: str = "reports/siem_audit_export.json") -> str:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        siem_payload = {
            "audit_standard": "AI-Security-Risk-Matrix-Auditor v1.0",
            "total_assets_audited": len(assets),
            "assets": assets
        }
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(siem_payload, f, indent=4)
        return filepath

    @classmethod
    def export_html_dashboard(cls, assets: List[Dict[str, Any]], filepath: str = "reports/executive_risk_dashboard.html") -> str:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        rows_html = ""
        for a in assets:
            score = a.get("risk_score", 0)
            rating = a.get("risk_rating", "LOW")
            badge_color = "#28a745" if rating == "LOW" else "#ffc107" if rating == "MEDIUM" else "#fd7e14" if rating == "HIGH" else "#dc3545"
            
            remediations = "".join([f"<li>{r}</li>" for r in a.get("remediation_steps", [])])
            
            rows_html += f"""
            <tr>
                <td><code>{a.get('asset_id')}</code></td>
                <td><strong>{a.get('name')}</strong><br><small>{a.get('type')}</small></td>
                <td>{a.get('exposure')}</td>
                <td><span style="background-color: {badge_color}; color: white; padding: 4px 8px; border-radius: 4px; font-weight: bold;">{rating} ({score}/100)</span></td>
                <td><strong>{a.get('primary_threat')}</strong><br><em>{a.get('owasp_mapping')}</em></td>
                <td><ul>{remediations}</ul></td>
            </tr>
            """

        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>AI & IT Executive Risk Matrix Dashboard</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; margin: 40px; background: #f8f9fa; color: #333; }}
        h1 {{ color: #0066cc; }}
        .card {{ background: white; padding: 24px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }}
        table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
        th, td {{ padding: 12px; border-bottom: 1px solid #dee2e6; text-align: left; vertical-align: top; }}
        th {{ background: #0066cc; color: white; }}
        ul {{ margin: 0; padding-left: 20px; }}
    </style>
</head>
<body>
    <div class="card">
        <h1>🛡️ AI-Security-Risk-Matrix-Auditor</h1>
        <p>Executive Risk Assessment Report & Hardening Dashboard</p>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Asset Name</th>
                    <th>Exposure</th>
                    <th>Risk Rating</th>
                    <th>Threat Model</th>
                    <th>Hardening Controls</th>
                </tr>
            </thead>
            <tbody>
                {rows_html}
            </tbody>
        </table>
    </div>
</body>
</html>
"""
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html_content)
        return filepath
