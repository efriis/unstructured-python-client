"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""


import requests as requests_http
from ._hooks import SDKHooks
from .utils import utils
from .utils.retries import RetryConfig
from dataclasses import dataclass
from typing import Callable, Dict, Optional, Tuple, Union
from unstructured_client.models import shared


SERVER_FREE_API = 'free-api'
r"""Hosted API Free"""
SERVER_DEVELOPMENT = 'development'
r"""Development server"""
SERVERS = {
	SERVER_FREE_API: 'https://api.unstructured.io',
	SERVER_DEVELOPMENT: 'http://localhost:8000',
}
"""Contains the list of servers available to the SDK"""


@dataclass
class SDKConfiguration:
    client: requests_http.Session
    security: Union[shared.Security,Callable[[], shared.Security]] = None
    server_url: Optional[str] = ''
    server: Optional[str] = ''
    language: str = 'python'
    openapi_doc_version: str = '1.0.33'
    sdk_version: str = '0.23.2'
    gen_version: str = '2.339.1'
    user_agent: str = 'speakeasy-sdk/python 0.23.2 2.339.1 1.0.33 unstructured-client'
    retry_config: Optional[RetryConfig] = None

    def __post_init__(self):
        self._hooks = SDKHooks()

    def get_server_details(self) -> Tuple[str, Dict[str, str]]:
        if self.server_url is not None and self.server_url != '':
            return utils.remove_suffix(self.server_url, '/'), {}
        if not self.server:
            self.server = SERVER_FREE_API

        if self.server not in SERVERS:
            raise ValueError(f"Invalid server \"{self.server}\"")

        return SERVERS[self.server], {}


    def get_hooks(self) -> SDKHooks:
        return self._hooks
