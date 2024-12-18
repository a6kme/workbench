"use client";

import WSEcho from "@/components/ws_echo";
import { useAuthContext } from "@/lib/auth";

export default function Home() {
  const { user } = useAuthContext();

  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      {user ? (
        <div>
          <h1>Hello {user.full_name}!</h1>
          <br />
          <WSEcho />
        </div>
      ) : (
        <h1>Hello There</h1>
      )}
    </div>
  );
}
