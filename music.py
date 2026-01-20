import discord
from discord.ext import commands
import wavelink
import os

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        if not wavelink.Pool.nodes:
            await wavelink.Pool.connect(
                client=self.bot,
                nodes=[
                    wavelink.Node(
                        uri=f"http://{os.getenv('LAVALINK_HOST')}:{os.getenv('LAVALINK_PORT')}",
                        password=os.getenv("LAVALINK_PASSWORD")
                    )
                ]
            )
            print("🎵 Lavalink conectado")

    @commands.command()
    async def play(self, ctx, *, query: str):
        if not ctx.author.voice:
            return await ctx.send("❌ Entre em um canal de voz primeiro.")

        if not ctx.voice_client:
            vc: wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
        else:
            vc: wavelink.Player = ctx.voice_client

        tracks = await wavelink.Playable.search(query)
        if not tracks:
            return await ctx.send("❌ Música não encontrada.")

        track = tracks[0]
        await vc.play(track)

        await ctx.send(f"▶️ Tocando **{track.title}**")

    @commands.command()
    async def volume(self, ctx, vol: int):
        vc: wavelink.Player = ctx.voice_client
        if not vc:
            return await ctx.send("❌ Bot não está na call.")

        await vc.set_volume(vol)
        await ctx.send(f"🔊 Volume ajustado para {vol}%")

    @commands.command()
    async def stop(self, ctx):
        vc: wavelink.Player = ctx.voice_client
        if not vc:
            return await ctx.send("❌ Bot não está na call.")

        await vc.disconnect()
        await ctx.send("⏹️ Música parada e bot desconectado.")

async def setup(bot):
    await bot.add_cog(Music(bot))
