## weaves
# From TVDB, this is their original pytest.
# I know it won't work unless there is a ./config.json.
# There is a directory in tests/home0 that has a config.
# 
# But it uses a mock and doesn't seem to run anything.

import sys
import os
import json
import pytest

from unittest.mock import patch, MagicMock

import pdb

from tvdb_v5_unofficial import TVDB, Config

VALID_API_KEY = "valid_api_key"
VALID_PIN = "valid_pin"


@pytest.fixture
def tvdb_instance():
    with patch("tvdb_v4_official.Auth") as MockAuth:
        MockAuth.return_value.get_token.return_value = "test_token"

        # How to initialize for netrc
        os.environ["TVDB_MACHINE"]="api4.thetvdb.com"
        v0 = Config.handler(env1="TVDB_MACHINE")

        instance = TVDB(config_file=v0)
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
