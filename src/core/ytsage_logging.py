"""
YTSage logging configuration using loguru.

This module provides centralized logging configuration for the entire YTSage application.
It replaces the inefficient print statements with structured logging using loguru.
"""

import os
import sys
from pathlib import Path
from loguru import logger


def setup_logging():
    """
    Configure loguru logging for YTSage application.
    
    Sets up multiple log levels and outputs:
    - Console output for INFO and above
    - File output for DEBUG and above  
    - Separate error log file for ERROR and above
    """
    
    # Remove default logger to avoid duplicate output
    logger.remove()
    
    # Get the application data directory
    if sys.platform == 'win32':
        log_dir = Path(os.environ.get('LOCALAPPDATA')) / 'YTSage' / 'logs'
    elif sys.platform == 'darwin':
        log_dir = Path.home() / 'Library' / 'Application Support' / 'YTSage' / 'logs'
    else:
        log_dir = Path.home() / '.local' / 'share' / 'YTSage' / 'logs'
    
    # Create log directory if it doesn't exist
    log_dir.mkdir(parents=True, exist_ok=True)
    
    # Console handler - INFO and above, with colors
    logger.add(
        sys.stdout,
        level="INFO",
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        colorize=True,
        catch=True
    )
    
    # Main log file - DEBUG and above, with rotation
    logger.add(
        log_dir / "ytsage.log",
        level="DEBUG", 
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
        rotation="10 MB",  # Rotate when file reaches 10MB
        retention="7 days",  # Keep logs for 7 days
        compression="zip",  # Compress old logs
        catch=True
    )
    
    # Error log file - ERROR and above only
    logger.add(
        log_dir / "ytsage_errors.log",
        level="ERROR",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
        rotation="5 MB",
        retention="30 days",  # Keep error logs longer
        compression="zip",
        catch=True
    )
    
    # Log startup message
    logger.info("YTSage logging system initialized")
    logger.debug(f"Log directory: {log_dir}")
    
    return logger


def get_logger(name: str = None):
    """
    Get a logger instance for a specific module.
    
    Args:
        name: Name of the module/component requesting the logger
        
    Returns:
        Configured logger instance
    """
    if name:
        return logger.bind(name=name)
    return logger


# Initialize logging when module is imported
setup_logging()

# Export the main logger for convenience
__all__ = ['logger', 'get_logger', 'setup_logging']
