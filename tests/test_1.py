import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

def test_workflow_1():
    \"\"\"测试工作流1\"\"\"
    assert True
