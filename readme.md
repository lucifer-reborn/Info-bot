# FF Info Discord Bot

A Discord bot to fetch **Free Fire account information** using the Cosmos API.

---

## Features

- Fetch account info by UID.
- Shows **basic info, profile info, guild info, captain info, pet info, social info, and honor score**.
- Lightweight and simple.
- Only responds in allowed channels.

---

## Requirements

- Python 3.11+
- `discord.py`
- `aiohttp`

All required packages are listed in `requirements.txt`.

---

## Setup

### 1. Clone or Download

Clone this repository or download the ZIP.

```bash
git clone https://github.com/Lucifer-reborn/info-bot.git
cd info-bot
```

### 2. Install Dependencies

Install all packages using `requirements.txt`:

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:

```text
discord.py
aiohttp
```

### 3. Create Config File

Create a file named `config.json` in the same folder as your bot:

```json
{
  "token": "TOKEN",
  "prefix": "!",
  "allowed_channel_id": 1453862264762531995
}
```

- Replace `"TOKEN"` with your Discord bot token.
- Replace `"allowed_channel_id"` with the channel ID where the bot should respond.
- `"prefix"` can be any character(s) you want for bot commands (default: `!`).

### 4. Run the Bot

```bash
python main.py
```

Bot should now be online and ready to respond in the allowed channel.

---

## Commands

| Command | Description |
|---------|-------------|
| `!info <UID>` | Fetches all account info for the given Free Fire UID. |

### Example Usage

```text
!info 1234567890
```

The bot will reply with an embed containing:

- Basic Info
- Profile Info
- Guild Info
- Guild Captain Info
- Pet Info
- Social Info
- Honor Score

---

## Notes

- Bot will only respond in the channel ID specified in `config.json`.
- If the API fails or times out, the bot will return an error message.
- No images are fetched or displayed in this version.
- Optimized for low memory usage and fast responses.

---

## Credits

- **YT**: [Luciferr-GG](https://www.youtube.com/@Luciferr-GG)
- **Discord**: [Lucifer_reborn](https://discord.com/users/1396114922097868862)
- **GitHub**: [Lucifer-reborn/info-bot](https://github.com/Lucifer-reborn/info-bot)

---

## License

This project is for personal use and non-commercial projects.  
Redistribution or modification is allowed with credit.