from typing import List
from bitmovin.utils import Serializable
from bitmovin.resources.enums import LiveEncodingMode
from bitmovin.errors import InvalidTypeError
from .live_dash_manifest import LiveDashManifest
from .live_hls_manifest import LiveHlsManifest
from .auto_restart_configuration import AutoRestartConfiguration


class LiveStreamConfiguration(Serializable):
    def __init__(self,
                 stream_key: str,
                 live_dash_manifests: List[LiveDashManifest] = None,
                 live_hls_manifests: List[LiveHlsManifest] = None,
                 live_encoding_mode=None,
                 auto_restart_configuration: AutoRestartConfiguration=None):
        super().__init__()
        self.streamKey = stream_key
        self.dashManifests = live_dash_manifests
        self.hlsManifests = live_hls_manifests
        self._live_encoding_mode = None
        self.liveEncodingMode = live_encoding_mode
        self.autoRestartConfiguration = auto_restart_configuration

    @property
    def liveEncodingMode(self):
        return self._live_encoding_mode

    @liveEncodingMode.setter
    def liveEncodingMode(self, new_encoding_mode):
        if new_encoding_mode is None:
            self._live_encoding_mode = None
        elif isinstance(new_encoding_mode, str):
            self._live_encoding_mode = new_encoding_mode
        elif isinstance(new_encoding_mode, LiveEncodingMode):
            self._live_encoding_mode = new_encoding_mode.value
        else:
            raise InvalidTypeError(
                'Invalid type {} for liveEncodingMode: must be either str or LiveEncodingMode!'.format(
                    type(new_encoding_mode)))

    def serialize(self):
        serialized = super().serialize()
        serialized['liveEncodingMode'] = self.liveEncodingMode
        return serialized
