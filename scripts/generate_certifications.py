#!/usr/bin/env python3
"""Generate docs/certifications.md from data/certifications.json"""

import json
import html
import sys
from pathlib import Path

ISSUER_SHORT_LABELS = {
    "Google Cloud": "GCP",
    "Amazon Web Services": "AWS",
    "Okta": "Okta",
    "HashiCorp": "HCP"
}

VALID_ISSUER_BADGE_CLASSES = {"google", "aws", "okta", "hashicorp"}

REQUIRED_CERT_KEYS = {"issuer", "title", "issued_month_year", "expires_date", "expires_full", "badge_url", "issuer_badge_class"}

def validate_url(url, cert_idx):
    """Validate that URL is a string and uses http or https scheme."""
    if not isinstance(url, str):
        raise ValueError(f"Certification #{cert_idx} has invalid badge_url: must be a string, got {type(url).__name__}")
    if not url.startswith(("http://", "https://")):
        raise ValueError(f"Certification #{cert_idx} has invalid badge_url: must use http or https, got {url}")

def validate_iso_date(date_str, cert_idx, field_name):
    """Validate that date is in ISO-8601 format (YYYY-MM-DD)."""
    if not isinstance(date_str, str):
        raise ValueError(f"Certification #{cert_idx} has invalid {field_name}: must be a string, got {type(date_str).__name__}")
    if not len(date_str) == 10 or date_str[4] != '-' or date_str[7] != '-':
        raise ValueError(f"Certification #{cert_idx} has invalid {field_name} format: expected YYYY-MM-DD, got {date_str}")
    try:
        int(date_str[:4])
        int(date_str[5:7])
        int(date_str[8:10])
    except ValueError:
        raise ValueError(f"Certification #{cert_idx} has invalid {field_name} format: dates must be numeric, got {date_str}")

def generate_certifications_page():
    # Read JSON data
    json_path = Path(__file__).parent.parent / "data" / "certifications.json"
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in {json_path}: {e}")
    except FileNotFoundError:
        raise ValueError(f"Certifications data file not found: {json_path}")

    # Group certifications by issuer (maintain order)
    issuers = {}
    for idx, cert in enumerate(data.get("certifications", [])):
        # Validate required keys
        missing_keys = REQUIRED_CERT_KEYS - set(cert.keys())
        if missing_keys:
            raise ValueError(f"Certification #{idx} missing required fields: {missing_keys}")

        # Validate URL scheme
        validate_url(cert["badge_url"], idx)

        # Validate date format
        validate_iso_date(cert["expires_date"], idx, "expires_date")

        # Validate issuer_badge_class against allowlist
        badge_class = cert["issuer_badge_class"]
        if badge_class not in VALID_ISSUER_BADGE_CLASSES:
            raise ValueError(f"Certification #{idx} has invalid issuer_badge_class '{badge_class}'. Must be one of: {', '.join(sorted(VALID_ISSUER_BADGE_CLASSES))}")

        issuer = cert["issuer"]
        if issuer not in issuers:
            issuers[issuer] = []
        issuers[issuer].append(cert)

    # Build markdown content
    content = "<!-- This file is auto-generated from data/certifications.json. Do not edit directly. -->\n\n"
    content += "# Certifications\n\n"
    content += "A collection of certifications reflecting continuous learning across cloud platforms, identity management, and infrastructure technologies.\n\n"

    for issuer, certs in issuers.items():
        escaped_issuer = html.escape(issuer, quote=True)
        short_label = ISSUER_SHORT_LABELS.get(issuer, issuer)
        escaped_short_label = html.escape(short_label, quote=True)

        content += f"## {escaped_issuer}\n\n"
        content += '<div class="certs-grid">\n'

        for cert in certs:
            # HTML-escape all user-controlled values
            escaped_badge_url = html.escape(cert["badge_url"], quote=True)
            escaped_title = html.escape(cert["title"], quote=True)
            escaped_expires = html.escape(cert["expires_date"], quote=True)
            escaped_class = html.escape(cert["issuer_badge_class"], quote=True)
            escaped_issued = html.escape(cert["issued_month_year"], quote=True)
            escaped_expires_full = html.escape(cert["expires_full"], quote=True)

            content += f'  <a href="{escaped_badge_url}" class="cert-card" data-expires="{escaped_expires}" target="_blank" rel="noopener noreferrer">\n'
            content += f'    <span class="issuer-badge issuer-compact {escaped_class}" title="{escaped_issuer}" aria-label="{escaped_issuer}">{escaped_short_label}</span>\n'
            content += f'    <h3>{escaped_title}</h3>\n'
            content += f'    <span class="cert-date">Issued: {escaped_issued} | Expires: {escaped_expires_full}</span>\n'
            content += "  </a>\n\n"

        content += "</div>\n\n"

    content += "---\n\n"
    content += "*View all certifications on [Credly](https://www.credly.com/users/smatoto/badges)*\n"

    return content

if __name__ == "__main__":
    try:
        content = generate_certifications_page()

        # Ensure output directory exists
        cert_path = Path(__file__).parent.parent / "docs" / "certifications.md"
        cert_path.parent.mkdir(parents=True, exist_ok=True)

        # Write to certifications.md
        with open(cert_path, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)

        print(f"Generated {cert_path}")
    except (ValueError, KeyError, TypeError, OSError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
