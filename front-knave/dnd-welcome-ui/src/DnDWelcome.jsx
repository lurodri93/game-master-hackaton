import { useState } from "react";
import { motion } from "framer-motion";

export default function DnDWelcome() {
  const [name, setName] = useState("");
  const [message, setMessage] = useState("");
  const [gameStarted, setGameStarted] = useState(false);

  const sendToWebhook = async (action) => {
    const url = `http://localhost:5678/webhook/${action}`;
    const payload = { player_name: name };

    try {
      const res = await fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
      const data = await res.json();
      setMessage(data.message || JSON.stringify(data));
      
      if (action === "create" && data.success) {
        setGameStarted(true);
      }
    } catch (err) {
      setMessage("Error al conectar con el flujo de N8N");
    }
  };

  return (
    <div className="min-h-screen bg-[url('/parchment.jpg')] bg-cover bg-center p-6 flex flex-col items-center justify-center">
      <motion.div
        initial={{ opacity: 0, y: 50 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        className="w-full max-w-md bg-white/90 backdrop-blur-md rounded-2xl shadow-xl p-6 border-2 border-yellow-800"
      >
        <h1 className="text-3xl font-bold font-serif text-center text-yellow-900 mb-4">
          ✨ Bienvenido al mundo de Knave ✨
        </h1>

        <label htmlFor="player_name" className="text-yellow-900 font-semibold block mb-1">
          Nombre del aventurero:
        </label>
        <input
          id="player_name"
          placeholder="Ej. Gizmo"
          value={name}
          onChange={(e) => setName(e.target.value)}
          className="mb-4 w-full p-2 border-2 border-yellow-800 rounded focus:outline-none focus:ring-2 focus:ring-yellow-900"
        />

        <div className="grid grid-cols-3 gap-2 mb-4">
          <button className="bg-yellow-800 text-white py-2 rounded" onClick={() => sendToWebhook("create")}>Crear</button>
          <button className="bg-yellow-800 text-white py-2 rounded" onClick={() => sendToWebhook("load")}>Cargar</button>
          <button className="bg-yellow-800 text-white py-2 rounded" onClick={() => sendToWebhook("delete")}>Borrar</button>
        </div>

        {message && (
          <div className="bg-yellow-100 border border-yellow-700 rounded p-4 text-sm font-mono whitespace-pre-wrap">
            {message}
          </div>
        )}
      </motion.div>
    </div>
  );
}
