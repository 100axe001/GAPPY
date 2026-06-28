"use client";

import type { ReactNode } from "react";
import { Button } from "@/components/ui/button";
import { RotateCcw } from "lucide-react";
import type { AgentRuntimeConfig, AvailableModelInfo } from "lemma-sdk";
import type {
  AssistantControllerView,
  LemmaAssistantDensity,
} from "./assistant-types";
import {
  AssistantHeader,
  AssistantModelPicker,
  type AssistantSurfaceTone,
} from "./assistant-chrome";

export interface AssistantExperienceHeaderProps {
  controller: AssistantControllerView;
  headerTone: AssistantSurfaceTone;
  title: ReactNode;
  subtitle: ReactNode;
  badge: ReactNode;
  headerLeadingActions: ReactNode;
  headerActions: ReactNode;
  density: LemmaAssistantDensity;
  showModelPicker: boolean;
  showNewConversationButton: boolean;
  availableModelOptions: AvailableModelInfo[];
  isConversationBusy: boolean;
  isUpdatingModel: boolean;
  onModelChange: (nextModel: string | null, runtime?: AgentRuntimeConfig | null) => void;
}

export function AssistantExperienceHeader({
  controller,
  headerTone,
  title,
  subtitle,
  badge,
  headerLeadingActions,
  headerActions,
  density,
  showModelPicker,
  showNewConversationButton,
  availableModelOptions,
  isConversationBusy,
  isUpdatingModel,
  onModelChange,
}: AssistantExperienceHeaderProps) {
  return (
    <AssistantHeader
      tone={headerTone}
      title={title}
      subtitle={subtitle}
      badge={badge}
      leadingControls={headerLeadingActions}
      compact={density === "compact"}
      controls={showModelPicker || showNewConversationButton || headerActions ? (
        <>
          {showModelPicker ? (
            <AssistantModelPicker
              value={controller.conversationModel}
              runtime={controller.conversationRuntime ?? null}
              options={availableModelOptions}
              onChange={(nextModel, runtime) => { onModelChange(nextModel, runtime); }}
              disabled={isConversationBusy || isUpdatingModel}
              autoLabel="Auto"
              compact={density === "compact"}
            />
          ) : null}
          {showNewConversationButton ? (
            <Button
              type="button"
              variant="ghost"
              size="icon"
              onClick={controller.clearMessages}
              title="New conversation"
              className="size-9"
            >
              <RotateCcw className="size-3.5" />
            </Button>
          ) : null}
          {headerActions}
        </>
      ) : undefined}
    />
  );
}
