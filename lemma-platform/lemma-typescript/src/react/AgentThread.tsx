import type { ReactNode } from "react";
import {
  useConversationMessages,
  type UseConversationMessagesOptions,
  type UseConversationMessagesResult,
} from "./useConversationMessages.js";

// Headless chat primitive: the full multi-turn conversation preset. Renders only
// what its render-prop returns — the app owns the message list, composer, and
// controls; streaming, history, and final-output handling come from the core.
export interface AgentThreadProps extends UseConversationMessagesOptions {
  children: (thread: UseConversationMessagesResult) => ReactNode;
}

export function AgentThread({ children, ...options }: AgentThreadProps): ReactNode {
  const thread = useConversationMessages(options);
  return children(thread);
}
