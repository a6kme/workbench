import pino from "pino";

// Use Pino on the server and console on the client
export const logger = pino({
  name: "ui",
  level: process.env.NEXT_PUBLIC_NODE_ENV === "production" ? "info" : "debug",
});
