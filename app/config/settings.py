
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2]
CFG=ROOT/'data'/'config.json'
DEFAULT={'output_dir':str(ROOT/'output')}
def load():
    CFG.parent.mkdir(exist_ok=True)
    if not CFG.exists():
        CFG.write_text(json.dumps(DEFAULT,indent=2),encoding='utf-8')
    return json.loads(CFG.read_text(encoding='utf-8'))
