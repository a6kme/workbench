import { usersGetUserProfile } from "@/client/services.gen";

export const getUser = async () => {
  const response = await usersGetUserProfile();
  return response;
};
