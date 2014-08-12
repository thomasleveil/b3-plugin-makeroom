# -*- encoding: utf-8 -*-
from tests import *
import pytest
from mock import call, Mock


@pytest.fixture
def plugin(console):
    p = plugin_maker_xml(console, """
        <configuration>
            <settings name="commands">
                <set name="makeroomauto-mrauto">20</set>
            </settings>
            <settings name="automation">
                <set name="enabled">no</set>
                <set name="total_slots">3</set>
                <set name="min_free_slots">1</set>
            </settings>
        </configuration>
    """)
    p._delay = 0
    return p


def test_kick_non_member_when_on(plugin, superadmin, joe):
    # GIVEN
    superadmin.connects(0)
    superadmin.says('!makeroomauto on')
    plugin._total_slots = 2
    plugin._min_free_slots = 1
    joe.kick = Mock()
    # WHEN
    joe.connects(1)
    # THEN
    assert [call(reason='to free a slot', silent=True, keyword='makeroom')] == joe.kick.mock_calls


def test_no_kick_member_when_off(plugin, superadmin, joe):
    # GIVEN
    superadmin.connects(0)
    superadmin.says('!makeroomauto off')
    plugin._total_slots = 2
    plugin._min_free_slots = 1
    superadmin.says('!putgroup joe admin')
    joe.kick = Mock()
    # WHEN
    joe.connects(1)
    # THEN
    assert [] == joe.kick.mock_calls


def test_no_kick_non_member_when_off(plugin, superadmin, joe):
    # GIVEN
    superadmin.connects(0)
    superadmin.says('!makeroomauto off')
    plugin._total_slots = 2
    plugin._min_free_slots = 1
    joe.kick = Mock()
    # WHEN
    joe.connects(1)
    # THEN
    assert [] == joe.kick.mock_calls
