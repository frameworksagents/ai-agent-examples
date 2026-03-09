function routeTask(task) {
  if (task.includes("support")) {
    return "support-agent";
  }

  if (task.includes("content")) {
    return "content-agent";
  }

  return "general-agent";
}

console.log(routeTask("support ticket"));
