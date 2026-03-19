# 🚦 Verified Smart Traffic System (K Framework & Django)

Acest proiect implementează un sistem de control al traficului rutier care utilizează **Metode Formale** pentru a garanta siguranța tranzițiilor între stările semafoarelor. Inovația constă în utilizarea **K Framework** pentru verificarea în timp real (Runtime Verification) a deciziilor luate de aplicația web.

## 🛠️ Tehnologii Utilizate
* **Backend:** Django (Python) - Gestionarea simulării și interfeței.
* **Formal Verification:** K Framework - Definirea regulilor matematice de rescriere.
* **Interfață:** HTML/CSS (Monitorizare în timp real).
* **Protocol:** Integrare între Python și motorul de verificare K.

## 🧠 Cum funcționează?
Spre deosebire de un sistem clasic, acest sistem nu schimbă culoarea semaforului direct. 
1. **Intercepție:** Orice cerere de schimbare a stării (ex. Verde -> Galben) este interceptată.
2. **Verificare Formale:** Cererea este trimisă către **K Framework**.
3. **Validare:** Dacă tranziția respectă regulile de siguranță definite matematic (nu există conflicte de verde), K Framework aprobă starea.
4. **Execuție:** Doar după aprobare, sistemul actualizează interfața vizuală.

## 🛡️ Siguranță Garantată
Sistemul previne erorile umane sau de logică software prin demonstrarea matematică a faptului că sistemul nu va intra niciodată într-o stare nesigură (ex. semafoare verzi simultan pe direcții conflictuale).

---
*Proiect realizat pentru disciplina "Software Engineering" la UTCN.*
