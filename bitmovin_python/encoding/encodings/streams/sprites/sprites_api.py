# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.sprite import Sprite
from bitmovin_python.encoding.encodings.streams.sprites.customdata.customdata_api import CustomdataApi
from bitmovin_python.encoding.encodings.streams.sprites.sprites_list_query_params import SpritesListQueryParams


class SpritesApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(SpritesApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

        self.customdata = CustomdataApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def create(self, encoding_id, stream_id, sprite=None, **kwargs):
        """Add Sprite"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/sprites',
            sprite,
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            type=Sprite,
            **kwargs
        )

    def delete(self, encoding_id, stream_id, sprite_id, **kwargs):
        """Delete Sprite"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/sprites/{sprite_id}',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id, 'sprite_id': sprite_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, stream_id, sprite_id, **kwargs):
        """Sprite Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/sprites/{sprite_id}',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id, 'sprite_id': sprite_id},
            type=Sprite,
            **kwargs
        )

    def list(self, encoding_id, stream_id, query_params: SpritesListQueryParams = None, **kwargs):
        """List Sprites"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/sprites',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id},
            query_params=query_params,
            pagination_response=True,
            type=Sprite,
            **kwargs
        )