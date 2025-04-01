import logging
import json
import asyncio
from sanic import Sanic, Blueprint, response
from sanic.request import Request
from sanic.response import HTTPResponse
from typing import Text, Dict, Any, Optional, Callable, Awaitable, NoReturn, List

from rasa.core.channels.channel import InputChannel, UserMessage, OutputChannel
from rasa.core.channels.rest import RestInput

logger = logging.getLogger(__name__)

class CustomRestInput(RestInput):
    """A custom REST input channel with CORS support for testing."""

    @classmethod
    def name(cls) -> Text:
        return "rest"

    def blueprint(
        self, on_new_message: Callable[[UserMessage], Awaitable[None]]
    ) -> Blueprint:
        custom_webhook = Blueprint("custom_webhook", __name__)
        
        @custom_webhook.route("/", methods=["GET"])
        async def health(_: Request) -> HTTPResponse:
            return response.json({"status": "ok"})
        
        @custom_webhook.route("/webhook", methods=["POST"])
        async def receive(request: Request) -> HTTPResponse:
            sender_id = request.json.get("sender", "default")
            text = request.json.get("message", "")
            message = UserMessage(
                text, self.output_channel, sender_id, input_channel=self.name()
            )
            await on_new_message(message)
            return response.json({"status": "message received"})
            
        @custom_webhook.route("/webhook", methods=["GET"])
        async def health(_: Request) -> HTTPResponse:
            return response.json({"status": "ok"})
            
        return custom_webhook 