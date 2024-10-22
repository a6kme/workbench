"use client";
import Link from "next/link";

export default function Aside() {
  return (
    <aside className="hidden md:block w-64">
      <nav>
        <ul>
          <li>
            <Link href="/">Home</Link>
          </li>
          <li>
            <Link href="/about">About</Link>
          </li>
          <li>
            <Link href="/contact">Contact</Link>
          </li>
        </ul>
      </nav>
    </aside>
  );
}
