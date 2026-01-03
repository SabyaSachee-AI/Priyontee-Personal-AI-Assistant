class PriyonteeAssistant:
    def __init__(self, engine, prompt_controller, memory):
        self.engine = engine
        self.prompt_controller = prompt_controller
        self.memory = memory

    def respond(self, user_input):
        self.memory.add("User", user_input)
        prompt = self.prompt_controller.build_prompt(
            user_input, self.memory.get_history()
        )
        response = self.engine.generate(prompt)
        self.memory.add("Priyontee!", response)
        return response
