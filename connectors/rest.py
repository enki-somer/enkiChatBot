import logging
import json
from sanic import Blueprint, response
from sanic.request import Request
from sanic.response import HTTPResponse
from typing import Text, Dict, Any, Optional, Callable, Awaitable, List

from rasa.core.channels.channel import InputChannel, UserMessage, OutputChannel

logger = logging.getLogger(__name__)

class CustomRestInput(InputChannel):
    """A custom REST input channel that handles direct webhook requests."""

    @classmethod
    def name(cls) -> Text:
        return "custom_rest"

    def blueprint(
        self, on_new_message: Callable[[UserMessage], Awaitable[None]]
    ) -> Blueprint:
        custom_webhook = Blueprint(
            "custom_webhook_{}".format(type(self).__name__),
            __name__,
        )

        @custom_webhook.route("/", methods=["GET"])
        async def health(request: Request) -> HTTPResponse:
            return response.json({"status": "ok"})

        @custom_webhook.route("/webhook", methods=["POST"])
        async def receive(request: Request) -> HTTPResponse:
            try:
                payload = request.json
                sender_id = payload.get("sender", "default")
                message = payload.get("message", "")
                
                if not message:
                    return response.json(
                        {"status": "failed", "message": "No message provided"}
                    )
                
                await on_new_message(
                    UserMessage(
                        text=message,
                        output_channel=self.get_output_channel(),
                        sender_id=sender_id,
                        input_channel=self.name(),
                    )
                )
                
                return response.json({"status": "message received"})
            
            except Exception as e:
                logger.error(f"Exception when receiving message: {e}")
                return response.json(
                    {"status": "failed", "message": str(e)}, status=500
                )

        @custom_webhook.route("/webhook", methods=["GET"])
        async def webhook_info(request: Request) -> HTTPResponse:
            return response.json({
                "status": "ok",
                "channel": self.name(),
                "usage": "Send a POST request to /webhooks/custom_rest/webhook with the message in JSON format"
            })

        return custom_webhook

    def get_output_channel(self) -> OutputChannel:
        return CustomRestOutput()


class CustomRestOutput(OutputChannel):
    """Output channel for the custom REST connector."""

    @classmethod
    def name(cls) -> Text:
        return "custom_rest"

    async def send_text_message(
        self, recipient_id: Text, text: Text, **kwargs: Any
    ) -> None:
        """Send a message through this channel."""
        # Message sending happens automatically via the webhook response

    async def send_image_url(
        self, recipient_id: Text, image: Text, **kwargs: Any
    ) -> None:
        """Send an image through this channel."""
        pass

    async def send_text_with_buttons(
        self,
        recipient_id: Text,
        text: Text,
        buttons: List[Dict[Text, Any]],
        **kwargs: Any,
    ) -> None:
        """Send buttons to the output."""
        pass

    async def send_custom_json(
        self, recipient_id: Text, json_message: Dict[Text, Any], **kwargs: Any
    ) -> None:
        """Send custom json to the output."""
        pass 