class AppException(Exception):
    def __init__(self, message: str, status_code: int = 500, details: str = None):
        self.message = message
        self.status_code = status_code
        self.details = details
        super().__init__(self.message)


class AuthenticationException(AppException):
    def __init__(self, message: str = "Authentication failed", details: str = None):
        super().__init__(message, status_code=401, details=details)


class AuthorizationException(AppException):
    def __init__(self, message: str = "Access denied", details: str = None):
        super().__init__(message, status_code=403, details=details)


class ValidationException(AppException):
    def __init__(self, message: str = "Validation failed", details: str = None):
        super().__init__(message, status_code=400, details=details)


class NotFoundException(AppException):
    def __init__(self, message: str = "Resource not found", details: str = None):
        super().__init__(message, status_code=404, details=details)


class ConflictException(AppException):
    def __init__(self, message: str = "Resource conflict", details: str = None):
        super().__init__(message, status_code=409, details=details)


class DatabaseException(AppException):
    def __init__(self, message: str = "Database operation failed", details: str = None):
        super().__init__(message, status_code=500, details=details)


class ExternalServiceException(AppException):
    def __init__(self, message: str = "External service error", details: str = None):
        super().__init__(message, status_code=502, details=details)


class RateLimitException(AppException):
    def __init__(self, message: str = "Rate limit exceeded", details: str = None):
        super().__init__(message, status_code=429, details=details)


class ConfigurationException(AppException):
    def __init__(self, message: str = "Configuration error", details: str = None):
        super().__init__(message, status_code=500, details=details)