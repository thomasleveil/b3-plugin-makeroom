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

 * copy makeroom.py into b3/extplugins
 * copy makeroom.xml into b3/extplugins/conf
 * update your main b3 config file with :

<plugin name="makeroom" config="@b3/extplugins/conf/plugin_makeroom.xml"/>


Support
-------

http://forum.bigbrotherbot.net/plugins-by-courgette/makeroom-plugin/
