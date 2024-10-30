# Blockchain with Proof of Work (PoW) and Proof of Stake (PoS)

This project implements a simple blockchain in Python with two consensus mechanisms: Proof of Work (PoW) and Proof of Stake (PoS). The code allows for adding new blocks to the blockchain through either mining (PoW) or validator selection (PoS).

## Features

- **Blockchain Structure**: Basic blockchain with `Block` and `Blockchain` classes, including a genesis block.
- **Proof of Work (PoW)**: A mining-based consensus mechanism, adjustable by difficulty level.
- **Proof of Stake (PoS)**: A stake-based consensus where validators are selected based on the number of tokens held.

## Code Overview

### `Block` Class
Represents a single block in the blockchain.
- `compute_hash()`: Computes the hash of the block using SHA-256.

### `Blockchain` Class
Manages the chain of blocks.
- `create_genesis_block()`: Creates the initial block in the chain.
- `add_block(block)`: Adds a new block to the chain.

### `ProofOfStake` Class
Implements a simple Proof of Stake mechanism.
- `add_stake(staker, amount)`: Adds stake for a validator.
- `select_validator()`: Randomly selects a validator based on stake weight.

### `ProofOfWork` Class
Implements a mining mechanism with adjustable difficulty.
- `mine(block)`: Mines a block by finding a hash with the required number of leading zeros.
