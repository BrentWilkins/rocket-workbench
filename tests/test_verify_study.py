import hashlib
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from verify_study import verify


def test_artifact_verification_detects_changes(tmp_path):
    (tmp_path/'report.md').write_text('original')
    (tmp_path/'manifest.json').write_text(json.dumps(dict(artifact_sha256={
        'report.md':hashlib.sha256(b'original').hexdigest()})))
    assert verify(tmp_path)['verified_artifact_references']==1
    (tmp_path/'report.md').write_text('changed')
    with pytest.raises(ValueError,match='Artifact changed'):
        verify(tmp_path)


def test_unsealed_manifest_is_not_success(tmp_path):
    (tmp_path/'manifest.json').write_text('{}')
    with pytest.raises(ValueError,match='Unsealed'):
        verify(tmp_path)
