import pickle

words = ["aardvark", "baboon", "camel", "opera", "learn",
         "breed", "large", "chaos", "cheek", "arrow",
         "rider", "gaffe", "kneel", "drive", "waist",
         "small", "light", "liver", "video", "dance",
         "braid", "album", "trade", "onion", "burst",
         "gloom", "faith", "stand", "pilot", "grand",
         "mercy", "guide", "weigh", "flush", "tough",
         "dough", "press", "angle", "graze", "greet",
         "house", "tight", "shaft", "frank", "wagon",
         "print", "leash", "ridge", "harsh", "stain",
         "voter", "scrap", "awful", "canvas", "refund",
         "reform", "wander", "snatch", "basket", "praise",
         "outlet", "script", "happen", "square", "action",
         "choose", "admire", "extent", "salmon", "census",
         "gravel", "person", "needle", "layout", "tiptoe",
         "prefer", "health", "second", "likely", "record",
         "export", "bitter", "guitar", "rocket", "carrot",
         "circle", "speech", "direct", "ballet", "honest",
         "sphere", "bubble", "banner", "empire", "desert",
         "stress", "string", "prayer", "squash", "church"]


def create_words():
    save_file = open('words.dat', 'wb')
    pickle.dump(words, save_file)
    save_file.close()

