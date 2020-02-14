import random

class Environment:
    def __init__(self):
        self.steps_left = 10

    def get_observation(self):
        return [0,0,0]
    
    def get_actions(self):
        return [0, 1]

    def action(self,action):
        if self.is_done():
            raise Exception("Game Over")
        self.steps_left -= 1
        print(self.steps_left)
        return random.random() 

    def is_done(self):  
        if self.steps_left == 0:
            return True
        else:
            return False        

class Agent:
    def __init__(self):
        self.total_reward = 0

    def step(self, env):
        self.current_obs = env.get_observation()
        self.actions = env.get_actions()
        self.reward = env.action(random.choice(self.actions))
        self.total_reward += self.reward


if __name__ == "__main__":
    env = Environment()
    agent = Agent()

    while not env.is_done():
        agent.step(env)

    agent.step(env)

    print("Game Over")