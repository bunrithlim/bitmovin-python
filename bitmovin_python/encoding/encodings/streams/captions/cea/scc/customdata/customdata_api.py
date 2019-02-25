# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.custom_data import CustomData
from bitmovin_python.models.response_envelope import ResponseEnvelope


class CustomdataApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(CustomdataApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def getCustomData(self, encoding_id, stream_id, captions_id, **kwargs):
        """Embed SCC captions as 608/708 Custom Data"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/streams/{stream_id}/captions/608-708/scc/{captions_id}/customData',
            path_params={'encoding_id': encoding_id, 'stream_id': stream_id, 'captions_id': captions_id},
            type=CustomData,
            **kwargs
        )