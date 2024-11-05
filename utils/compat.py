try:
    # Flask Version 2.1.0
    # safe_join is removed, use werkzeug.utils.safe_join instead
    from flask import safe_join
except ImportError:
    # werkzeug Version 0.7
    # Added werkzeug.security.safe_join().
    from werkzeug.security import safe_join

try:
    # @since Python 3.10
    from collections.abc import Iterator
except ImportError:
    from collections import Iterator
