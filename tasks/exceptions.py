import logging

from rest_framework.response import Response
from rest_framework.views import exception_handler

logger = logging.getLogger(__name__)


def api_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        response.data = {
            "error": {
                "status_code": response.status_code,
                "details": response.data,
            }
        }
        return response

    logger.error(
        "Unhandled API exception",
        exc_info=(type(exc), exc, exc.__traceback__),
    )

    return Response(
        {
            "error": {
                "status_code": 500,
                "details": {
                    "detail": "An unexpected server error occurred."
                },
            }
        },
        status=500,
    )
