import { clientService } from "./client";

export const getUser = async () => {
  const response = await clientService.get("api/auth/user/profile/", {});
  return response;
};
