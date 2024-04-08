# Brute force with a try-except block (Python 3+)
try: 
    with open('/path/to/file', 'r') as fh:
        pass
except FileNotFoundError: 
    pass

# Leverage the OS package (possible race condition)
import os 
exists = os.path.isfile('/path/to/file')

# Wrap the path in an object for enhanced functionality
from pathlib import Path

config = Path('/path/to/file') 
if config.is_file(): 
    pass