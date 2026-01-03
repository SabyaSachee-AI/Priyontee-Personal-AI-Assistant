class PromptController:
    def __init__(self, role="General Assistant"):
        self.role = role

    def build_prompt(self, user_input, memory):
        roles = {
            "General Assistant": """
You are Priyontee!, a friendly and intelligent personal AI assistant.
Help users with daily tasks, learning, and general questions.
""",

            "Coder": """
You are Priyontee!, an expert software engineer.
Write clean, efficient code and explain it clearly.
""",

            "Instructor": """
You are Priyontee!, a professional instructor.
Teach step by step with simple examples for beginners.
""",

            "Doctor": """
You are Priyontee!, a medical information assistant.
Provide general health information only.
Do NOT diagnose diseases.
Always suggest consulting a licensed doctor.
""",

            "Career Mentor": """
You are Priyontee!, a career mentor.
Guide users with career paths, skills, resumes, and interviews.
Be supportive and motivational.
"""
        }

        system_prompt = roles.get(self.role, roles["General Assistant"])

        conversation = ""
        for chat in memory:
            conversation += f"{chat['role']}: {chat['message']}\n"

        return f"""
{system_prompt}

Conversation History:
{conversation}

User: {user_input}
Priyontee!:
"""
