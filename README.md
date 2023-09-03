# AI-Mini-Project-Breakthrough-Game

## Introduction

Welcome to the Breakthrough AI project! This project is inspired by the game "Breakthrough," which was the winner of the 2001 8 × 8 Game Design Competition, sponsored by *About.com* and *Abstract Games Magazine*. In this project, you will have the opportunity to create an artificial intelligence (AI) program to play Breakthrough on a 6×6 board.

## Game Overview

### Breakthrough Rules

- **Board Size:** The game is played on a 6×6 board, which limits the complexity compared to the original 7×7 version.
  
- **Game Type:** Breakthrough is a fully observable, strategic, deterministic game, meaning that all aspects of the game are known to both players, and there is no element of chance involved. The game always results in a win for one of the two players.

- **Objective:** Your objective is to develop a program that can play the game of Breakthrough effectively. Your program will act as a surrogate player in this game.

### Coding the AI

To code an AI to play this game, you'll need to create an agent that can take sensory input, reason about it, and output actions at each time step. Specifically, your program should be able to:

1. Read in a representation of the game board as input.
2. Output a legal move in the game of Breakthrough.

## Evaluation Function Description

The evaluation function implemented in this code serves as a critical component of our Breakthrough AI, determining the desirability of a given game state. It employs a combination of heuristic values to assess the strategic position of the AI player in the context of the game. Here's a breakdown of the key aspects of the evaluation function:

1. **Piece Count Balance:** The function starts by calculating the difference between the number of black and white pawns on the board. This balance of pieces (controlled by the `SIZE_CONSTANT`) indicates the overall strength of the AI player concerning the opponent.

2. **Protection and Attack:** To further evaluate the strategic situation, the function considers the protection and attack capabilities of the AI player and the opponent. It calculates the difference between the AI's and the opponent's protection and attack values. These values are influenced by factors such as pawn positioning and board control.

3. **High Danger Zones:** Identifying high-danger areas on the board is crucial. The evaluation function assesses the AI player's and the opponent's presence in these high-danger zones, with the goal of avoiding or capturing opponent pawns in dangerous positions.

4. **General Danger Zones:** Similar to high-danger zones, the function evaluates the presence of pawns in areas of general danger. It aims to minimize the AI player's exposure to potential threats while maximizing the opponent's vulnerabilities.

5. **Last Row Defense:** The AI's ability to defend its pawns as they approach the opponent's last row is assessed. Effective last row defense is vital for achieving the game objective, and this aspect is factored into the evaluation.

By combining these heuristic values and adjusting them with specific constants, the evaluation function provides a numeric value that represents the overall desirability of the current game state. This value guides the AI's decision-making process, helping it make informed and strategic moves in the game of Breakthrough.

The fine-tuning of these heuristic values and constants is a crucial part of enhancing the AI's gameplay performance. By continuously refining this evaluation function, the AI can become more proficient at making strategic decisions in the game.


## Search Strategy: Alpha-Beta Pruning

In the development of our Breakthrough AI, we have implemented the alpha-beta pruning technique as the core search strategy. Alpha-beta pruning is a well-established algorithm for optimizing the exploration of game trees, making it especially suitable for a game like Breakthrough with a substantial branching factor.

### Key Benefits of Alpha-Beta Pruning

- **Efficiency:** Alpha-beta pruning significantly reduces the number of nodes that need to be evaluated in the search tree, allowing our AI to make quicker decisions without sacrificing the quality of the moves.

- **Optimality:** While enhancing efficiency, alpha-beta pruning ensures that our AI still finds the optimal move within the search space, thus maintaining competitive gameplay.

- **Resource Management:** By managing resources effectively, we can adhere to the time constraints imposed by the game, providing a seamless and responsive gaming experience.

### Implementation Details

Our alpha-beta pruning implementation can be found in [template.py](https://github.com/dunliang0513/AI-Mini-Project-Breakthrough-Game/blob/main/template.py), where we carefully traverse the game tree while maintaining alpha and beta values to narrow down the search and identify the best possible move for our AI.

By utilizing this strategy, we aim to provide a challenging and engaging gaming experience in Breakthrough. Feel free to explore the code and see how alpha-beta pruning contributes to the decision-making process of our AI.


### Game Rules

- **Piece Movement:** In Breakthrough, pieces move one space directly forward or diagonally forward and capture diagonally forward.

- **Legal Moves:** Your program's moves must adhere to the game's rules. Refer to "Figure 2" for a visual representation of possible moves.

- **Off-Board Moves:** Your moves should never take your pawn outside the board.

- **Playing as Black:** Your program will always play as the black side. The objective is to move a black pawn to row index 5.

- **Move Representation:** When your agent makes a move, it should output a pair of coordinates using the coordinate system shown in the figure. For example, moving a black pawn from (0,4) to (1,3) should be represented as [0, 4] to [1, 3].

- **Legal and Timely Moves:** Your agent must always provide a legal move within 3 real-time seconds. Failure to do so will result in a decrease in your assignment score, and the competition framework will choose the next available valid move on your behalf.

## Getting Started

To get started with this project, follow the guidelines in the provided "template.py" and implement your AI agent accordingly. Ensure that your AI adheres to the rules and constraints mentioned in this README.

## Have Fun and Good Luck!

This project offers a great opportunity to explore AI in a strategic gaming context. Have fun coding your Breakthrough AI, and may the best AI player win! If you have any questions or need assistance, feel free to reach out to the course instructors or your peers. Happy coding!
