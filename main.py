@namespace
class SpriteKind:
    Item = SpriteKind.create()

def on_on_overlap(sprite2, otherSprite2):
    tiles.place_on_random_tile(mySprite2, assets.tile("""
        myTile
    """))
    mySprite2.set_stay_in_screen(True)
    info.change_score_by(1)
    music.play(music.melody_playable(music.ba_ding),
        music.PlaybackMode.UNTIL_DONE)
    sprites.destroy(mySprite2, effects.fire, 500)
    pause(1000)
sprites.on_overlap(SpriteKind.player, SpriteKind.Item, on_on_overlap)

def on_on_overlap2(sprite22, otherSprite22):
    info.change_score_by(-1)
    music.play(music.melody_playable(music.thump),
        music.PlaybackMode.UNTIL_DONE)
    pause(1000)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.player, on_on_overlap2)

def addItem():
    global mySprite2
    if mySprite.overlaps_with(mySprite2):
        sprites.destroy(mySprite2, effects.fire, 500)
        mySprite2 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . f f f f f f f f f . . . 
                            . . . f f 5 5 5 5 5 5 5 f f . . 
                            . . f f 5 5 5 5 5 5 5 5 5 f f . 
                            . . f 5 5 5 f f f 5 1 5 5 5 f . 
                            . . f 5 5 f 5 5 5 5 1 5 5 5 f . 
                            . . f 5 5 f 5 5 5 5 1 5 5 5 f . 
                            . . f 5 5 f 5 5 5 5 5 5 5 5 f . 
                            . . f 5 5 5 5 5 5 5 5 5 5 5 f . 
                            . . f 5 5 f 5 5 5 5 5 5 5 5 f . 
                            . . f 5 5 5 5 f 5 f 5 5 5 5 f . 
                            . . f f 5 5 5 5 5 5 5 5 5 f f . 
                            . . . f f 5 5 5 5 5 5 5 f f . . 
                            . . . . f f f f f f f f f . . .
            """),
            SpriteKind.Item)
        tiles.place_on_random_tile(mySprite2, assets.tile("""
            myTile
        """))
mySprite2: Sprite = None
mySprite: Sprite = None
scene.set_background_color(1)
tiles.set_current_tilemap(tilemap("""
    level2
"""))
tiles.set_wall_at(tiles.get_tile_location(scene.screen_height(), scene.screen_width()),
    True)
mySprite = sprites.create(assets.image("""
    myImage
"""), SpriteKind.player)
mySprite.set_stay_in_screen(True)
controller.move_sprite(mySprite)
mySprite2 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . f f f f f f f f f . . . 
            . . . f f 5 5 5 5 5 5 5 f f . . 
            . . f f 5 5 5 5 5 5 5 5 5 f f . 
            . . f 5 5 5 f f f 5 1 5 5 5 f . 
            . . f 5 5 f 5 5 5 5 1 5 5 5 f . 
            . . f 5 5 f 5 5 5 5 1 5 5 5 f . 
            . . f 5 5 f 5 5 5 5 5 5 5 5 f . 
            . . f 5 5 5 5 5 5 5 5 5 5 5 f . 
            . . f 5 5 f 5 5 5 5 5 5 5 5 f . 
            . . f 5 5 5 5 f 5 f 5 5 5 5 f . 
            . . f f 5 5 5 5 5 5 5 5 5 f f . 
            . . . f f 5 5 5 5 5 5 5 f f . . 
            . . . . f f f f f f f f f . . .
    """),
    SpriteKind.Item)
mySprite3 = sprites.create(assets.image("""
    myImage0
"""), SpriteKind.projectile)
mySprite4 = sprites.create(assets.image("""
    myImage0
"""), SpriteKind.projectile)
mySprite5 = sprites.create(assets.image("""
    myImage0
"""), SpriteKind.projectile)
tiles.place_on_random_tile(mySprite3, assets.tile("""
    myTile
"""))
tiles.place_on_random_tile(mySprite4, assets.tile("""
    myTile
"""))
tiles.place_on_random_tile(mySprite5, assets.tile("""
    myTile
"""))
mySprite3.set_bounce_on_wall(True)
mySprite3.set_velocity(40, 50)
mySprite3.set_stay_in_screen(True)
mySprite4.set_bounce_on_wall(True)
mySprite4.set_velocity(55, 65)
mySprite4.set_stay_in_screen(True)
mySprite5.set_bounce_on_wall(True)
mySprite5.set_velocity(70, 60)
mySprite5.set_stay_in_screen(True)