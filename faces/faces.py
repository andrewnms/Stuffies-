def convert(emote):
    emote = emote.replace(":)", "🙂")
    emote = emote.replace(":(", "🙁")
    
    return emote


Entry = convert(input())
print(Entry)
