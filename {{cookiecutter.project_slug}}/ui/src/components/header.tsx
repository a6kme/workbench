"use client";

import { useAuthContext } from "@/lib/auth";
import { supabase } from "@/utils/supabase";

export default function Header() {
  const { user, setAuthContext } = useAuthContext();

  const signOut = async () => {
    await supabase.auth.signOut();
    setAuthContext((prev) => ({
      ...prev,
      user: null,
    }));
  };

  const signInWithGoogle = async () => {
    await supabase.auth.signInWithOAuth({
      provider: "google",
      options: {
        redirectTo: `${window.location.origin}`,
      },
    });
  };

  return (
    <header className="flex flex-1 p-4">
      <div className="hidden md:block md:flex-1">
        <h1 className="text-2xl font-bold">{{cookiecutter.project_name.title()}}</h1>
      </div>

      {user ? (
        <div>
          <button
            type="button"
            className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800"
            onClick={signOut}
          >
            Logout
          </button>
        </div>
      ) : (
        <button
          type="button"
          className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800"
          onClick={signInWithGoogle}
        >
          Login
        </button>
      )}
    </header>
  );
}
