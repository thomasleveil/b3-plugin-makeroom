# -*- encoding: utf-8 -*-
import os
from textwrap import dedent
from tests import *


@pytest.mark.skipif(not os.path.exists(DEFAULT_PLUGIN_CONFIG_FILE), reason="Could not find default plugin config file %r" % DEFAULT_PLUGIN_CONFIG_FILE)
def test_default_conf(console):
    plugin = plugin_maker(console,  DEFAULT_PLUGIN_CONFIG_FILE)
    assert 2 == plugin._non_member_level
    assert 5.0 == plugin._delay
    assert False is plugin._automation_enabled
    assert 32 is plugin._total_slots
    assert 1 is plugin._min_free_slots


def test_empty_conf(console):
    plugin = plugin_maker_ini(console,  dedent(""""""))
    assert 2 == plugin._non_member_level
    assert 5.0 == plugin._delay
    assert None is plugin._automation_enabled
    assert None is plugin._total_slots
    assert None is plugin._min_free_slots


def test_non_member_level(console):
    plugin = plugin_maker_ini(console, dedent("""
        [global_settings]
        non_member_level: 20
        """))
    assert 20 == plugin._non_member_level


def test_non_member_level_with_group_names(console):
    plugin = plugin_maker_ini(console, dedent("""
        [global_settings]
        non_member_level: mod
        """))
    assert 20 == plugin._non_member_level


def test_delay(console):
    plugin = plugin_maker_ini(console, dedent("""
        [global_settings]
        delay: 20
        """))
    assert 20 == plugin._delay


def test_automation_missing_enabled(console):
    plugin = plugin_maker_ini(console, dedent("""
        [automation]
        total_slots: 5
        min_free_slots: 1
        """))
    assert False is plugin._automation_enabled


def test_automation_off(console):
    plugin = plugin_maker_ini(console, dedent("""
        [automation]
        enabled: no
        total_slots: 5
        min_free_slots: 1
        """))
    assert False is plugin._automation_enabled


def test_automation_on(console):
    plugin = plugin_maker_ini(console, dedent("""
        [automation]
        enabled: yes
        total_slots: 5
        min_free_slots: 1
        """))
    assert True is plugin._automation_enabled


def test_automation_total_slots(console):
    plugin = plugin_maker_ini(console, dedent("""
        [automation]
        enabled: yes
        total_slots: 6
        min_free_slots: 1
        """))
    assert 6 == plugin._total_slots


def test_automation_min_free_slots(console):
    plugin = plugin_maker_ini(console, dedent("""
        [automation]
        enabled: yes
        total_slots: 6
        min_free_slots: 3
        """))
    assert 3 == plugin._min_free_slots


def test_automation_total_slots_cannot_be_less_than_2(console):
    plugin = plugin_maker_ini(console, dedent("""
        [automation]
        enabled: yes
        total_slots: 1
        min_free_slots: 1
        """))
    assert None is plugin._automation_enabled
