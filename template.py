import utils
import time
import copy



class PlayerAI:
    class State:
        def __init__(self, turn, from_, to_, board):
            # Is black or white turn, True => black; False => white
            self.turn = turn
            # Previous pawn's position
            self.from_ = from_
            # New pawn's position
            self.to_ = to_
            # Current board configuration
            self.board = board

        def is_black(self):
            return self.turn is True

        def is_white(self):
            return self.turn is False

        def get_src_and_dst(self):
            return [self.from_, self.to_]

        def get_black_position(self):
            result = []
            for r in range(len(board)):
                for c in range(len(board[r])):
                    if self.board[r][c] == 'B':
                        result.append([r, c])

            return result

        def get_white_position(self):
            result = []
            for r in range(len(board)):
                for c in range(len(board[r])):
                    if self.board[r][c] == 'W':
                        result.append([r, c])
            return result

    # Implement the Minimax and Alpha Beta Pruning Algorithm
    class AlphaBetaMinimax:

        def __init__(self, state):
            self.state = state
            self.board = state.board
            self.turn = state.turn
            self.from_ = state.from_
            self.to_ = state.to_

        def alpha_beta_iterative_deepening(self, state):
            MAX_TIME = 2.90
            MAX_SEARCH_DEPTH = 3
            infinity = float('inf')
            start_time = time.time()

            def alpha_beta_pruning(state, alpha, beta, depth):

                def max_value(state, alpha, beta, depth):
                    curr_value = -infinity
                    next_states = self.get_next_states(state)
                    for next_state in next_states:
                        curr_value = max(curr_value, alpha_beta_pruning(next_state, alpha, beta, depth - 1))

                        if curr_value >= beta:
                            return curr_value
                        alpha = max(curr_value, beta)
                    return curr_value

                def min_value(state, alpha, beta, depth):
                    curr_value = infinity
                    next_states = self.get_next_states(state)
                    for next_state in next_states:
                        curr_value = min(curr_value, alpha_beta_pruning(next_state, alpha, beta, depth - 1))
                        if curr_value <= alpha:
                            return curr_value
                        beta = min(curr_value, beta)
                    return curr_value

                if utils.is_game_over(state.board):
                    if state.is_black():
                        return infinity
                    else:
                        return -infinity
                end_time = time.time()
                if depth <= 0 or end_time - start_time > MAX_TIME:
                    return self.evaluation_func(state)

                if state.is_black():
                    return max_value(state, alpha, beta, depth)
                else:
                    return min_value(state, alpha, beta, depth)

            best_move = None
            alpha = -infinity
            beta = infinity
            for d in range(1, MAX_SEARCH_DEPTH):
                end_time = time.time()
                if end_time - start_time > MAX_TIME:
                    break
                next_states = self.get_next_states(state)

                for poss_next_state in next_states:
                    curr_beta_value = alpha_beta_pruning(poss_next_state, alpha, beta, d)
                    if utils.is_game_over(poss_next_state.board):
                        return poss_next_state.get_src_and_dst()

                    if curr_beta_value > alpha:
                        alpha = curr_beta_value
                        best_state = poss_next_state
                        best_move = best_state.get_src_and_dst()
            return best_move

        def get_next_states(self, state):
            possible_next_states = []
            for r in range(len(state.board)):
                for c in range(len(state.board[r])):
                    dup_board = copy.deepcopy(state.board)
                    # When it is Black turn
                    if state.is_black() and board[r][c] == 'B':
                        # Move in front one step
                        if utils.is_valid_move(board, [r, c], [r + 1, c]):
                            new_state = PlayerAI.State(not state.turn, [r, c], [r + 1, c],
                                              utils.state_change(dup_board, [r, c], [r + 1, c]))
                            possible_next_states.append(new_state)
                        # Move diagonally right
                        if utils.is_valid_move(board, [r, c], [r + 1, c + 1]):
                            new_state = PlayerAI.State(not state.turn, [r, c], [r + 1, c + 1],
                                              utils.state_change(dup_board, [r, c], [r + 1, c + 1]))
                            possible_next_states.append(new_state)
                        # Move diagonally left
                        if utils.is_valid_move(board, [r, c], [r + 1, c - 1]):
                            new_state = PlayerAI.State(not state.turn, [r, c], [r + 1, c - 1],
                                              utils.state_change(dup_board, [r, c], [r + 1, c - 1]))
                            possible_next_states.append(new_state)

                    # When it is white turn
                    else:
                        # Move in front one step
                        if utils.is_valid_move(board, [r, c], [r + 1, c]):
                            new_state = PlayerAI.State(not state.turn, [r, c], [r + 1, c],
                                              utils.state_change(dup_board, [r, c], [r + 1, c]))
                            possible_next_states.append(new_state)
                        # Move diagonally right
                        if utils.is_valid_move(board, [r, c], [r +1, c + 1]):
                            new_state = PlayerAI.State(not state.turn, [r, c], [r + 1, c + 1],
                                              utils.state_change(dup_board, [r, c], [r + 1, c + 1]))
                            possible_next_states.append(new_state)
                        # Move diagonally left
                        if utils.is_valid_move(board, [r, c], [r + 1, c - 1]):
                            new_state = PlayerAI.State(not state.turn, [r, c], [r + 1, c - 1],
                                              utils.state_change(dup_board, [r, c], [r + 1, c - 1]))
                            possible_next_states.append(new_state)

            return possible_next_states

        # Implement the evaluation function
        def evaluation_func(self, state):
            # Uses a couple of different heuristic value to decide
            value = 0
            # Constant Values
            SIZE_CONSTANT = 4
            HIGH_DANGER_CONSTANT = 6
            DANGER_CONSTANT = 3
            ATTACK_CONSTANT = 5
            PROTECTION_CONSTANT = 2
            LAST_ROW_DEFEND_CONSTANT = 1

            # List that contains black pawns positions and white pawns positions
            black_pos_list = state.get_black_position()
            white_pos_list = state.get_white_position()

            num_of_black_pawns = len(black_pos_list)
            num_of_white_pawns = len(white_pos_list)

            if state.is_black():
                value += (num_of_black_pawns - num_of_white_pawns) * SIZE_CONSTANT
            else:
                value += (num_of_white_pawns - num_of_black_pawns) * SIZE_CONSTANT

            protection_val, attack_val = self.get_protection_and_attack_value(state.turn, black_pos_list, white_pos_list)
            opp_protection_val, opp_attack_val = self.get_protection_and_attack_value(state.turn, black_pos_list, white_pos_list)
            value += (attack_val - opp_attack_val) * ATTACK_CONSTANT
            value += (protection_val - opp_protection_val) * PROTECTION_CONSTANT

            high_danger_val = self.get_high_danger_value(state.turn, black_pos_list, white_pos_list)
            opp_high_danger_val = self.get_high_danger_value(not state.turn, black_pos_list, white_pos_list)
            value += (high_danger_val - opp_high_danger_val) * HIGH_DANGER_CONSTANT

            danger_val = self.get_danger_value(state.turn, black_pos_list, white_pos_list)
            opp_danger_val = self.get_danger_value(not state.turn, black_pos_list, white_pos_list)
            value += (danger_val - opp_danger_val) * DANGER_CONSTANT

            last_row_defense = self.get_last_row_defense(state.turn, black_pos_list, white_pos_list)
            opp_last_row_defense = self.get_last_row_defense(not state.turn, black_pos_list, white_pos_list)
            value += (last_row_defense - opp_last_row_defense) * LAST_ROW_DEFEND_CONSTANT

            return value

        def get_last_row_defense(self, is_black_turn, black_pawn_list, white_pawn_list):
            result = 0
            if is_black_turn:
                defending_row = 0
                my_pawn_list = black_pawn_list
            else:
                defending_row = 5
                my_pawn_list = white_pawn_list
        
            for my_pawn in my_pawn_list:
                if my_pawn[0] == defending_row:
                    result += 1
            return result

        def get_protection_and_attack_value(self, is_black_turn, black_pawn_list, white_pawn_list):
            protection_val = 0
            attack_val = 0
            if is_black_turn:
                offset = 1
                my_pawn_list = black_pawn_list
                opponent_pawn_list = white_pawn_list
            else:
                offset = -1
                my_pawn_list = white_pawn_list
                opponent_pawn_list = black_pawn_list

            for my_pawn in my_pawn_list:
                pos_diagonal_opp_pawn1 = [my_pawn[0] + offset, my_pawn[1] + 1]
                pos_diagonal_opp_pawn2 = [my_pawn[0] + offset, my_pawn[1] - 1]
                diagonal_my_pawn_behind1 = [my_pawn[0] - offset, my_pawn[1] + 1]
                diagonal_my_pawn_behind2 = [my_pawn[0] - offset, my_pawn[1] - 1]
                # Defend value
                if pos_diagonal_opp_pawn1 in opponent_pawn_list or pos_diagonal_opp_pawn2 in opponent_pawn_list:
                    attack_val += 1
                    if diagonal_my_pawn_behind1 in my_pawn_list or diagonal_my_pawn_behind2 in my_pawn_list:
                        protection_val += 1
                    if pos_diagonal_opp_pawn1 in opponent_pawn_list and pos_diagonal_opp_pawn2 in opponent_pawn_list:
                        attack_val += 1
            return protection_val, attack_val

        def get_danger_value(self, is_black_turn, black_pawn_list, white_pawn_list):
            result = 0
            if is_black_turn:
                third_last_row = 3
                my_pawn_list = black_pawn_list
            else:
                third_last_row = 2
                my_pawn_list = white_pawn_list

            for my_pawn in my_pawn_list:
                if my_pawn[0] == third_last_row:
                    result += 1

            return result

        def get_high_danger_value(self, is_black_turn, black_pawn_list, white_pawn_list):
            result = 0
            # Danger value of a pawn can be defined by the shortest distance to the targeted row
            # Danger value is high when it is smaller or equal to 2 steps
            if is_black_turn:
                second_last_row = 4
                my_pawn_list = black_pawn_list
            else:
                second_last_row = 1
                my_pawn_list = white_pawn_list

            for my_pawn in my_pawn_list:
                if my_pawn[0] == second_last_row:
                    result += 1
            return result


    def make_move(self, board):
        '''
        This is the function that will be called from main.py
        Your function should implement a minimax algorithm with 
        alpha beta pruning to select the appropriate move based 
        on the input board state. Play for black.

        Parameters
        ----------
        self: object instance itself, passed in automatically by Python
        board: 2D list-of-lists
        Contains characters 'B', 'W', and '_' representing
        Black pawns, White pawns and empty cells respectively
        
        Returns
        -------
        Two lists of coordinates [row_index, col_index]
        The first list contains the source position of the Black pawn 
        to be moved, the second list contains the destination position
        '''
        ################
        # Starter code #
        ################
        # TODO: Replace starter code with your AI
        start_time = time.time()


        initial_state = PlayerAI.State(True, [0, 0], [0, 0], board)
        minimax = PlayerAI.AlphaBetaMinimax(initial_state)
        best_move = minimax.alpha_beta_iterative_deepening(initial_state)
        return best_move[0], best_move[1]

class PlayerNaive:
    ''' A naive agent that will always return the first available valid move '''
    def make_move(self, board):
        return utils.generate_rand_move(board)

# You may replace PLAYERS with any two players of your choice
PLAYERS = [PlayerAI(), PlayerNaive()]
COLOURS = [BLACK, WHITE] = 'Black', 'White'
TIMEOUT = 3.0

##########################
# Game playing framework #
##########################
if __name__ == "__main__":


    print("Initial State")
    board = utils.generate_init_state()
    utils.print_state(board)
    move = 0

    # game starts
    while not utils.is_game_over(board):
        player = PLAYERS[move % 2]
        colour = COLOURS[move % 2]
        if colour == WHITE: # invert if white
            utils.invert_board(board)
        start = time.time()
        src, dst = player.make_move(board) # returns [i1, j1], [i2, j2] -> pawn moves from position [i1, j1] to [i2, j2]
        end = time.time()
        within_time = end - start <= TIMEOUT
        valid = utils.is_valid_move(board, src, dst) # checks if move is valid
        if not valid or not within_time: # if move is invalid or time is exceeded, then we give a random move
            print('executing random move')
            src, dst = utils.generate_rand_move(board)
        utils.state_change(board, src, dst) # makes the move effective on the board
        if colour == WHITE: # invert back if white
            utils.invert_board(board)

        print(f'Move No: {move} by {colour}')
        utils.print_state(board) # printing the current configuration of the board after making move
        move += 1
    print(f'{colour} Won')