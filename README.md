# kivai-protocol

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status: In Development](https://img.shields.io/badge/Status-In%20Development-blue)
![JSON Schema: Draft-07](https://img.shields.io/badge/Schema-Draft--07-green)

**The open protocol and API format for enabling communication between humans and intelligent devices using the Kivai language.**

---

## 🔌 What is the Kivai Protocol?

The Kivai Protocol defines how devices, services, and applications interpret, exchange, and act on commands issued in the Kivai language.

It is designed to be:

- 💬 **Language-agnostic** — works with human speech or text in any language
- 📡 **Platform-independent** — usable on any device, OS, or ecosystem
- 🤝 **Interoperable** — encourages communication between different devices, brands, and services
- 🔓 **Open & extensible** — community-driven, built to evolve

---

## 📦 Core Components

This repository will define:

- **Protocol schema** – The standard format for Kivai commands and responses (JSON-based)
- **Intent API** – A common API for devices to receive and respond to parsed Kivai commands
- **Context sharing** – A mechanism for smart handoff and coordination between devices
- **Authentication & trust layer** – Optional lightweight auth between trusted devices

---

## 🧪 Examples

```json
{
  "command": "turn on",
  "object": "light",
  "location": "kitchen",
  "confidence": 0.97,
  "trigger": "Kivai",
  "language": "en",
  "user_id": "abc123"
}
```

---

## 🔗 Integration Goals

- Create SDKs and reference libraries (JavaScript, Python, etc.)
- Provide embeddable modules for smart devices
- Offer gateway support for legacy systems and cloud APIs

---

## 👥 Who Should Use This?

- Device manufacturers
- Smart home tinkerers
- App developers
- AI & NLP researchers
- Anyone building human-centric technology

---

## 🚀 Roadmap

- ✅ Define v0.1 protocol schema
- 🔲 Draft API structure and sample calls
- 🔲 Create reference implementation
- 🔲 Build mock devices and testbed
- 🔲 Write security & trust guidelines

---

## 🙌 Contribute

We’re building an open, human-first language for machines — and we need you.  
Help define how technology listens, understands, and responds.

Open an issue. Propose a schema. Share an idea. Let’s create the future — together.


---

### ✅ Your Turn:
1. Replace your current README with this content.
2. Commit it with a message like:  
   **`Add protocol overview and goals to README`**

Let me know when that’s done and we’ll move to the **next key piece** — defining the actual **Kivai protocol schema (v0.1)**!

---

## 🧾 Command Schema (v0.1)

You can find the official Kivai command schema here:  
[`schema/kivai-command.schema.json`](./schema/kivai-command.schema.json)

This JSON Schema defines how devices and services should interpret Kivai commands.  
It can be used to:

- Validate commands generated by NLP engines
- Ensure consistent formatting across platforms
- Build integrations for smart devices and systems

> The schema includes fields like `command`, `object`, `location`, `confidence`, `trigger`, and more.

More versions and extended schemas coming soon!

---

## 🛠️ How to Use the Schema

Want to integrate Kivai into your app or device? Here’s how:

### 🧪 Validate Commands
Make sure your command structure matches the official schema:

1. Go to [jsonschemavalidator.net](https://www.jsonschemavalidator.net)
2. Paste the contents of [`kivai-command.schema.json`](./schema/kivai-command.schema.json) into the **Schema** box
3. Paste your Kivai command into the **Data** box
4. You should see `No errors found` when your command is valid ✅

### 🔗 Integrate It
You can use this schema to:

- Validate input from voice assistants or chatbots
- Power your own intent engine or device API
- Build smart home devices, apps, or Kivai-compatible tools

## Running the CLI Demo Script

You can use the `demo.py` script to interact with the mock devices.

### Prerequisites

Before running the script, you need to install the `requests` library.

You can do this by running:

```bash
pip install requests

---

## 🚀 Running the Demo

### Prerequisites
Before running the demo, make sure you have installed the required dependencies. You can install the necessary library using pip:

```bash
pip install requests
```

### Running the Demo Script

1. Run the mock device server (e.g., `mock-thermostat.py`) by executing the following command:

```bash
python mock-thermostat.py
```

2. After the server is running, run the demo script to send requests to the server:

```bash
python demo.py
```

### Example Output

When the demo script runs successfully, you should see output like this:

```json
{
    "device_id": "kitchen-thermostat-01",
    "message": "Temperature set to 21°C in kitchen",
    "status": "success",
    "timestamp": "2025-04-17T17:34:54.623009Z"
}
```

### Example Commands in the Demo Script

```python
import requests
import json

# Define the endpoint and headers
url = "http://127.0.0.1:5001/intent"
headers = {"Content-Type": "application/json"}

# Create a payload for the thermostat
payload = {
    "command": "set temperature",
    "object": "thermostat",
    "location": "kitchen",
    "temperature": 21
}

# Send POST request
response = requests.post(url, json=payload, headers=headers)

# Print the response from the server
print(response.status_code)
print(response.json())
```

### Notes
- Make sure the mock server is running before executing the demo script.
- This demo simulates the thermostat setting and checks the status of the device by sending JSON data to the server.

## License
MIT License. See the `LICENSE` file for more information.

