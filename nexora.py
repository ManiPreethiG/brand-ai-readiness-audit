#!/usr/bin/env python3
"""Root convenience proxy for Nexora AI.

Delegates execution to brand-ai-readiness-audit/nexora.py so commands work
whether run from workspace root or inside the repository directory.
"""

import os
import sys
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET = os.path.join(HERE, "brand-ai-readiness-audit", "nexora.py")

if not os.path.exists(TARGET):
    TARGET = os.path.join(HERE, "nexora.py")

if __name__ == "__main__":
    cmd = [sys.executable, TARGET] + sys.argv[1:]
    sys.exit(subprocess.run(cmd).returncode)
