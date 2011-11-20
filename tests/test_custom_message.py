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

        <settings name="messages">
            <!-- You can use the following keywords in your messages :
                $clientname
            -->
            <!-- kick_message will be displayed to all players when a player is kicked to free a slot -->
            <set name="kick_message">kicking $clientname to make room for a member xxxxxxxxxx</set>
            <!-- kick_reason will be displayed to the player to be kicked -->
            <set name="kick_reason">to free a slot ! mlkjmlkj</set>
        </settings>
    </configuration>
""")
p = MakeroomPlugin(fakeConsole, conf)
p.onLoadConfig()
p.onStartup()
p._delay = 0.1

jack = FakeClient(fakeConsole, name="Jack", guid="qsd654sqf", _maxLevel=0)
jack.connects(1)
moderator.connects(2)

moderator.says('!makeroom')