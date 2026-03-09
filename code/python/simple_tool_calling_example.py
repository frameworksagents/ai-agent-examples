def search_tool(query):
    return f"result for {query}"


def agent(goal):
    result = search_tool(goal)
    return f"agent used tool: {result}"


if __name__ == "__main__":
    print(agent("framework agents"))
