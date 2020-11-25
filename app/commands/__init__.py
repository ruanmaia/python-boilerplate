from cleo import Application

from app.commands.debug import DebugRoutesCommand
from app.commands.webserver import WebserverStartCommand
from app.commands.celery import CeleryStartCommand

cli = Application('ustore', 'v1.0.0')

cli.add(DebugRoutesCommand())
cli.add(WebserverStartCommand())
cli.add(CeleryStartCommand())