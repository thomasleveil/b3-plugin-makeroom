# -*- encoding: utf-8 -*-
import logging
from mock import Mock
from mockito import when
import pytest
from b3 import TEAM_UNKNOWN
from b3.config import XmlConfigParser, CfgConfigParser
from b3.plugins.admin import AdminPlugin
from b3.update import B3version
from makeroom import MakeroomPlugin
from b3 import __version__ as b3_version

class logging_disabled(object):
    """
    context manager that temporarily disable logging.

    USAGE:
        with logging_disabled():
            # do stuff
    """
    DISABLED = False

    def __init__(self):
        self.nested = logging_disabled.DISABLED

    def __enter__(self):
        if not self.nested:
            logging.getLogger('output').propagate = False
            logging_disabled.DISABLED = True

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self.nested:
            logging.getLogger('output').propagate = True
            logging_disabled.DISABLED = False


@pytest.fixture
def console():
    with logging_disabled():
        from b3.fake import FakeConsole
        console = FakeConsole('@b3/conf/b3.distribution.xml')

    # load the admin plugin
    if B3version(b3_version) >= B3version("1.10dev"):
        admin_plugin_conf_file = '@b3/conf/plugin_admin.ini'
    else:
        admin_plugin_conf_file = '@b3/conf/plugin_admin.xml'
    with logging_disabled():
        admin_plugin = AdminPlugin(console, admin_plugin_conf_file)
        admin_plugin._commands = {}  # work around known bug in the Admin plugin which makes the _command property shared between all instances
        admin_plugin.onStartup()

    # make sure the admin plugin obtained by other plugins is our admin plugin
    when(console).getPlugin('admin').thenReturn(admin_plugin)

    return console


def plugin_maker(console, conf):
    p = MakeroomPlugin(console, conf)
    p.onLoadConfig()
    p.onStartup()
    return p


def plugin_maker_xml(console, conf_content):
    conf = XmlConfigParser()
    conf.loadFromString(conf_content)
    return plugin_maker(console, conf)


def plugin_maker_ini(console, conf_content):
    conf = CfgConfigParser()
    conf.loadFromString(conf_content)
    return plugin_maker(console, conf)


@pytest.fixture
def superadmin(console):
    with logging_disabled():
        from b3.fake import FakeClient
    superadmin = FakeClient(console, name="Superadmin", guid="Superadmin_guid", groupBits=128, team=TEAM_UNKNOWN)
    superadmin.clearMessageHistory()
    return superadmin


@pytest.fixture
def moderator(console):
    with logging_disabled():
        from b3.fake import moderator
    moderator.console = console
    moderator.clearMessageHistory()
    return moderator


@pytest.fixture
def joe(console):
    with logging_disabled():
        from b3.fake import joe
    joe.console = console
    joe.clearMessageHistory()
    return joe


@pytest.fixture
def jack(console):
    with logging_disabled():
        from b3.fake import FakeClient
    jack = FakeClient(console, name="jack", guid="jack_guid", groupBits=1, team=TEAM_UNKNOWN)
    jack.clearMessageHistory()
    return jack