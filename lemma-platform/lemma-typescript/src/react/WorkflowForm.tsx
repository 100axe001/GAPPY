import type { ReactNode } from "react";
import {
  useWorkflowForm,
  type UseWorkflowFormOptions,
  type UseWorkflowFormResult,
} from "./useWorkflowForm.js";

// Headless workflow-form primitive: renders only what its render-prop returns.
// Apps own the timeline, inputs, and buttons; this handles field derivation,
// value state, and the submit payload.
export interface WorkflowFormProps extends UseWorkflowFormOptions {
  children: (form: UseWorkflowFormResult) => ReactNode;
}

export function WorkflowForm({ children, ...options }: WorkflowFormProps): ReactNode {
  const form = useWorkflowForm(options);
  return children(form);
}
