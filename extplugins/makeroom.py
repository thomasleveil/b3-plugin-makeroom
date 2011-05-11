#
# Plugin for BigBrotherBot(B3) (www.bigbrotherbot.net)
# Copyright (C) 2011 Courgette
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
# Changelog:
#
__version__ = '1.0'
__author__  = 'Courgette'

import time, string
from b3.plugin import Plugin

class MakeroomPlugin(Plugin):
    """
    This plugin provides a command to free a slot kicking the last connected player from
    the lowest group
    """
    _adminPlugin = None
    _non_member_level = None


    def onStartup(self):
        pass


    def onLoadConfig(self):
        # get the admin plugin
        self._adminPlugin = self.console.getPlugin('admin')
        if not self._adminPlugin:
            # something is wrong, can't start without admin plugin
            self.error('Could not find admin plugin')
            return False

        # register our commands
        if 'commands' in self.config.sections():
            for cmd in self.config.options('commands'):
                level = self.config.get('commands', cmd)
                sp = cmd.split('-')
                alias = None
                if len(sp) == 2:
                    cmd, alias = sp

                func = self.getCmd(cmd)
                if func:
                    self._adminPlugin.registerCommand(self, cmd, level, func, alias)


        # load non-member group level
        try:
            self._non_member_level = self.config.getint('global_settings', 'immunity_level')
        except:
            self._non_member_level = 2
        self.info('non member level : %s' % self._non_member_level)


    def onEvent(self, event):
        pass

    def getCmd(self, cmd):
        cmd = 'cmd_%s' % cmd
        if hasattr(self, cmd):
            func = getattr(self, cmd)
            return func


    def cmd_makeroom(self, data=None, client=None, cmd=None):
        """\
        free a slot
        """
        if client is None: return

        clients = self.console.clients.getClientsByLevel(min=0, max=self._non_member_level)
        clientToKick = None
        if len(clients) == 0:
            client.message('No non-member found to kick !')
        else:
            # sort players by group and connection time
            clientsByGroup = sorted(clients, key=lambda x:x.maxLevel)
            #self.debug([(x.name, x.maxLevel) for x in clientsByGroup])
            lowestGroup = clientsByGroup[0].maxLevel
            lowestClients = [x for x in clientsByGroup if x.maxLevel == lowestGroup]
            #self.debug([(x.name, x.timeAdd) for x in lowestClients])
            clientsByTime = sorted(lowestClients, key=lambda x:x.timeAdd, reverse=True)
            #self.debug([(x.name, x.timeAdd) for x in clientsByTime])
            client2kick = clientsByTime[0]
            self.console.say("kicking %s to free a slot" %client2kick.name)
            time.sleep(1.5)
            client2kick.kick(reason="to make room for a server member", keyword="makeroom", silent=True, data={"requestedby": client})

if __name__ == '__main__':

    from b3.fake import fakeConsole, moderator
    from b3.fake import FakeClient
    from b3.config import XmlConfigParser

    conf1 = XmlConfigParser()
    conf1.loadFromString("""
        <configuration plugin="makeroom">

            <settings name="global_settings">
                <!-- level under which players to kick will be chosen from (default: 2) -->
                <set name="non_member_level">2</set>
            </settings>

            <settings name="commands">
                <!-- Command to free a slot -->
                <set name="makeroom-mr">20</set>
            </settings>

        </configuration>
    """)
    p = MakeroomPlugin(fakeConsole, conf1)
    p.onStartup()

    def testPlugin1():
        jack = FakeClient(fakeConsole, name="Jack", guid="qsd654sqf", _maxLevel=0)
        jack.connects(0)
        jack.says('!makeroom')
    
    def testPlugin2():
        moderator.connects(0)
        moderator.says('!makeroom')

    def testPlugin3():
        jack = FakeClient(fakeConsole, name="Jack", guid="qsd654sqf", _maxLevel=0)
        jack.connects(1)
        moderator.connects(0)
        moderator.says('!makeroom')

    def testPlugin4():
        jack = FakeClient(fakeConsole, name="Jack", _maxLevel=0)
        jack.connects(1)
        time.sleep(1.1)
        joe = FakeClient(fakeConsole, name="Joe", _maxLevel=0)
        joe.connects(2)
        moderator.connects(0)
        moderator.says('!makeroom')

    def testPlugin5():
        jack = FakeClient(fakeConsole, name="Jack", _maxLevel=0)
        jack.connects(1)
        time.sleep(1.1)
        joe = FakeClient(fakeConsole, name="Joe", _maxLevel=2)
        joe.connects(2)
        moderator.connects(0)
        moderator.says('!makeroom')

    testPlugin5()
    time.sleep(2)
