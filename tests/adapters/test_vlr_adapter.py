import json
from unittest.mock import patch

import pytest
from httpx import Response

from vleague_backend.adapters.vlr_adapter import VLRAdapter
from vleague_backend.clients.http_client import HTTPClient
from vleague_backend.models.vlr_gg_api import DetailedPlayerStats


def construct_response(content: str) -> Response:
    return Response(status_code=200, content=content)


class TestVLRAdapter:
    @pytest.fixture()
    def adapter(self) -> VLRAdapter:
        return VLRAdapter()

    def test_adapter_initialization(self, adapter: VLRAdapter):
        assert adapter._client is not None
        assert isinstance(adapter._client, HTTPClient)

    def test_get_health_status(self, adapter: VLRAdapter):
        expected_response = '{"foo": "bar"}'

        with patch.object(adapter, "_client") as mock_client:
            mock_client.send_request.return_value = construct_response(
                expected_response
            )
            actual_response = json.dumps(adapter.get_health())
            assert actual_response == expected_response

    def test_get_player(self, adapter: VLRAdapter):
        expected_response = DetailedPlayerStats(data=None).model_dump_json()

        with patch.object(adapter, "_client") as mock_client:
            mock_client.send_request.return_value = construct_response(
                expected_response
            )
            actual_response = json.dumps(adapter.get_health())
            assert actual_response == expected_response
