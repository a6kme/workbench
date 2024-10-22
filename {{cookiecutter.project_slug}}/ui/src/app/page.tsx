"use client";

import { useAuthContext } from "@/lib/auth";

export default function Home() {
  const { user } = useAuthContext();

  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      {user ? <h1>Hello {user.name}!</h1> : <h1>Hello There</h1>}
    </div>
  );
}
