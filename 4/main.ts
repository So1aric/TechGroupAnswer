const makeResponse = (data: unknown, code: number = 0, msg: string = "") => {
  return new Response(JSON.stringify({
    code,
    msg,
    data,
  }));
};

const servers = new Map<string, Date>();
servers.set("ZJUEVA204", new Date());

Deno.serve(async (req) => {
  const url = new URL(req.url);

  switch (url.pathname) {
    case "/ping": {
      return makeResponse({ msg: "pong" });
    }
    case "/check": {
      const data = await req.formData();
      const source = data.get("source")?.toString();

      if (!source) {
        return makeResponse({}, 101, "Should have a server name");
      }
      if (!servers.has(source)) {
        return makeResponse({ isChecked: false }, 100, "Server not authorized");
      }

      servers.set(source, new Date());

      return makeResponse({ isChecked: true });
    }
    case "/status": {
      const formatDate = (date: Date) => {
        const year = date.getFullYear();
        const month = date.getMonth();
        const day = date.getDate();
        const time = date.toLocaleTimeString().split(" ")[0];

        return `${year}/${month}/${day} ${time}`;
      };

      const data = await req.formData();
      const source = data.get("source")!.toString();

      return makeResponse({
        lastTime: formatDate(servers.get(source)!),
        isDisconnected: false,
      });
    }
    default:
      return makeResponse({});
  }
});
