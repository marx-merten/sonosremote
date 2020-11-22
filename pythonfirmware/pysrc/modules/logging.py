import utime

LOG_NONE = const(0)
LOG_TRACE = const(1)
LOG_DEBUG = const(2)
LOG_WARN = const(3)
LOG_ERROR = const(4)
LOG_FATAL = const(5)

logger = {}
log_level = LOG_DEBUG


class Logger:
    def __init__(self, name: string):
        self.name = name
        logger[name] = self

    def active(self, level):
        return level >= log_level

    def is_debug(self):
        return self.active(LOG_DEBUG)

    def is_trace(self):
        return self.active(LOG_TRACE)

    def log(self, msg, level=LOG_DEBUG):
        if self.active(level):
            print(msg)
