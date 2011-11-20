# -*- encoding: utf-8 -*-
from mock import Mock
import time
from b3.fake import fakeConsole, FakeClient
from makeroom import MakeroomPlugin
from b3.config import XmlConfigParser
from tests import show_player_info


conf = XmlConfigParser()
conf.loadFromString("""
<configuration plugin="makeroom">
    <settings name="global_settings">
        <!-- delay in seconds between the time the info_message is shown and the kick happens.
        If you set this to 0, then no info_message will be shown and kick will happen
        instantly -->
        <set name="delay">0</set>
    </settings>
    <settings name="commands">
        <set name="makeroom-mr">20</set>
    </settings>
</configuration>
""")

p = MakeroomPlugin(fakeConsole, conf)
p.onLoadConfig()
p.onStartup()

guest = FakeClient(fakeConsole, name="guest", guid="guest", groupBits=0)
registered = FakeClient(fakeConsole, name="registered", guid="registered", groupBits=1)
regular = FakeClient(fakeConsole, name="regular", guid="regular", groupBits=2)
moderator = FakeClient(fakeConsole, name="moderator", guid="moderator", groupBits=8)
admin = FakeClient(fakeConsole, name="admin", guid="admin", groupBits=16)

guest.connects(0)
registered.connects(1)
regular.connects(2)
moderator.connects(3)
admin.connects(4)


show_player_info(guest)
show_player_info(registered)
show_player_info(regular)
show_player_info(moderator)
show_player_info(admin)


for p in (guest, registered, regular, moderator, admin):
    print "\n\n####################################### %s" % p.name
    p.says("!makeroom")
    time.sleep(.4)
