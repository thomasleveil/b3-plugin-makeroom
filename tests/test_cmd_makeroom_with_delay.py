# -*- encoding: utf-8 -*-
import time
from tests import *
import pytest


t = int(time.time())


@pytest.fixture
def plugin(console):
    p = plugin_maker_xml(console, """
        <configuration>
            <settings name="global_settings">
                <!-- level (inclusive) under which players to kick will be chosen from (default: 2) -->
                <set name="non_member_level">2</set>
                <!-- delay in seconds between the time the info_message is shown and the kick happens.
                If you set this to 0, then no info_message will be shown and kick will happen
                instantly -->
                <set name="delay">.2</set>
            </settings>
            <settings name="commands">
                <set name="makeroom-mr">20</set>
            </settings>
        </configuration>
    """)
    return p


def test_no_player_to_kick(plugin, superadmin):
    # GIVEN
    superadmin.connects(0)
    # WHEN
    superadmin.says('!makeroom')
    # THEN
    time.sleep(.3)
    assert ['No non-member found to kick !'] == superadmin.message_history


def test_one_player_to_kick(plugin, superadmin, joe):
    # GIVEN
    superadmin.connects(0)
    joe.connects(1)
    joe.kick = Mock()
    # WHEN
    superadmin.says('!makeroom')
    # THEN
    time.sleep(.3)
    assert 1 == joe.kick.call_count


def test_kick_last_connected_player(plugin, superadmin, joe, jack):
    # GIVEN
    jack.kick = Mock()
    joe.kick = Mock()
    superadmin.connects(0)
    joe.connects(1)
    joe.timeAdd = t
    # WHEN
    superadmin.says('!makeroom')
    jack.connects(2)
    jack.timeAdd = t + 1
    # THEN
    time.sleep(.3)
    assert 0 == joe.kick.call_count
    assert 1 == jack.kick.call_count


def test_kick_player_of_lowest_B3_group(plugin, superadmin, joe, jack):
    # GIVEN
    joe.kick = Mock()
    jack.kick = Mock()
    superadmin.connects(0)
    joe.connects(1)
    joe.timeAdd = t
    # WHEN
    superadmin.says('!makeroom')
    # AND
    jack.connects(2)
    joe.timeAdd = t + 1
    superadmin.says('!putgroup jack reg')
    # THEN
    time.sleep(.3)
    assert 1 == joe.kick.call_count
    assert 0 == jack.kick.call_count


def test_makeroom_called_twice_within_delay(plugin, superadmin, joe):
    # GIVEN
    superadmin.connects(0)
    joe.connects(1)
    # WHEN
    superadmin.says('!makeroom')
    superadmin.says('!makeroom')
    # THEN
    assert ['There is already a makeroom request in progress. Try again later'] == superadmin.message_history