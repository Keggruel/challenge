namespace SpriteKind {
    export const Item = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Item, function (sprite2, otherSprite2) {
    tiles.placeOnRandomTile(mySprite2, assets.tile`myTile`)
    mySprite2.setStayInScreen(true)
    info.changeScoreBy(1)
    music.play(music.melodyPlayable(music.baDing), music.PlaybackMode.UntilDone)
    sprites.destroy(mySprite2, effects.fire, 500)
    pause(1000)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Player, function (sprite2, otherSprite2) {
    info.changeScoreBy(-1)
    music.play(music.melodyPlayable(music.thump), music.PlaybackMode.UntilDone)
    pause(1000)
})
function addItem () {
    if (mySprite.overlapsWith(mySprite2)) {
        sprites.destroy(mySprite2, effects.fire, 500)
        mySprite2 = sprites.create(img`
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
            `, SpriteKind.Item)
        tiles.placeOnRandomTile(mySprite2, assets.tile`myTile`)
    }
}
let mySprite2: Sprite = null
let mySprite: Sprite = null
scene.setBackgroundColor(1)
tiles.setCurrentTilemap(tilemap`level2`)
tiles.setWallAt(tiles.getTileLocation(scene.screenHeight(), scene.screenWidth()), true)
mySprite = sprites.create(assets.image`myImage`, SpriteKind.Player)
mySprite.setStayInScreen(true)
controller.moveSprite(mySprite)
mySprite2 = sprites.create(img`
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
    `, SpriteKind.Item)
let mySprite3 = sprites.create(assets.image`myImage0`, SpriteKind.Projectile)
let mySprite4 = sprites.create(assets.image`myImage0`, SpriteKind.Projectile)
let mySprite5 = sprites.create(assets.image`myImage0`, SpriteKind.Projectile)
tiles.placeOnRandomTile(mySprite3, assets.tile`myTile`)
tiles.placeOnRandomTile(mySprite4, assets.tile`myTile`)
tiles.placeOnRandomTile(mySprite5, assets.tile`myTile`)
mySprite3.setBounceOnWall(true)
mySprite3.setVelocity(40, 50)
mySprite3.setStayInScreen(true)
mySprite4.setBounceOnWall(true)
mySprite4.setVelocity(55, 65)
mySprite4.setStayInScreen(true)
mySprite5.setBounceOnWall(true)
mySprite5.setVelocity(70, 60)
mySprite5.setStayInScreen(true)
