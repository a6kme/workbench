class ClientService {
  authToken: string | undefined;

  constructor() {
    this.authToken = undefined;
  }

  setToken(token: string | undefined) {
    this.authToken = token;
  }

  getHeaders() {
    const headers: { [key: string]: string } = {
      "Content-Type": "application/json",
    };
    if (this.authToken) {
      headers["Authorization"] = `Bearer ${this.authToken}`;
    }
    return headers;
  }

  async post(endpoint: string, payload: any) {
    const headers = this.getHeaders();
    const res = await fetch(
      `${process.env.NEXT_PUBLIC_BACKEND_URL}/${endpoint}`,
      {
        method: "POST",
        headers,
        body: JSON.stringify(payload),
      },
    );
    if (res.ok) {
      return await res.json();
    }
    throw new Error("Failed to fetch");
  }

  async get(endpoint: string, parameters: any) {
    const headers = this.getHeaders();
    const url = new URL(`${process.env.NEXT_PUBLIC_BACKEND_URL}/${endpoint}`);
    Object.keys(parameters).forEach((key) =>
      url.searchParams.append(key, parameters[key]),
    );

    const res = await fetch(url, {
      headers,
    });
    if (res.ok) {
      return await res.json();
    }
    throw new Error("Failed to fetch");
  }
}

export const clientService = new ClientService();
