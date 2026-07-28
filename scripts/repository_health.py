#!/usr/bin/env python3
"""Backward-compatible repository-health entry point."""
import subprocess, sys
from pathlib import Path
raise SystemExit(subprocess.call([sys.executable,str(Path(__file__).with_name('repository_checks.py')),'health',*sys.argv[1:]]))
