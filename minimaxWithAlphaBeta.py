    def alphaBetaPruning(self, depth, board_value, bound, alpha, beta, maximizingPlayer):

        if depth <= 0 or (self.checkResult() != None):
            return  board_value # Static evaluation
        
        # Transposition table of the format {hash: [score, depth]}
        if self.rollingHash in self.TTable and self.TTable[self.rollingHash][1] >= depth:
            return self.TTable[self.rollingHash][0] #return board value stored in TTable
        
        # AI is the maximizing player 
        if maximizingPlayer:
            # Initializing max value
            max_val = -math.inf

            # Look through the all possible child nodes
            for child in self.childNodes(bound):
                i, j = child[0], child[1]
                # Create a new bound with updated values
                # and evaluate the position if making the move
                new_bound = dict(bound)
                new_val = self.evaluate(i, j, board_value, 1, new_bound)
                
                # Make the move and update zobrist hash
                self.boardMap[i][j] = 1
                self.rollingHash ^= self.zobristTable[i][j][0] # index 0 for AI moves

                # Update bound based on the new move (i,j)
                self.updateBound(i, j, new_bound) 

                # Evaluate position going now at depth-1 and it's the opponent's turn
                eval = self.alphaBetaPruning(depth-1, new_val, new_bound, alpha, beta, False)
                if eval > max_val:
                    max_val = eval
                    if depth == self.depth: 
                        self.currentI = i
                        self.currentJ = j
                        self.boardValue = eval
                        self.nextBound = new_bound
                alpha = max(alpha, eval)

                # Undo the move and update again zobrist hashing
                self.boardMap[i][j] = 0 
                self.rollingHash ^= self.zobristTable[i][j][0]
                
                del new_bound
                if beta <= alpha: # prune
                    break

            # Update Transposition Table
            utils.update_TTable(self.TTable, self.rollingHash, max_val, depth)

            return max_val

        else:
            # Initializing min value
            min_val = math.inf
            # Look through the all possible child nodes
            for child in self.childNodes(bound):
                i, j = child[0], child[1]
                # Create a new bound with updated values
                # and evaluate the position if making the move
                new_bound = dict(bound)
                new_val = self.evaluate(i, j, board_value, -1, new_bound)

                # Make the move and update zobrist hash
                self.boardMap[i][j] = -1 
                self.rollingHash ^= self.zobristTable[i][j][1] # index 1 for human moves

                # Update bound based on the new move (i,j)
                self.updateBound(i, j, new_bound)

                # Evaluate position going now at depth-1 and it's the opponent's turn
                eval = self.alphaBetaPruning(depth-1, new_val, new_bound, alpha, beta, True)
                if eval < min_val:
                    min_val = eval
                    if depth == self.depth: 
                        self.currentI = i 
                        self.currentJ = j
                        self.boardValue = eval 
                        self.nextBound = new_bound
                beta = min(beta, eval)
                
                # Undo the move and update again zobrist hashing
                self.boardMap[i][j] = 0 
                self.rollingHash ^= self.zobristTable[i][j][1]

                del new_bound
                if beta <= alpha: # prune
                    break

            # Update Transposition Table
            utils.update_TTable(self.TTable, self.rollingHash, min_val, depth)

            return min_val