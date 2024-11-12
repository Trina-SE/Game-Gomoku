from gomoku import GoMokuUI

if __name__ == '__main__':
    game = GoMokuUI("Gomoku", 10, GomokuUI.PVC)
    game.loop()