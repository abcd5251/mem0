import os
from mem0 import Memory
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

config = {
    "llm": {
        "provider": "openai",
        "config": {
            "model": "gpt-4o-mini",
            "temperature": 0.2,
            "max_tokens": 1500,
        }
    }
}
m = Memory.from_config(config)
result = m.add("I am working on improving my tennis skills. Suggest some online courses.", user_id="alice", metadata={"category": "hobbies"})
print(result)
# Created memory: Improving her tennis skills. Looking for online suggestions.

# Retrieve memories
all_memories = m.get_all()
print(all_memories)

# Search memory
related_memories = m.search(query="What are Alice's hobbies?", user_id="alice")
print(related_memories)

#  Update a memory
result = m.update(memory_id="m1", data="Likes to play tennis on weekends")
print(result)

# Get memory history
history = m.history(memory_id="m1")
print(history)
