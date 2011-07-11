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


Installation
------------

 * copy makeroom.py into b3/extplugins
 * copy makeroom.xml into b3/extplugins/conf
 * update your main b3 config file with :

<plugin name="makeroom" config="@b3/extplugins/conf/plugin_makeroom.xml"/>


Changelog
---------

2011-05-12 - 1.1 : messages can be customized in the plugin config file
2011-05-29 - 1.1.1 : fix saving the kick into database
2011-06-08 - 1.2 : add info message and delay between info message and actual kick
2011-06-20 - 1.3 : add an automation feature to keep some free slot
2011-07-09 - 1.3.1 : fix issue in automation mode where the last player to connect
    would not be kicked if his level is equals to the non_member_level 
2011-07-11 - 1.4.0 : fix automated mode where any last connected player would be 
    the one kicked whatever his level
2011-07-11 - 1.4.1 : just more debug messages

Support
-------

http://forum.bigbrotherbot.net/plugins-by-courgette/makeroom-plugin/
