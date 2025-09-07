import logging
import functools
import time
import traceback

def log_function(logger, include_runtime=False):
    """
    Decorator to log function entry, exit, and exceptions.

    Parameters:
        logger (logging.Logger): Logger instance to use
        include_runtime (bool): Whether to log execution time

    Returns:
        function: Wrapped function with logging
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logger.info(f"Entering function: {func.__name__}")
            start_time = time.time()

            try:
                result = func(*args, **kwargs)
                if include_runtime:
                    duration = time.time() - start_time
                    logger.info(f"Function {func.__name__} completed in {duration:.2f} seconds")
                else:
                    logger.info(f"Exiting function:  {func.__name__}")
                return result
            except Exception as e:
                logger.error(f"[ERROR] Function '{func.__name__}' failed: {str(e)}")
                logger.debug(traceback.format_exc())
                raise
        return wrapper
    return decorator
                    

