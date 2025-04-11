# 🔄 Token Ring Simulation

This is a simple Python simulation of the **Token Ring** network protocol. It models how computers in a ring topology pass a token around to control who can send a message on the network.

The simulation is ideal for learning the basics of:
- Message passing
- Token-based access control
- Ring topologies in computer networks

---

## 🧠 What is Token Ring?

In a **Token Ring** network:
- Each device (node) is connected in a closed loop (ring)
- A token (control signal) circulates the ring
- Only the device holding the token can send data
- Ensures no data collision and structured communication

---

## 🔧 Features

- 🔄 10 simulated computers with random IPs
- 🎟 Token passed around to control access
- 💬 Random messages sent from one node to another
- 📥 Destination receives the message in its buffer
- 🔁 Token returns to source after delivery

---

## 🛠 Requirements

- Python 3.x  

---

## 🚀 How to Run

Run the simulation directly in your terminal:

```bash
python token-ring-simulation.py
