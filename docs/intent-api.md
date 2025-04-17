# Kivai Intent API

The Intent API defines how devices and services should handle structured Kivai commands.

It acts as the bridge between natural language and real-world action.

---

## 🔁 Request Format

The device or service receives a JSON payload like:

```json
{
  "command": "turn on",
  "object": "light",
  "location": "kitchen",
  "trigger": "Kivai",
  "confidence": 0.95,
  "language": "en",
  "user_id": "abc123"
}
