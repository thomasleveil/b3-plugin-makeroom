# -*- encoding: utf-8 -*-
import time
from b3.fake import fakeConsole, superadmin, joe, FakeClient
from makeroom import MakeroomPlugin
from b3.config import XmlConfigParser


conf = XmlConfigParser()
conf.loadFromString("""
    <configuration plugin="makeroom">
        <settings name="commands">
            <!-- Command to free a slot -->
            <set name="makeroomauto-mrauto">20</set>
        </settings>
        <settings name="automation">
            <!-- enabled : yes/no
              If yes, then this plugin will make sure that min_free_slots are kept free
              and kick all connecting player until min_free_slots are free.
             -->
            <set name="enabled">no</set>
            <!-- The total number of slots on the server  -->
            <set name="total_slots">3</set>
            <!-- The number of slots to keep free -->
            <set name="min_free_slots">1</set>
        </settings>
    </configuration>
""")
p = MakeroomPlugin(fakeConsole, conf)
p.onLoadConfig()
p.onStartup()
p._delay = 0

superadmin.connects(0)
superadmin.says('!makeroomauto')
superadmin.says('!makeroomauto on')
superadmin.says('!makeroomauto off')

print "\n\n+++++++++++++++++++++++++++++++++ when joe connects, he should get kicked"
fakeConsole.clients.clear()
p._automation_enabled = True
p._delay = 1
p._total_slots = 2
p._min_free_slots = 1
superadmin.connects(0)
time.sleep(.3)
joe.connects(1)
time.sleep(2)

print "\n\n+++++++++++++++++++++++++++++++++ when jack connects, he should get kicked"
fakeConsole.clients.clear()
p._automation_enabled = True
p._delay = 0
p._total_slots = 3
p._min_free_slots = 1
joe.connects(0)
time.sleep(.3)
superadmin.connects(1)
time.sleep(.3)
jack = FakeClient(fakeConsole, name="Jack", guid="qsd654sqf", _maxLevel=2)
jack.connects(2)
time.sleep(2)