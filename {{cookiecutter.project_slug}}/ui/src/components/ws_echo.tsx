/*
 * This is a simple example of a component that uses a WebSocket connection to
 * echo messages back to the client.
 */

"use client";

import { clientService } from "@/service/client";
import { useEffect, useState } from "react";

export default function WSEcho() {
  const [message, setMessage] = useState<string>("");
  const [socket, setSocket] = useState<WebSocket | null>(null);

  useEffect(() => {
    const ws = clientService.getWebSocket("ws/auth/echo/");

    ws.onopen = () => {
      console.log("Connected to websocket");
    };

    ws.onmessage = (event: MessageEvent) => {
      const data = JSON.parse(event.data);
      setMessage(data.message);
    };

    setSocket(ws);

    return () => {
      ws.close();
    };
  }, []);

  const sendMessage = () => {
    if (socket) {
      const randomNum = Math.round(Math.random() * 100);
      socket.send(
        JSON.stringify({ message: `Hello from Next.js! ${randomNum}` }),
      );
    }
  };

  return (
    <div>
      <p>Received message: {message}</p>
      <button onClick={sendMessage}>Send Message</button>
    </div>
  );
}
