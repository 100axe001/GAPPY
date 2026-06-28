"use client";

// Self-contained hooks extracted from assistant-experience.tsx. Only hooks that
// take explicit inputs and return values (no closing over the component's mutable
// locals) live here; the rest stay in AssistantExperienceView to preserve behavior.

import { useCallback, useState } from "react";

export function useControllableDraft(
  controlledValue: string | undefined,
  onChange: ((value: string) => void) | undefined,
): [string, (value: string) => void] {
  const [uncontrolledValue, setUncontrolledValue] = useState("");
  const isControlled = typeof controlledValue === "string";

  const setValue = useCallback((nextValue: string) => {
    if (!isControlled) {
      setUncontrolledValue(nextValue);
    }
    onChange?.(nextValue);
  }, [isControlled, onChange]);

  return [isControlled ? controlledValue : uncontrolledValue, setValue];
}
