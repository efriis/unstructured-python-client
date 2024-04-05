"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .general import General
from .sdkconfiguration import SDKConfiguration
from .utils.retries import RetryConfig
from typing import Callable, Dict, Optional, Union
from unstructured_client import utils
from unstructured_client._hooks import SDKHooks
from unstructured_client.models import shared

class UnstructuredClient:
    r"""Unstructured Pipeline API: Partition documents with the Unstructured library"""
    general: General

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 api_key_auth: Union[str, Callable[[], str]],
                 server: Optional[str] = None,
                 server_url: Optional[str] = None,
                 url_params: Optional[Dict[str, str]] = None,
                 client: Optional[requests_http.Session] = None,
                 retry_config: Optional[RetryConfig] = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.

        :param api_key_auth: The api_key_auth required for authentication
        :type api_key_auth: Union[str, Callable[[], str]]
        :param server: The server by name to use for all operations
        :type server: str
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: Dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session
        :param retry_config: The utils.RetryConfig to use globally
        :type retry_config: RetryConfig
        """
        if client is None:
            client = requests_http.Session()

        if callable(api_key_auth):
            def security():
                return shared.Security(api_key_auth = api_key_auth())
        else:
            security = shared.Security(api_key_auth = api_key_auth)

        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        self.sdk_configuration = SDKConfiguration(
            client,
            security,
            server_url,
            server,
            retry_config=retry_config
        )

        hooks = SDKHooks()

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(current_server_url, self.sdk_configuration.client)
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        # pylint: disable=protected-access
        self.sdk_configuration._hooks = hooks

        self._init_sdks()


    def _init_sdks(self):
        self.general = General(self.sdk_configuration)
