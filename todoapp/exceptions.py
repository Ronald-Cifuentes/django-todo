import logging
import traceback

from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):
    """Custom exception handler to match Node.js API format."""
    response = exception_handler(exc, context)
    
    if response is not None:
        custom_response = {
            'error': {
                'code': response.status_text.upper().replace(' ', '_'),
                'message': str(exc.detail) if hasattr(exc, 'detail') else 'An error occurred',
                'details': exc.detail if isinstance(exc.detail, dict) else None,
            }
        }
        return Response(custom_response, status=response.status_code)
    
    # Log unexpected errors (visible in Render logs)
    logger.exception("Unhandled exception in API: %s", exc)
    traceback.print_exc()
    
    # Handle unexpected errors
    return Response({
        'error': {
            'code': 'INTERNAL_ERROR',
            'message': 'An unexpected error occurred',
        }
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
