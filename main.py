import sys
import os
import discord


def exec_command(command):
  std_out = sys.stdout
  sys.stdout = open("output.txt", 'w')
  try:
    exec(command[11:])
  except Exception as e:
    sys.stdout = std_out
    return f"Error: {e}"
  else:
    sys.stdout = std_out
    with open("output.txt") as file:
      result = file.read()
    return result


client = discord.Client()

@client.event
async def on_ready():
  print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('$run python'):
    await message.channel.send(exec_command(message.content))

client.run(os.environ['TOKEN'])
