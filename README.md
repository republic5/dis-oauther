# Dis-oauther

This repository is a simple discord oauth implementation.
It is expected to be used for anti vpn and participation in the guild for authenticated users.

## 1 Setup

- 1. Create bot <br/>
  Go [here](https://discord.com/developers/applications) and click New application. <br/>
  And choose a name, agree to the [TOS](https://discord.com/developers/docs/policies-and-agreements/terms-of-service) and [Privacy](https://discord.com/developers/docs/policies-and-agreements/developer-policy), and create your bot.
  
- 2. Setting bot <br/>
  Enable all Gateway Intents.
  
- 3. Edit config.yml <br/>
  Open Config.<br/>
  And, Press Reset Token from Bot and copy - paste.<br/>
  Describe guild_id and role_id to assign a role.<br/>
  _This bot has Anti vpn functionality. If used, see section 2._
 
- 4. Make url <br/>
  Go to OAuth2.<br/>
  Copy the CLIENT ID and CLIENT SECRET from Client information and paste them into config.yml.
  Then add the url you plan to forward to Redirects and add /login there.<br/>
  The url should be pasted into the redirect_uri in config.yml.<br/>
  Next, go to URL Generator from the left bar and select the url you just created from SELECT REDIRECT URL.
  Also select a scope.<br/>
  Copy the URL from the GENERATED URL.
  This is important for login.<br/>
  The selected scope is also stuck to the config.yml.<br/>
  _Example: identify%20guilds.join_
  
- 5.  Stating bot<br/>
  Install the package with pip install -r requirements.txt.<br/>
  Finally, python main.py is used to start it up.
  
## 2 Anti vpn
Anti vpn by [getipintel](https://www.getipintel.net/).<br/>
However, it is recommended to set anti_vpn to false when planning or scaling up large servers, as errors caused by rate limiting can cause problems.<br/>
If used, anti_vpn must be set to true and email must be an email address that can receive email.

## 3 License
republic5 follows the MIT license.

## 4 Docker & k8s
Plans for implementation.
