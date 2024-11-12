from gomoku import GoMokuUI

PVP = "PlayerVsPlayer"
PVA = "PlayerVsAI"
AVA = "AIVsAI"

if __name__ == '__main__':
    game = GoMokuUI( 10, PVA)
    game.loop()