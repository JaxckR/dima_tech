class ApplicationError(Exception):
    """Базовое исключение слоя application"""


class AccessError(ApplicationError):
    """Ошибка доступа"""


class NotFoundError(ApplicationError):
    """Ошибка если данные не найдены"""


class AlreadyExists(ApplicationError):
    """Сущность уже существует"""
