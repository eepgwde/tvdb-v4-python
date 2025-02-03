## weaves
# From TVDB, this is their original pytest.
# I know it won't work unless there is a ./config.json.
# There is a directory in tests/home0 that has a config.
# 
# But it uses a mock and doesn't seem to run anything.

from unittest.mock import patch, MagicMock
import pytest
import json
import sys

import pdb

from tvdb_v5_unofficial import TVDB

VALID_API_KEY = "valid_api_key"
VALID_PIN = "valid_pin"


@pytest.fixture
def tvdb_instance():
    with patch("tvdb_v4_official.Auth") as MockAuth:
        MockAuth.return_value.get_token.return_value = "test_token"
        instance = TVDB(config_file="./config.json")
        return instance

@patch("urllib.request.urlopen")
def test_get_artwork(mocked_urlopen, tvdb_instance):
    mock_response_content = json.dumps(
        {"status": "success", "data": {"id": 123, "type": "Poster"}, "links": {}}
    ).encode("utf-8")

    print("message", file=sys.stderr)

    mock_response = MagicMock()
    mock_response.read.return_value = mock_response_content
    mock_response.__enter__.return_value = mock_response
    mocked_urlopen.return_value = mock_response

    artwork = tvdb_instance.get_artwork(123)
    assert artwork["id"] == 123
    assert artwork["type"] == "Poster"



# -*- coding: utf-8 -*-
# Local Variables:
# mode:python
# python-indent-offset: 2
# End:
