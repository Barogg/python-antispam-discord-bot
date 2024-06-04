# python-antispam-discord-bot
Antispam API for Python applications and sending notifications to the discord channel.

Prevents spam in your python web apps. Cloud features allow you to use additional anti-spam functionality. Cloud features allow you to use additional anti-spam functionality, such as: Personal IP/Email lists, blocking by country, language, stop words and etc.

You can read more about the Anti-Spam library here: https://github.com/CleanTalk/python-antispam?tab=readme-ov-file#python-antispam

I've created 2 examples, one using **content**(request_content file), and the other using **embeds**(request_embeds file). Depending on your preferences, choose the one you need.

## How to send notifications about spam to your Discord channel?
1) Create a webhook on your channel.
2) Copy the webhook URL and paste it into the **webhook_url** variable in the **request_embeds** or **request_content** files.
3) Paste your auth key from CleanTalk into the **auth_key** variable.
4) Run the program and you will receive a message from your bot.

Result when using **content**:

![content](https://github.com/Barogg/python-antispam-discord-bot/assets/38746827/4c2ba317-8c1c-48c1-92e0-caa77d5bda38)

and when using **embeds**:

![embeds](https://github.com/Barogg/python-antispam-discord-bot/assets/38746827/baef7b57-0e32-4153-9908-bb07660ade62)
