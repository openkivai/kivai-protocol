# Kivai Context Sharing

Kivai supports smart context sharing between devices to create seamless, multi-device interactions.

---

## 🤝 What is Context?

"Context" refers to useful metadata about a user's request, including:

- Location (`kitchen`, `living room`)
- Time (`now`, `later`, `at 6pm`)
- Active intent (e.g. `"command": "turn off"`)
- User identity and preferences
- Device capabilities

---

## 🔄 Why Share Context?

Context sharing allows one device to inform another. For example:

- A voice assistant sets the thermostat → thermostat knows who requested it and when.
- A motion sensor detects presence → triggers nearby lights or music based on preferences.
- A TV paused on one device resumes on another.

---

## 📦 Shared Context Format

Context is shared as a JSON object like this:

```json
{
  "intent": {
    "command": "turn off",
    "object": "light",
    "location": "bedroom"
  },
  "user": {
    "id": "abc123",
    "preferences": {
      "temperature_unit": "celsius",
      "language": "en"
    }
  },
  "timestamp": "2025-04-17T17:20:00Z",
  "handoff": {
    "from_device": "bedroom-sensor-01",
    "to_device": "bedroom-light-01"
  }
}
```

---

## 🔧 How Devices Use Context

- **Receiving context:** Devices can use this metadata to better respond.
- **Passing context:** Devices can send it to others via HTTP POST or shared message bus.
- **Filtering context:** Devices may ignore irrelevant or incomplete context.

---

## 📌 Future Goals

- Define a standard way to share context securely
- Build a lightweight context bus
- Enable device-to-device learning via shared history

---

Let’s build an ecosystem where devices cooperate — not compete.  
Context is the bridge to intelligence.
