makeroom plugin for Big Brother Bot (www.bigbrotherbot.net)
===========================================================

By Courgette


Description
-----------

This plugin provides a command that will kick the player who last joined server from the lowest group.
This command is useful on popular servers which need to make room for member players.


Command :
---------

!makeroom : kick the last non-member player who entered the game
!makeroomauto <on|off> : will makeroom every time the server gets full


Installation
------------

 * copy makeroom.py into `b3/extplugins`
 * copy plugin_makeroom.ini in the same directory as your b3.xml file
 * update your main b3 config file with :

```xml
<plugin name="makeroom" config="@conf/plugin_makeroom.ini"/>
```

Support
-------

http://forum.bigbrotherbot.net/plugins-by-courgette/makeroom-plugin/
