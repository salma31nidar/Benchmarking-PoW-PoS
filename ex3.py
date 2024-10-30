import hashlib
import time
import random

class Block:
    def __init__(self, index, data, prev_hash=""):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.prev_hash = prev_hash
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.prev_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "Genesis Block")

    def add_block(self, block):
        self.chain.append(block)

class ProofOfStake:
    def __init__(self):
        self.stakers = {}

    def add_stake(self, staker, amount):
        self.stakers[staker] = self.stakers.get(staker, 0) + amount

    def select_validator(self):
        total_stake = sum(self.stakers.values())
        pick = random.uniform(0, total_stake)
        current = 0
        for staker, stake in self.stakers.items():
            current += stake
            if current >= pick:
                return staker

class ProofOfWork:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def mine(self, block):
        start_time = time.time()
        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * self.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()
        end_time = time.time()
        return computed_hash, end_time - start_time

# Création de la blockchain et des systèmes de consensus
blockchain = Blockchain()
pos = ProofOfStake()
pow = ProofOfWork(difficulty=4)

# Ajouter des validateurs avec différentes quantités de jetons pour PoS
pos.add_stake("Validator1", 50)
pos.add_stake("Validator2", 150)
pos.add_stake("Validator3", 300)

# Proof of Stake: Sélection d'un validateur et ajout d'un bloc
start_time_pos = time.time()
validator = pos.select_validator()
new_block_pos = Block(len(blockchain.chain), f"Bloc validé par {validator}", blockchain.chain[-1].hash)
blockchain.add_block(new_block_pos)
end_time_pos = time.time()

# Proof of Work: Minage d'un bloc
new_block_pow = Block(len(blockchain.chain), "Bloc miné avec PoW", blockchain.chain[-1].hash)
_, time_pow = pow.mine(new_block_pow)
blockchain.add_block(new_block_pow)

# Affichage des temps d'exécution
print(f"Temps d'exécution pour Proof of Stake (PoS) : {end_time_pos - start_time_pos:.4f} secondes")
print(f"Temps d'exécution pour Proof of Work (PoW) : {time_pow:.4f} secondes")
