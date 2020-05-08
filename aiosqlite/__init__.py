# Copyright 2018 John Reese
# Licensed under the MIT license

"""asyncio bridge to the standard sqlite3 module"""

from sqlite3 import (  # pylint: disable=redefined-builtin
    DatabaseError,
    Error,
    IntegrityError,
    NotSupportedError,
    OperationalError,
    ProgrammingError,
    Row,
    Warning,
    register_adapter,
    register_converter,
    sqlite_version,
    sqlite_version_info,
)

from .core import Connection, Cursor, connect
from .pool import create_pool, Pool

__version__ = "0.12.0"
__all__ = [
    "__version__",
    "create_pool",
    "register_adapter",
    "register_converter",
    "sqlite_version",
    "sqlite_version_info",
    "connect",
    "Connection",
    "Cursor",
    "Pool",
    "Row",
    "Warning",
    "Error",
    "DatabaseError",
    "IntegrityError",
    "ProgrammingError",
    "OperationalError",
    "NotSupportedError",
]
