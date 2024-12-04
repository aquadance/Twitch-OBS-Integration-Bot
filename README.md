
# 🎮 Twitch & OBS Integration Bot  

**Easily display Twitch subscription statistics in OBS with this interactive bot!**  
Integrate your Twitch channel with OBS seamlessly and enhance your streaming experience.  

---

### 🔧 **Installation Guide**  

1. **Install OBS WebSocket Plugin**:  
   - Download it from [OBS WebSocket Plugin Releases](https://github.com/obsproject/obs-websocket/releases).  
   - For stability, I recommend **version 4.9.1**.  
   - Choose your installation type:  
     - **windows-installer.exe** (Automatic installation)  
     - **windows.zip** (Manual installation)  

2. **Configure OBS**:  
   - Open **OBS** → **Tools** → **WebSockets Server Settings**:  
     - Set a **password** for security.  
     - Use any port (default: `4444`).  

3. **Create a Text Source** in OBS:  
   - Add a text source (**FreeType 2**) with the name **`SubText`**.  
   - Leave the text field empty.  
   - Apply the **Scrolling filter** for smooth animation.

4. **Set Up the Bot**:  
   - Run the `.exe` file (bot application).  
   - Input the following details:  
     - **OBS Host**: Use `localhost` if the bot runs on the same machine as OBS.  
       - For a different device, use its local network **IP address**.  
       - If using VPN, enter your VPN address.  
     - **OBS Port**: Match the port set in OBS (default: `4444`).  
     - **Twitch Access Token**:  
       - Generate it from [Twitch Developer Console](https://dev.twitch.tv/console).  
       - For testing, you can also use [Twitch Token Generator](https://twitchtokengenerator.com/) (not recommended for production).  
     - **Twitch Channel Name**: Your Twitch username.

---

### 🎮 **Features**  

- Displays the **top 15 subscribers** (can be adjusted in code).  
- Real-time updates on **Twitch events** like subscriptions.  
- **Customizable text design** in OBS for a professional stream overlay.  
- **Test commands** to simulate Twitch events for easy debugging.  

---

### 🛠️ **Commands**  

- **`!test_sub`**: Add a single test subscription and display it in OBS.  
- **`!test_multiple_subs <number>`**: Add multiple test subscriptions (e.g., `!test_multiple_subs 10`).  

---

### 💡 **Additional Notes**  

- The bot works with **OBS WebSocket Plugin** version 4.9.1 for better stability.  
- You can customize text design directly in OBS under the `SubText` source settings.  
