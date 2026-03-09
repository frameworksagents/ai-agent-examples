def agent_step(state):
    if not state["done"]:
        state["notes"].append("step executed")
        state["done"] = True
    return state


if __name__ == "__main__":
    state = {"notes": [], "done": False}
    state = agent_step(state)
    print(state)
