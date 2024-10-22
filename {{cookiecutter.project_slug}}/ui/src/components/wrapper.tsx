"use client";
import Aside from "@/components/aside";
import Header from "@/components/header";
import { useAuthContext } from "@/lib/auth";

export function LayoutWrapper({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  const { resolved } = useAuthContext();

  return resolved ? (
    <div className="min-h-screen flex flex-col">
      <Header />
      <div className="flex flex-1">
        <Aside />
        <main className="flex-1">{children}</main>
      </div>
    </div>
  ) : (
    <div className="fixed inset-0 flex items-center justify-center z-50">
      <div className="w-16 h-16 border-t-4 border-blue-500 rounded-full animate-spin"></div>
    </div>
  );
}
