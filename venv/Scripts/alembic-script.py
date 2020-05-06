#!"c:\users\john\desktop\python specialist path\udacity\full stack nano degree\part 1 sql & data modeling\exercises\todoappvenv\venv\scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'alembic==1.4.2','console_scripts','alembic'
__requires__ = 'alembic==1.4.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('alembic==1.4.2', 'console_scripts', 'alembic')()
    )
