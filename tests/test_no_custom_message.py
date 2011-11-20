# -*- encoding: utf-8 -*-
from b3.fake import fakeConsole, FakeClient, moderator
from makeroom import MakeroomPlugin
from b3.config import XmlConfigParser


conf = XmlConfigParser()
conf.loadFromString("""
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
p = MakeroomPlugin(fakeConsole, conf)
p.onLoadConfig()
p.onStartup()
p._delay = 0

jack = FakeClient(fakeConsole, name="Jack", guid="qsd654sqf", _maxLevel=0)
jack.connects(1)
moderator.connects(2)

moderator.says('!makeroom')