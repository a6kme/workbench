"use client";

import { UserPublic } from "@/client/types.gen";
import { logger } from "@/lib/logger";
import { getUser } from "@/service/auth";
import { clientService } from "@/service/client";
import { supabase } from "@/utils/supabase";
import { useRouter } from "next/navigation";
import React, {
  createContext,
  useContext,
  useEffect,
  useRef,
  useState,
} from "react";

interface AuthContextType {
  user: UserPublic | null;
  resolved: boolean;
  setAuthContext: React.Dispatch<React.SetStateAction<AuthContextType>>;
}

const initialContext: AuthContextType = {
  user: null,
  resolved: false,
  setAuthContext: () => {},
};

const AuthContext = createContext<AuthContextType>(initialContext);

export const AuthProvider = ({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) => {
  logger.debug("Mounting AuthProvider");

  const [authContext, setAuthContext] = useState(initialContext);
  const mountRef = useRef(false);
  const router = useRouter();

  useEffect(() => {
    logger.debug("In AuthProvider useEffect");

    const loadSupabaseSession = async () => {
      // Get session from supabase
      const {
        data: { session },
        error,
      } = await supabase.auth.getSession();

      logger.debug("loadSupabaseSession error is", error);

      if (session === null) {
        logger.debug("No session found");
        setAuthContext((prev: AuthContextType) => ({
          ...prev,
          user: null,
          resolved: true,
        }));
      } else {
        clientService.setToken(session.access_token);

        // If the user is logged in, get the user and state from application server
        const { data } = await getUser();

        setAuthContext((prev: AuthContextType) => ({
          ...prev,
          user: data ?? null,
          resolved: true,
        }));
      }
    };

    // In react strict mode, useEffect is called twice,
    // so we need to check if the component is mounted
    if (!mountRef.current) {
      loadSupabaseSession();
      mountRef.current = true;
    }
    return () => {
      logger.debug("Unmounting AuthProvider");
    };
  }, [router]);

  return (
    <AuthContext.Provider value={{ ...authContext, setAuthContext }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuthContext = () => {
  return useContext(AuthContext);
};
