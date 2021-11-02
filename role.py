import discord
from discord.ext import commands
import random


class Role(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def weeb(self, ctx):
        members = ctx.guild.members
        role = ctx.guild.get_role(876300081521905725)
        for member in members:
            if len(member.roles) == 1:
                await member.add_roles(role)
                await ctx.send(member.mention)
        await ctx.send(f'**You all got `{role.name}` role! Congratulations!**')

    @commands.command(aliases=['r'])
    @commands.has_permissions(administrator=True)
    async def role(self, ctx, member: discord.Member, *, role: discord.Role):
        if role in member.roles:
            return await ctx.send(f'**{member.display_name}**\'s already had **{role.name}** role')
        await member.add_roles(role)
        t = f'{member.mention}, おめでとうございます！\nあなたは **{role.name}** の役割を果たしました.\n' \
            f':confetti_ball: :partying_face: :white_flower: \n' \
            f'{member.mention}, congratulations!\nYou got **{role.name}** role.'
        with open('./gifs/omedetou.txt', 'r') as f:
            gif = [line.rstrip() for line in f.readlines()]
        await ctx.send(t)
        await ctx.send(random.choice(gif))

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.MissingPermissions):
            with open('./gifs/howdareyou.txt', 'r') as f:
                gif = [line.rstrip() for line in f.readlines()]
            await ctx.send(f'**{ctx.author.mention}! Only Admin can use me! How dare you!!!**')
            await ctx.send(random.choice(gif))
