# Subscriptions-Twitch-to-OBS
When you subscribe to a twich channel in the obs displays the nicknames of users


First you need to install the plugin on obs (OBS WebSocket Plugin) - https://github.com/obsproject/obs-websocket/releases. 
I recommend to download version 4.9.1, it is more stable than newer ones. There are two types of installation, windows-installer.exe - automatic installation and windows.zip - manual installation
Open OBS - Tools - WebSockets Server Settings - be sure to set a password. 
Set any port (standard 4444)
Create a source text (FreeType 2) under the obligatory name ‘SubText’ leave the text empty, do not enter anything there. Then put on the Scrolling filter 
After that, open the exe file.
OBS host is localhost
If OBS is running on another device in local network or via internet, you will need to specify IP address of this device instead of localhost.
write localhost if you run the bot on one device, if you use vpn specify vpn-address.
OBS port - in our case 4444 (which you set in the obs plugin).
Twitch Access Token: it can be found at (https://dev.twitch.tv/console) I think you know it better than I do.
Twitch Channel Name - this is the nickname of the Twitch.
(If you want to test you can use https://twitchtokengenerator.com/ there you can create a Twitch token, but it is better to use your own, I think for obvious reasons).
That's it, the script should work. It displays the top 15 people who gave sabki, this number can be easily changed. The rest is to be customised in the OBS.
You can test the script with the commands 
!test_sub - adds a test sub and displays it in OBS.
!test_multiple_subs 10 - adds 10 test subs.
These commands should be entered on Twitch
