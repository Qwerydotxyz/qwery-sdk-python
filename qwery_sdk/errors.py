"""Error types for Qwery SDK."""

class QweryError(Exception):
    """Base exception for Qwery SDK."""
    pass

class QweryAPIError(QweryError):
    """API returned an error."""
    def __init__(self, message: str, status_code: int = None):
        self.status_code = status_code
        super().__init__(message)

class QweryConfigError(QweryError):
    """Invalid configuration."""
    pass

class QwerySigningError(QweryError):
    """Transaction signing failed."""
    pass
