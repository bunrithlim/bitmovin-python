# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.bitmovin_response import BitmovinResponse
from bitmovin_python.models.response_envelope import ResponseEnvelope
from bitmovin_python.models.timecode_track_trimming_input_stream import TimecodeTrackTrimmingInputStream
from bitmovin_python.encoding.encodings.inputStreams.trimming.timecodeTrack.timecode_track_trimming_input_streams_list_query_params import TimecodeTrackTrimmingInputStreamsListQueryParams


class TimecodeTrackApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(TimecodeTrackApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def create(self, encoding_id, timecode_track_trimming_input_stream=None, **kwargs):
        """Add Timecode Track Trimming Input Stream"""

        return self.api_client.post(
            '/encoding/encodings/{encoding_id}/input-streams/trimming/timecode-track',
            timecode_track_trimming_input_stream,
            path_params={'encoding_id': encoding_id},
            type=TimecodeTrackTrimmingInputStream,
            **kwargs
        )

    def delete(self, encoding_id, input_stream_id, **kwargs):
        """Delete Timecode Track Trimming Input Stream"""

        return self.api_client.delete(
            '/encoding/encodings/{encoding_id}/input-streams/trimming/timecode-track/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=BitmovinResponse,
            **kwargs
        )

    def get(self, encoding_id, input_stream_id, **kwargs):
        """Timecode Track Trimming Input Stream Details"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/trimming/timecode-track/{input_stream_id}',
            path_params={'encoding_id': encoding_id, 'input_stream_id': input_stream_id},
            type=TimecodeTrackTrimmingInputStream,
            **kwargs
        )

    def list(self, encoding_id, query_params: TimecodeTrackTrimmingInputStreamsListQueryParams = None, **kwargs):
        """List Timecode Track Trimming Input Streams"""

        return self.api_client.get(
            '/encoding/encodings/{encoding_id}/input-streams/trimming/timecode-track',
            path_params={'encoding_id': encoding_id},
            query_params=query_params,
            pagination_response=True,
            type=TimecodeTrackTrimmingInputStream,
            **kwargs
        )