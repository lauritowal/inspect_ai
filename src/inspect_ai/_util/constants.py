from pathlib import Path

PKG_AUTHOR = "UK AI Safety Institute"
PKG_AUTHOR_DIR = "UK-AISI"
PKG_NAME = Path(__file__).parent.parent.stem
PKG_PATH = Path(__file__).parent.parent
DEFAULT_EPOCHS = 1
DEFAULT_MAX_RETRIES = 5
DEFAULT_TIMEOUT = 120
DEFAULT_MAX_CONNECTIONS = 10
DEFAULT_MAX_TOKENS = 2048
DEFAULT_VIEW_PORT = 7575
DEFAULT_SERVER_HOST = "127.0.0.1"
HTTP = 15
HTTP_LOG_LEVEL = "HTTP"
SANDBOX = 17
SANDBOX_LOG_LEVEL = "SANDBOX"
ALL_LOG_LEVELS = [
    "DEBUG",
    HTTP_LOG_LEVEL,
    SANDBOX_LOG_LEVEL,
    "INFO",
    "WARNING",
    "ERROR",
]
DEFAULT_LOG_LEVEL = "warning"
DEFAULT_LOG_BUFFER_LOCAL = 10
DEFAULT_LOG_BUFFER_REMOTE = 100
SCORED_SUFFIX = "-scored"
SAMPLE_SUBTASK = "sample"
