## 🛡️ Guardrails in OpenAI Agents SDK

OpenAI includes **guardrails** in the Agents SDK to help ensure that both inputs and outputs are safe and appropriate.

There are two types of guardrails:

- **Input Guardrails**: Validate and filter the **user's input** before it reaches the main agent logic.
- **Output Guardrails**: Validate the **agent's final response** before it's returned to the user.

These guardrails run **in parallel to your agents**, allowing you to check and validate user input/output without interfering directly with your agent’s core logic.

### 💡 Why Use Guardrails?

Imagine you have an agent using a **smart (but slow and expensive)** model to assist with customer support. You want to avoid wasting resources on:

- Malicious or irrelevant queries
- Homework questions (e.g., "solve my math homework")

By applying a **guardrail powered by a fast and cheap model**, you can pre-screen the input:

- If a **malicious or invalid request** is detected by the input guardrail, it can raise an error immediately.
- This prevents the expensive model from running, saving both **time and money**.

### ✅ Summary

- **Input Guardrails**: Run on the **initial user input**
- **Output Guardrails**: Run on the **final agent output**
- Guardrails allow **early detection** and **cost control** in intelligent agent systems.

## 🚦 Input Guardrails

**Input guardrails** are used to validate user input before it's processed by your agent. They run in **three main steps**:

1. The guardrail receives the **same input** passed to the agent.
2. The guardrail function runs and returns a `GuardrailFunctionOutput`, which is wrapped in an `InputGuardrailResult`.
3. If `.tripwire_triggered` is `true`, an `InputGuardrailTripwireTriggered` exception is raised — allowing you to handle the error or notify the user appropriately.

### 🧠 Design Note

Input guardrails are only run if the **agent is the first agent** in the chain. This is because they are specifically designed to run on **user input**.

You might wonder why the `guardrails` property is defined on the **Agent** rather than being passed to `Runner.run()`. The reason is:  
> **Guardrails are agent-specific**. You’d likely use different guardrails for different agents, so colocating the logic on the agent improves code clarity and maintainability.

---

## ⚠️ Tripwires

**Tripwires** are the mechanism guardrails use to **halt agent execution** when unsafe input or output is detected.

If an input or output fails a guardrail check:

- The guardrail **triggers a tripwire**.
- An exception is immediately raised:
  - `InputGuardrailTripwireTriggered` for input issues
  - `OutputGuardrailTripwireTriggered` for output issues
- Agent execution is **stopped immediately** to prevent further processing.

This ensures that agents remain safe, cost-effective, and aligned with usage policies.

---

### 🔗 Reference

Read the official documentation for more info:  
[https://openai.github.io/openai-agents-python/guardrails/](https://openai.github.io/openai-agents-python/guardrails/)
