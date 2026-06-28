export interface SseRawEvent {
  event?: string;
  data: string;
  raw: string;
}

/**
 * Async iterator over Server-Sent Event frames.
 */
export async function* readSSE(
  stream: ReadableStream<Uint8Array>,
): AsyncGenerator<SseRawEvent, void, unknown> {
  const reader = stream.getReader();
  const decoder = new TextDecoder();

  let buffer = "";
  let eventName: string | undefined;
  let dataLines: string[] = [];

  const flush = (): SseRawEvent | null => {
    if (dataLines.length === 0) {
      eventName = undefined;
      return null;
    }

    const data = dataLines.join("\n");
    const raw = `${eventName ? `event: ${eventName}\n` : ""}${dataLines
      .map((line) => `data: ${line}`)
      .join("\n")}`;

    const next: SseRawEvent = {
      event: eventName,
      data,
      raw,
    };

    eventName = undefined;
    dataLines = [];
    return next;
  };

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;

    buffer += decoder.decode(value, { stream: true });
    const lines = buffer.split("\n");
    buffer = lines.pop() || "";

    for (const line of lines) {
      const trimmed = line.endsWith("\r") ? line.slice(0, -1) : line;

      if (trimmed === "") {
        const event = flush();
        if (event) {
          yield event;
        }
        continue;
      }

      if (trimmed.startsWith("event:")) {
        eventName = trimmed.slice("event:".length).trim();
        continue;
      }

      if (trimmed.startsWith("data:")) {
        dataLines.push(trimmed.slice("data:".length).trim());
      }
    }
  }

  const event = flush();
  if (event) {
    yield event;
  }
}

export function parseSSEJson<T = unknown>(event: SseRawEvent): T | null {
  if (!event.data || event.data === "[DONE]") {
    return null;
  }

  try {
    return JSON.parse(event.data) as T;
  } catch {
    return null;
  }
}
