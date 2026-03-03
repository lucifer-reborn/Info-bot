# ⚠️ DO NOT EDIT THE CODE
import discord
from discord.ext import commands
import aiohttp
import asyncio
import gc
import time
import json
from datetime import datetime
import pytz
from zoneinfo import ZoneInfo

with open('config.json', 'r') as f:
    config = json.load(f)

TOKEN = config['token']
PREFIX = config['prefix']
ALLOWED_CHANNEL_ID = config['channel_id']

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

SMALL_IMAGE_URL = "https://cdn.discordapp.com/attachments/1447802398780428379/1478376380411678812/FF_SHORT_LOGO.PNG.png?ex=69a82ccb&is=69a6db4b&hm=16e132793e7f2c615beaf51d056f5756f758818b6547f2698cd0cbc6540b49b3"

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'Prefix: {PREFIX}')
    print(f'Allowed Channel ID: {ALLOWED_CHANNEL_ID}')

@bot.command(name="info")
@commands.cooldown(1, 30, commands.BucketType.user)
async def accinfo(ctx, uid: str):
    if ctx.channel.id != ALLOWED_CHANNEL_ID:
        return

    fetching_msg = await ctx.reply(f"🔍 **|** Fetching Info UID: {uid}.....")
    
    try:
        start_time = time.time()
        info_url = f"https://cosmos-ff-api.vercel.app/info?uid={uid}"
        
        async with aiohttp.ClientSession() as session:
            async with session.get(info_url, timeout=30) as resp:
                if resp.status != 200:
                    return await fetching_msg.edit(content=f"⚠️ **|** API Error")
                data = await resp.json()
            
            api_data = data.get("data", {})
            basicinfo = api_data.get("basicinfo", {})
            clanbasicinfo = api_data.get("clanbasicinfo", {})
            captainbasicinfo = api_data.get("captainbasicinfo", {})
            petinfo = api_data.get("petinfo", {})
            socialinfo = api_data.get("socialinfo", {})
            creditscoreinfo = api_data.get("creditscoreinfo", {})
            profileinfo = api_data.get("profileinfo", {})
            gc.collect()
            ist = pytz.timezone("Asia/Kolkata")
            ist_time = datetime.now(ist)
            embed = discord.Embed(title="**🔍 FF ID INFO**", color=0x00000,timestamp=ist_time)
            embed.set_thumbnail(url=SMALL_IMAGE_URL)
            
            basic_value = (
                f"**├─Name**: `{basicinfo.get('nickname', 'N/A')}`\n"
                f"**├─Account ID**: `{basicinfo.get('accountid', 'N/A')}`\n"
                f"**├─Level**: `{basicinfo.get('level', 'N/A')}`\n"
                f"**├─EXP**: `{basicinfo.get('exp', 'N/A')}`\n"
                f"**├─Region**: `{basicinfo.get('region', 'N/A')}`\n"
                f"**├─Release**: `{basicinfo.get('releaseversion', 'N/A')}`\n"
                f"**├─Liked**: `{basicinfo.get('liked', 'N/A')}`\n"
                f"**├─Rank**: `{basicinfo.get('rank', 'N/A')}`\n"
                f"**├─Ranking Points**: `{basicinfo.get('rankingpoints', 'N/A')}`\n"
                f"**├─CS Rank**: `{basicinfo.get('csrank', 'N/A')}`\n"
                f"**├─CS Points**: `{basicinfo.get('csrankingpoints', 'N/A')}`\n"
                f"**├─Badge ID**: `{basicinfo.get('badgeid', 'N/A')}`\n"
                f"**├─Banner ID**: `{basicinfo.get('bannerid', 'N/A')}`\n"
                f"**├─Headpic**: `{basicinfo.get('headpic', 'N/A')}`\n"
                f"**├─Avatar Frame**: `{basicinfo.get('avatarframe', 'N/A')}`\n"
                f"**├─Created**: <t:{basicinfo.get('createat', '0')}:R>\n"
                f"**└─Last Login**: <t:{basicinfo.get('lastloginat', '0')}:R>"
            )
            embed.add_field(name="**┌ BASIC INFO**", value=basic_value, inline=False)
            
            if profileinfo:
                weapon_skins = basicinfo.get('weaponskinshows', [])
                weapon_skins_str = ', '.join(str(s) for s in weapon_skins[:3]) if weapon_skins else 'N/A'
                
                profile_value = (
                    f"**├─Avatar ID**: `{profileinfo.get('avatarid', 'N/A')}`\n"
                    f"**├─Clothes**: `{profileinfo.get('clothes', ['N/A'])[0] if profileinfo.get('clothes') else 'N/A'}`\n"
                    f"**├─Primary Weapon**: `{profileinfo.get('pveprimaryweapon', 'N/A')}`\n"
                    f"**├─Equipped Skills**: `{len(profileinfo.get('equipedskills', []))} skills`\n"
                    f"**└─Weapon Skins**: `{weapon_skins_str}`"
                )
                embed.add_field(name="**┌ PROFILE INFO**", value=profile_value, inline=False)
            
            if clanbasicinfo and clanbasicinfo.get('clanname'):
                guild_value = (
                    f"**├─Guild Name**: `{clanbasicinfo.get('clanname', 'N/A')}`\n"
                    f"**├─ID**: `{clanbasicinfo.get('clanid', 'N/A')}`\n"
                    f"**├─Level**: `{clanbasicinfo.get('clanlevel', 'N/A')}`\n"
                    f"**├─Captain ID**: `{clanbasicinfo.get('captainid', 'N/A')}`\n"
                    f"**└─Members**: `{clanbasicinfo.get('membernum', 'N/A')}/{clanbasicinfo.get('capacity', 'N/A')}`"
                )
                embed.add_field(name="**┌ GUILD INFO**", value=guild_value, inline=False)
            
            if captainbasicinfo and captainbasicinfo.get('nickname'):
                captain_value = (
                    f"**├─Name**: `{captainbasicinfo.get('nickname', 'N/A')}`\n"
                    f"**├─Level**: `{captainbasicinfo.get('level', 'N/A')}`\n"
                    f"**├─EXP**: `{captainbasicinfo.get('exp', 'N/A')}`\n"
                    f"**├─Ranking Points**: `{captainbasicinfo.get('rankingpoints', 'N/A')}`\n"
                    f"**├─CS Points**: `{captainbasicinfo.get('csrankingpoints', 'N/A')}`\n"
                    f"**├─Badge Count**: `{captainbasicinfo.get('badgecnt', 'N/A')}`\n"
                    f"**├─Liked**: `{captainbasicinfo.get('liked', 'N/A')}`\n"
                    f"**├─Created**: <t:{captainbasicinfo.get('createat', '0')}:R>\n"
                    f"**└─Last Login**: <t:{captainbasicinfo.get('lastloginat', '0')}:R>"
                )
                embed.add_field(name="**┌ GUILD CAPTAIN**", value=captain_value, inline=False)
            
            if creditscoreinfo:
                credit_value = (
                    f"**├─Score**: `{creditscoreinfo.get('creditscore', 'N/A')}`\n"
                    f"**├─Reward State**: `{creditscoreinfo.get('rewardstate', 'N/A')}`\n"
                    f"**├─Summary Level**: `{creditscoreinfo.get('periodicsummarylevel', 'N/A')}`\n"
                    f"**└─End Time**: <t:{creditscoreinfo.get('periodicsummaryendtime', '0')}:R>"
                )
                embed.add_field(name="**┌ HONOR SCORE**", value=credit_value, inline=False)
            
            if petinfo and petinfo.get('name'):
                pet_value = (
                    f"**├─Pet ID**: `{petinfo.get('id', 'N/A')}`\n"
                    f"**├─Name**: `{petinfo.get('name', 'N/A')}`\n"
                    f"**├─Level**: `{petinfo.get('level', 'N/A')}`\n"
                    f"**├─EXP**: `{petinfo.get('exp', 'N/A')}`\n"
                    f"**└─Marked Star**: `{petinfo.get('ismarkedstar', 'N/A')}`"
                )
                embed.add_field(name="**┌ PET INFO**", value=pet_value, inline=False)
            
            if socialinfo:
                signature = socialinfo.get('signature', 'N/A')
                if len(signature) > 50:
                    signature = signature[:50] + "..."
                social_value = (
                    f"**├─Language**: `{socialinfo.get('language', 'N/A')}`\n"
                    f"**├─Rank Show**: `{socialinfo.get('rankshow', 'N/A')}`\n"
                    f"**└─Signature**: ```{signature}```"
                )
                embed.add_field(name="**┌ SOCIAL INFO**", value=social_value, inline=False)

            await fetching_msg.edit(content=None, embed=embed)
            print(f"Command completed in {time.time() - start_time:.2f}s")
            
    except asyncio.TimeoutError:
        await fetching_msg.edit(content="⚠️ **|** Account Not Found")
    except Exception as e:
        await fetching_msg.edit(content=f"⚠️ **|** Error: {str(e)[:100]}")
    finally:
        gc.collect()

@accinfo.error
async def accinfo_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = await ctx.reply(f"⏳ **|** Command on cooldown! Please wait {error.retry_after:.0f} seconds.")
        await asyncio.sleep(error.retry_after)
        await msg.delete()

if __name__ == "__main__":
    bot.run(TOKEN)