// Entry for the opt-in lemma-ui browser bundle. Auto-registers the custom
// elements on load so a no-build HTML app can just drop a <script> tag and use
// <lemma-agent-task> / <lemma-agent-thread>.
import {
  defineLemmaElements,
  LemmaAgentTaskElement,
  LemmaAgentThreadElement,
} from "./ui/index.js";

defineLemmaElements();

export { defineLemmaElements, LemmaAgentTaskElement, LemmaAgentThreadElement };
