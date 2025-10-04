import os
import discord
from discord.ext import commands
from discord.ui import Button, View, Select, Modal, TextInput

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="n!", intents=intents)

SERVER_LOGO = "https://i.imgur.com/XXXXXXX.png"  # Gerçek logo linki

# --- Modal ---
class KomutAraModal(Modal, title="Komut Ara"):
    komut = TextInput(label="Komut ismi", placeholder="Aramak istediğiniz komutun ismini yazın")

    async def on_submit(self, interaction: discord.Interaction):
        komutlar = {
            "çekiliş": "Sunucuda çekiliş başlatmak için kullanılır.",
            "ticket": "Ticket sistemi açar.",
            "moderasyon": "Moderasyon komutlarını gösterir.",
            "level": "Level sistemini gösterir."
        }
        komut_ad = self.komut.value.lower()
        if komut_ad in komutlar:
            embed = discord.Embed(title=f"{komut_ad.capitalize()} Komutu",
                                  description=komutlar[komut_ad],
                                  color=discord.Color.green())
        else:
            embed = discord.Embed(title="Komut Bulunamadı",
                                  description=f"`{komut_ad}` komutu bulunamadı.",
                                  color=discord.Color.red())
        await interaction.response.send_message(embed=embed, ephemeral=True)

# --- Yardım embed ---
def get_help_embed(ctx):
    embed = discord.Embed(
        title="NexTro Bot Yardım",
        description=f"Merhaba {ctx.author.mention}! Prefixim `n!`",
        color=discord.Color.blurple()
    )
    embed.set_footer(text="NexTro | Yardım Menüsü", icon_url=SERVER_LOGO)
    return embed

@bot.command()
async def yardım(ctx):
    embed = get_help_embed(ctx)
    view = View()
    button = Button(label="Komut Ara", style=discord.ButtonStyle.blurple)
    button.callback = lambda inter: inter.response.send_modal(KomutAraModal())
    view.add_item(button)
    await ctx.send(embed=embed, view=view)

# --- Bot token ---
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
