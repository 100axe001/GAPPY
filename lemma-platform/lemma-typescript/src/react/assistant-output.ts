// Moved to the framework-agnostic core. Kept here as a re-export so existing
// `lemma-sdk/react` imports keep working unchanged.
export {
  normalizeConversationStatus,
  isConversationRunningStatus,
  extractConversationMessageText,
  conversationMessageText,
  sortConversationMessagesByCreatedAt,
  getLatestAssistantMessage,
} from "../core/agent/messages.js";
