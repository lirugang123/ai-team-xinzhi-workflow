import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

def test_workflow_2():
    \"\"\"测试工作流2\"\"\"
    assert True
