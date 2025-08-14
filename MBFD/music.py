import discord
from discord.ext import commands
import yt_dlp as youtube_dl

class Music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            return await ctx.send("❌ No estás en un canal de voz.")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def disconnect(self, ctx):
        if ctx.voice_client:
            await ctx.voice_client.disconnect()
            await ctx.send("👋 Me he desconectado.")
        else:
            await ctx.send("❌ No estoy en un canal de voz.")

    @commands.command()
    async def play(self, ctx, url: str):
        if ctx.voice_client is None:
            return await ctx.send("❌ No estoy conectado a un canal de voz. Usa `?join` primero.")

        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            'options': '-vn'
        }
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': True}

        try:
            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
                url2 = info['url']
                source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
                ctx.voice_client.play(source)
            await ctx.send(f"🎶 Reproduciendo: **{info.get('title', 'Desconocido')}**")
        except Exception as e:
            await ctx.send(f"⚠️ Error al reproducir: `{e}`")

    @commands.command()
    async def pause(self, ctx):
        if ctx.voice_client and ctx.voice_client.is_playing():
            ctx.voice_client.pause()
            await ctx.send("⏸ Pausado.")
        else:
            await ctx.send("❌ No hay nada reproduciéndose.")

    @commands.command()
    async def resume(self, ctx):
        if ctx.voice_client and ctx.voice_client.is_paused():
            ctx.voice_client.resume()
            await ctx.send("▶️ Reanudado.")
        else:
            await ctx.send("❌ No hay nada pausado.")

async def setup(client):
    await client.add_cog(Music(client))
