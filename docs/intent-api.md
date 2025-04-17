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
```

---

## 📥 Handling the Request

When a device receives a request, it should:

1. **Parse** the payload  
2. **Match** it to known capabilities or device actions  
3. **Execute** the requested command  
4. **Respond** with a status update  

---

## 🔁 Response Format

Devices that receive a Kivai command should respond using a standard format like this:

```json
{
  "status": "success",
  "message": "Light turned on",
  "timestamp": "2025-04-17T14:23:00Z",
  "device_id": "kitchen-light-01"
}
```

### ✅ Required fields:

- **status**: `"success"` or `"error"`  
- **message**: Human-readable result  
- **timestamp**: When the response was generated (ISO 8601 format)  
- **device_id** *(optional)*: Unique device identifier  

This format ensures consistency across devices and services, and makes debugging easier.
