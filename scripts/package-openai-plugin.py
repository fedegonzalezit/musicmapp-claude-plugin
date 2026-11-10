"""Build the OpenAI submission ZIP using Python 3 standard library."""
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "musicmapp"
OUTPUT = ROOT / "dist" / "musicmapp-openai-plugin.zip"

def main():
    manifest = json.loads((PLUGIN / "plugin.json").read_text(encoding="utf-8"))
    interface = manifest["extensions"]["com.openai"]["interface"]
    review = manifest["extensions"]["com.openai"]["review"]
    for key, limit in (("displayName", 30), ("shortDescription", 30), ("developerName", 80), ("longDescription", 4000)):
        value = interface[key]
        if not isinstance(value, str) or not value.strip() or len(value) > limit:
            raise ValueError(f"Invalid {key}")
    for key in ("websiteURL", "supportURL", "privacyPolicyURL", "termsOfServiceURL"):
        if not interface[key].startswith("https://"):
            raise ValueError(f"Invalid {key}")
    if len(review["test_cases"]["positive"]) != 5 or len(review["test_cases"]["negative"]) != 3:
        raise ValueError("Expected five positive and three negative review cases")
    names = ["plugin.json", "mcp.json", "assets/logo.svg"]
    for key in ("logo", "composerIcon"):
        if interface[key] != "./assets/logo.svg":
            raise ValueError(f"Unexpected {key} path; update the packaging allowlist")
    for name in names:
        if not (PLUGIN / name).is_file():
            raise ValueError(f"Missing {name}")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(OUTPUT, "w", zipfile.ZIP_DEFLATED) as archive:
        for name in names:
            info = zipfile.ZipInfo(name, (2026, 11, 10, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, (PLUGIN / name).read_bytes())
    print(OUTPUT)
    if not review.get("demo_recording_url"):
        print("Draft package: still needs a real demo recording URL before submission.")

if __name__ == "__main__":
    main()
