# 🚦 Verified Smart Traffic System (K Framework & Django)

This project implements a road traffic control system that utilizes **Formal Methods** to guarantee the safety of transitions between traffic light states. The innovation lies in using the **K Framework** for real-time (Runtime Verification) of decisions made by the web application.



## 🛠️ Technologies Used
* **Backend:** Django (Python) - Simulation and interface management.
* **Formal Verification:** K Framework - Definition of mathematical rewriting rules.
* **Interface:** HTML/CSS (Real-time monitoring).
* **Protocol:** Integration between Python and the K verification engine.

## 🧠 How It Works
Unlike a traditional system, this system does not change the traffic light color directly. 
1. **Interception:** Any state change request (e.g., Green -> Yellow) is intercepted.
2. **Formal Verification:** The request is sent to the **K Framework**.
3. **Validation:** If the transition respects the mathematically defined safety rules (no green conflicts), the K Framework approves the state.
4. **Execution:** Only after approval does the system update the visual interface.



## 🛡️ Guaranteed Safety
The system prevents human error or software logic bugs by mathematically proving that the system will never enter an unsafe state (e.g., simultaneous green lights on conflicting directions).

---
*Project developed for the "Software Engineering" course at UTCN.*
