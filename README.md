🛡️ Guardrails & 🧠 Context Management – OpenAI Agents SDK
🛡️ Guardrails – Safety First for AI Agents
Guardrails help your agent avoid unsafe or unwanted behavior.

✅ Input Guardrails → Stop bad user prompts (e.g., math homework).

✅ Output Guardrails → Block unsafe replies (e.g., physics answers).


@input_guardrail
async def math_guardrail(...):  # Detects math help requests


@output_guardrail
async def physics_guardrail(...):  # Detects physics answer attempts

Uses GuardrailFunctionOutput to detect and trigger tripwires for safety.

🧠 Context Management – Memory for Agents
Context lets agents remember things across interactions.

🔒 local_context → Internal tool memory (not shared with the model).

📤 llm_context → Sent to the model to improve answers.


ctx.local_context.set("username", "Saad")

ctx.llm_context.append("You are a helpful assistant.")

Context helps agents stay smart, personal, and track multi-step flows.

✅ Use Guardrails for safety and Context for intelligence. Combine both for professional-grade AI agents!