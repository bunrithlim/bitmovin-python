# coding: utf-8

from __future__ import absolute_import

from bitmovin_python.common import BaseApi
from bitmovin_python.common.poscheck import poscheck_except

from bitmovin_python.models.response_envelope import ResponseEnvelope


class AgentDeploymentApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key: str, tenant_org_id: str = None, base_url: str = None, debug: bool = False, logger=None,
                 *args, **kwargs):
        super(AgentDeploymentApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            debug=debug,
            logger=logger,
            *args,
            **kwargs
        )

    def get(self, infrastructure_id, **kwargs):
        """Download bitmovin-agent deployment"""

        self.api_client.get(
            '/encoding/infrastructure/kubernetes/{infrastructure_id}/agent-deployment',
            path_params={'infrastructure_id': infrastructure_id},
            **kwargs
        )