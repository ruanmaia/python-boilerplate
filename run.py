import sys
import eventlet

eventlet.monkey_patch()

# Import application modules
from app import app

# Disable undesired logs if NOT in production environment

# import logging
# if not app.config['DEBUG']:
#     logging.getLogger('werkzeug').disable = True

# if app.config['DEBUG']:
#     logger = logging.getLogger('orator.connection.queries')
#     logger.setLevel(logging.DEBUG)

#     formatter = logging.Formatter(
#         '[ORM] It took %(elapsed_time)sms to execute the query %(query)s'
#     )

#     handler = logging.StreamHandler()
#     handler.setFormatter(formatter)

#     logger.addHandler(handler)

# CLI Command configuration
from app.commands import cli

# Executes the application
if __name__ == '__main__': cli.run()