
# Holder of all sprites. basically a look up table for any sprite you wanna grab. cant name two sprites the same.
class SpriteEnv:
    Env = [

    ]
    def Find(name):
        i = 0
        for sprite in SpriteEnv.Env:
            if name == sprite.Name:
                return SpriteEnv.Env[i]
            else:
                return f"Sprite named '{name}' cannot be found in the Sprite Environment"
            i+=1