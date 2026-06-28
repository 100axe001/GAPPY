"use client";

import { forwardRef, useMemo, useState, type ComponentPropsWithoutRef, type ReactNode } from "react";
import Image from "next/image";
import { Bot, Check, ChevronDown, Search, X } from "lucide-react";
import type { AgentRuntimeConfig, AvailableModelInfo } from "lemma-sdk";
import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import type {
  AssistantConversationListItem,
  AssistantConversationRenderArgs,
  LemmaAssistantRadius,
} from "./assistant-types";

export type AssistantSurfaceTone = "default" | "subtle" | "flat";
export type AssistantThemeMode = "auto" | "light" | "dark";

const RADIUS_MAP: Record<string, Record<string, string>> = {
  none: { shell: "rounded-none", item: "rounded-none", bubble: "rounded-none", inline: "rounded-none" },
  sm: { shell: "rounded-sm", item: "rounded-sm", bubble: "rounded-sm", inline: "rounded-sm" },
  md: { shell: "rounded-md", item: "rounded-md", bubble: "rounded-md", inline: "rounded-md" },
  lg: { shell: "rounded-lg", item: "rounded-md", bubble: "rounded-lg", inline: "rounded-md" },
  xl: { shell: "rounded-xl", item: "rounded-lg", bubble: "rounded-xl", inline: "rounded-lg" },
};

function assistantRadius(radius: LemmaAssistantRadius, kind: "shell" | "item" | "bubble" | "inline"): string {
  return RADIUS_MAP[radius]?.[kind] ?? RADIUS_MAP.lg[kind];
}

export function conversationStatusDotColor(status?: string | null): string {
  const s = (status || "").toLowerCase();
  if (s === "running" || s === "active") return "status-dot-active";
  if (s === "completed" || s === "done") return "status-dot-success";
  if (s === "error" || s === "failed") return "status-dot-error";
  return "status-dot-warning";
}

export function relativeTimeAgo(dateStr?: string | null): string {
  if (!dateStr) return "";
  const date = new Date(dateStr);
  if (isNaN(date.getTime())) return "";
  const now = Date.now();
  const diffMs = now - date.getTime();
  const seconds = Math.floor(diffMs / 1000);
  if (seconds < 60) return "just now";
  const minutes = Math.floor(seconds / 60);
  if (minutes < 60) return `${minutes}m ago`;
  const hours = Math.floor(minutes / 60);
  if (hours < 24) return `${hours}h ago`;
  const days = Math.floor(hours / 24);
  return `${days}d ago`;
}

export interface AssistantThemeScopeProps extends ComponentPropsWithoutRef<"div"> {
  children: ReactNode;
  theme?: AssistantThemeMode;
}

export const AssistantThemeScope = forwardRef<HTMLDivElement, AssistantThemeScopeProps>(function AssistantThemeScope({
  className,
  children,
  theme = "auto",
  ...props
}, ref) {
  return (
    <div
      ref={ref}
      data-lemma-theme={theme}
      className={cn("flex h-full min-h-0 w-full flex-col", theme === "dark" && "dark", className)}
      {...props}
    >
      {children}
    </div>
  );
});

export interface AssistantHeaderProps extends Omit<ComponentPropsWithoutRef<"div">, "title"> {
  title: ReactNode;
  subtitle?: ReactNode;
  badge?: ReactNode;
  leadingControls?: ReactNode;
  controls?: ReactNode;
  tone?: AssistantSurfaceTone;
  compact?: boolean;
}

export interface AssistantMessageViewportProps extends ComponentPropsWithoutRef<"div"> {
  innerClassName?: string;
  children: ReactNode;
}

export const AssistantMessageViewport = forwardRef<HTMLDivElement, AssistantMessageViewportProps>(function AssistantMessageViewport({
  className,
  innerClassName,
  children,
  ...props
}, ref) {
  return (
    <div
      ref={ref}
      className={cn("min-h-0 flex-1 overflow-y-auto bg-[var(--pod-main-bg)] px-4 py-6 [font-family:var(--font-landing-sans),var(--font-body-family)] [overflow-anchor:none] sm:px-6 lg:px-8", className)}
      {...props}
    >
      <div className={cn("mx-auto flex w-full max-w-4xl flex-col gap-6", innerClassName)}>
        {children}
      </div>
    </div>
  );
});

export interface AssistantShellLayoutProps extends ComponentPropsWithoutRef<"div"> {
  sidebar?: ReactNode;
  sidebarVisible?: boolean;
  main: ReactNode;
  radius?: LemmaAssistantRadius;
}

export const AssistantShellLayout = forwardRef<HTMLDivElement, AssistantShellLayoutProps>(function AssistantShellLayout({
  sidebar,
  sidebarVisible = false,
  main,
  radius = "lg",
  className,
  ...props
}, ref) {
  const hasSidebar = !!sidebar;

  return (
    <div
      ref={ref}
      className={cn(
        "flex h-full min-h-0 w-full flex-col gap-3",
        hasSidebar && sidebarVisible && "lg:grid lg:grid-cols-[minmax(16rem,24rem)_minmax(0,1fr)] lg:items-stretch",
        assistantRadius(radius, "shell"),
        className,
      )}
      {...props}
    >
      {sidebar && sidebarVisible ? (
        <div className={cn("min-h-0 overflow-hidden border border-[color:color-mix(in_srgb,var(--border-subtle)_60%,transparent)] bg-[color:color-mix(in_srgb,var(--surface-2)_25%,transparent)] shadow-[var(--shadow-sm)]", assistantRadius(radius, "shell"))}>
          {sidebar}
        </div>
      ) : null}
      {main}
    </div>
  );
});

export const AssistantHeader = forwardRef<HTMLDivElement, AssistantHeaderProps>(function AssistantHeader({
  title,
  subtitle,
  badge,
  leadingControls,
  controls,
  tone = "subtle",
  compact = false,
  className,
  ...props
}, ref) {
  return (
    <div
      ref={ref}
      data-tone={tone}
      className={cn(
        "lemma-assistant-header flex shrink-0 items-center justify-between border-b border-[color:color-mix(in_srgb,var(--border-subtle)_60%,transparent)]",
        compact ? "gap-2 px-3 py-2" : "gap-3 px-4 py-3 sm:px-6",
        tone === "default" && "bg-[color:color-mix(in_srgb,var(--card-bg)_95%,transparent)]",
        tone === "subtle" && "bg-[color:color-mix(in_srgb,var(--bg-canvas)_95%,transparent)]",
        tone === "flat" && "bg-transparent",
        className,
      )}
      {...props}
    >
      <div className={cn("flex min-w-0 items-center", compact ? "gap-2" : "gap-3")}>
        {leadingControls}
        {badge ? (
          <span className={cn("flex shrink-0 items-center justify-center rounded-lg bg-[var(--action-primary)] text-[var(--text-on-brand)]", compact ? "size-7" : "size-9")}>
            {badge}
          </span>
        ) : null}
        <div className="min-w-0">
          <h3 className={cn("truncate font-semibold tracking-tight text-[var(--text-primary)]", compact ? "text-sm" : "text-lg")}>{title}</h3>
          {subtitle && !compact ? (
            <p className="truncate text-sm text-[var(--text-secondary)]">{subtitle}</p>
          ) : null}
        </div>
      </div>
      {controls ? (
        <div className={cn("flex shrink-0 items-center", compact ? "gap-1" : "gap-2")}>{controls}</div>
      ) : null}
    </div>
  );
});

export interface AssistantConversationListProps extends Omit<ComponentPropsWithoutRef<"aside">, "title"> {
  conversations: AssistantConversationListItem[];
  activeConversationId: string | null;
  onSelectConversation: (conversationId: string) => void;
  onNewConversation?: () => void;
  renderConversationLabel?: (args: AssistantConversationRenderArgs) => ReactNode;
  title?: ReactNode;
  newLabel?: ReactNode;
  radius?: LemmaAssistantRadius;
}

export const AssistantConversationList = forwardRef<HTMLElement, AssistantConversationListProps>(function AssistantConversationList({
  conversations,
  activeConversationId,
  onSelectConversation,
  onNewConversation,
  renderConversationLabel,
  title = "Conversations",
  newLabel = "New",
  radius = "lg",
  className,
  ...props
}, ref) {
  return (
    <aside ref={ref} className={cn("flex h-full min-h-0 flex-col overflow-hidden border border-[color:color-mix(in_srgb,var(--border-subtle)_60%,transparent)] bg-[color:color-mix(in_srgb,var(--surface-2)_25%,transparent)]", assistantRadius(radius, "shell"), className)} {...props}>
      <div className="border-b border-[color:color-mix(in_srgb,var(--border-subtle)_60%,transparent)] px-4 py-3">
        <div className="flex items-center justify-between gap-3">
          <div className="min-w-0">
            <div className="truncate text-sm font-semibold text-[var(--text-primary)]">{title}</div>
            <div className="mt-0.5 text-xs text-[var(--text-secondary)]">
              {conversations.length} total
            </div>
          </div>
          {onNewConversation ? (
            <Button
              type="button"
              variant="outline"
              size="sm"
              onClick={onNewConversation}
              className="h-8 px-3 text-sm"
            >
              {newLabel}
            </Button>
          ) : null}
        </div>
      </div>
      <div className="flex min-h-0 flex-1 flex-col gap-2 overflow-y-auto p-3">
        {conversations.map((conversation) => {
          const isActive = conversation.id === activeConversationId;
          return (
            <button
              key={conversation.id}
              type="button"
              onClick={() => onSelectConversation(conversation.id)}
              aria-current={isActive ? "page" : undefined}
              className={cn(
                 "lemma-assistant-conversation-row-button w-full border px-3 py-3 text-left text-sm transition-colors",
                 assistantRadius(radius, "item"),
                 isActive
                   ? "border-[color:var(--row-border)] bg-[var(--card-bg)] shadow-[var(--shadow-sm)]"
                   : "lemma-assistant-conversation-list-item-idle",
               )}
            >
              <div className="truncate font-medium">
                {renderConversationLabel
                  ? renderConversationLabel({ conversation, isActive })
                  : (conversation.title || "Untitled conversation")}
              </div>
              <div className="mt-1 flex items-center gap-1.5 text-xs text-[var(--text-secondary)]">
                <span className={cn("size-1.5 rounded-full flex-shrink-0", conversationStatusDotColor(conversation.status))} />
                <span>{relativeTimeAgo(conversation.updated_at || conversation.created_at)}</span>
              </div>
            </button>
          );
        })}
      </div>
    </aside>
  );
});

const AUTO_RUNTIME_VALUE = "__AUTO_RUNTIME__";
const HARNESS_LOGOS: Partial<Record<string, string>> = {
  ANTIGRAVITY: "/harnesslogos/antigravity.png",
  CLAUDE_CODE: "/harnesslogos/claudecode.png",
  CODEX: "/harnesslogos/codex.png",
  OPENCODE: "/harnesslogos/opencode.png",
};

function assistantRuntimeKey(runtime: AgentRuntimeConfig): string {
  return `${runtime.profile_id}::${runtime.model_name ?? ""}`;
}

function shortAssistantModelName(modelName: string): string {
  const normalized = modelName.replace(/\/$/, "");
  const markerMatch = normalized.match(/\/(?:models|routers)\/([^/]+)$/);
  if (markerMatch?.[1]) return markerMatch[1];
  return normalized.split("/").filter(Boolean).at(-1) || normalized;
}

function assistantModelPathHint(modelName: string): string | null {
  const shortName = shortAssistantModelName(modelName);
  if (shortName === modelName) return null;
  return modelName.replace(new RegExp(`/?${escapeRuntimeRegExp(shortName)}$`), "").replace(/\/$/, "") || modelName;
}

function escapeRuntimeRegExp(value: string): string {
  return value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

function formatHarnessName(harnessKind?: string | null): string {
  if (!harnessKind) return "Models";
  return harnessKind
    .split("_")
    .filter(Boolean)
    .map((part) => part.slice(0, 1).toUpperCase() + part.slice(1).toLowerCase())
    .join(" ");
}

function modelRuntime(option: AvailableModelInfo): AgentRuntimeConfig | null {
  if (option.runtime) return option.runtime;
  if (option.profile_id) {
    return {
      profile_id: option.profile_id,
      model_name: option.id,
    };
  }
  return null;
}

interface AssistantRuntimeGroup {
  key: string;
  harnessKind: string | null;
  displayName: string;
  options: AvailableModelInfo[];
}

export interface AssistantModelPickerProps extends Omit<ComponentPropsWithoutRef<"div">, "onChange"> {
  value: string | null;
  runtime?: AgentRuntimeConfig | null;
  options: AvailableModelInfo[];
  disabled?: boolean;
  autoLabel?: ReactNode;
  compact?: boolean;
  onChange: (value: string | null, runtime?: AgentRuntimeConfig | null) => void;
}

export const AssistantModelPicker = forwardRef<HTMLDivElement, AssistantModelPickerProps>(function AssistantModelPicker({
  value,
  runtime,
  options,
  disabled,
  autoLabel = "Auto",
  compact = false,
  onChange,
  className,
  ...props
}, ref) {
  const [isOpen, setIsOpen] = useState(false);
  const [query, setQuery] = useState("");
  const [expandedHarnessKey, setExpandedHarnessKey] = useState<string | null>(null);

  const selectedOption = useMemo(() => {
    if (!value) return null;
    if (runtime) {
      return options.find((option) => {
        const optionRuntime = modelRuntime(option);
        return option.id === value
          && optionRuntime?.profile_id === runtime.profile_id
          && optionRuntime?.model_name === runtime.model_name;
      }) ?? null;
    }
    return options.find((option) => option.id === value) ?? null;
  }, [options, runtime, value]);

  const selectedRuntime = runtime ?? (selectedOption ? modelRuntime(selectedOption) : null);
  const selectedKey = selectedRuntime ? assistantRuntimeKey(selectedRuntime) : value ?? AUTO_RUNTIME_VALUE;
  const selectedHarnessName = selectedOption?.agentRuntime?.name ?? selectedOption?.profile?.name ?? selectedRuntime?.profile_id ?? null;
  const selectedModelLabel = selectedRuntime?.model_name
    ? shortAssistantModelName(selectedRuntime.model_name)
    : selectedOption?.name
      ? shortAssistantModelName(selectedOption.name)
      : value
        ? shortAssistantModelName(value)
        : null;
  const triggerLabel = selectedModelLabel
    ? selectedHarnessName
      ? `${selectedHarnessName} · ${selectedModelLabel}`
      : selectedModelLabel
    : autoLabel;

  const groups = useMemo<AssistantRuntimeGroup[]>(() => {
    const byKey = new Map<string, AssistantRuntimeGroup>();

    options.forEach((option) => {
      const optionRuntime = modelRuntime(option);
      const harnessKind = option.harness_kind ?? null;
      const key = optionRuntime?.profile_id ?? option.profile_id ?? harnessKind ?? "MODELS";
      const existing = byKey.get(key);
      if (existing) {
        existing.options.push(option);
        return;
      }
      byKey.set(key, {
        key,
        harnessKind,
        displayName: option.agentRuntime?.name ?? option.profile?.name ?? formatHarnessName(harnessKind),
        options: [option],
      });
    });

    return Array.from(byKey.values()).sort((a, b) => a.displayName.localeCompare(b.displayName));
  }, [options]);

  const filteredGroups = useMemo(() => {
    const normalizedQuery = query.trim().toLowerCase();
    if (!normalizedQuery) return groups;

    return groups
      .map((group) => {
        const harnessMatches = `${group.displayName} ${group.harnessKind ?? ""}`.toLowerCase().includes(normalizedQuery);
        const matchingOptions = group.options.filter((option) => {
          const optionRuntime = modelRuntime(option);
          return [
            option.id,
            option.name,
            option.agentRuntime?.name,
            option.profile?.name,
            optionRuntime?.profile_id,
            optionRuntime?.model_name,
            shortAssistantModelName(optionRuntime?.model_name ?? option.name ?? option.id),
          ].filter(Boolean).join(" ").toLowerCase().includes(normalizedQuery);
        });

        if (!harnessMatches && matchingOptions.length === 0) return null;
        return {
          ...group,
          options: harnessMatches ? group.options : matchingOptions,
        };
      })
      .filter((group): group is AssistantRuntimeGroup => Boolean(group));
  }, [groups, query]);

  const closePicker = () => {
    setIsOpen(false);
    setQuery("");
    setExpandedHarnessKey(null);
  };

  const handleSelect = (nextValue: string | null, nextRuntime?: AgentRuntimeConfig | null) => {
    onChange(nextValue, nextRuntime ?? null);
    closePicker();
  };

  return (
    <div ref={ref} className={className} {...props}>
      <button
        type="button"
        onClick={() => setIsOpen(true)}
        disabled={disabled}
        className={cn(
          "lemma-assistant-runtime-trigger-button inline-flex max-w-[240px] items-center rounded-lg border border-[var(--row-border)] bg-[var(--field-bg)] text-left text-sm font-medium shadow-none transition-colors hover:border-[var(--field-border-hover)] disabled:cursor-not-allowed disabled:opacity-55",
          compact ? "h-8 min-w-0 gap-1.5 px-2" : "h-9 min-w-28 gap-2 px-2.5",
        )}
        aria-label="Conversation model"
      >
        <span
          className={cn(
            "rounded-full border border-[var(--chip-border)] bg-[var(--chip-bg)] px-1.5 py-0.5 text-xs font-semibold text-[var(--text-secondary)]",
            compact && "sr-only",
          )}
        >
          Model
        </span>
        <span className="min-w-0 flex-1 truncate text-sm font-semibold text-[var(--text-primary)]">
          {triggerLabel}
        </span>
        <ChevronDown className="size-3.5 shrink-0 text-[var(--text-tertiary)]" />
      </button>

      <Dialog
        open={isOpen}
        onOpenChange={(nextOpen) => {
          setIsOpen(nextOpen);
          if (!nextOpen) {
            setQuery("");
            setExpandedHarnessKey(null);
          }
        }}
      >
        <DialogContent className="flex h-[min(620px,calc(100vh-40px))] max-h-[calc(100vh-40px)] w-[min(720px,calc(100vw-32px))] max-w-none grid-rows-none flex-col gap-0 overflow-hidden p-0">
          <DialogHeader className="shrink-0 border-b border-[var(--border-subtle)] px-5 py-4 pr-12">
            <DialogTitle className="text-xl">Choose model</DialogTitle>
            <DialogDescription>
              Choose a profile, then pick the model for this conversation.
            </DialogDescription>
          </DialogHeader>

          <div className="shrink-0 border-b border-[var(--border-subtle)] px-5 py-3">
            <div className="flex h-10 items-center gap-2 rounded-md border border-[var(--border-subtle)] bg-[var(--field-bg)] px-3 focus-within:border-[var(--field-border-focus)]">
              <Search className="size-4 shrink-0 text-[var(--text-tertiary)]" />
              <input
                value={query}
                onChange={(event) => setQuery(event.target.value)}
                placeholder="Search Agent Runtime or model"
                className="lemma-assistant-runtime-search-field inline-edit-field h-full min-w-0 flex-1 bg-transparent text-sm text-[var(--text-primary)] outline-none placeholder:text-[var(--text-tertiary)]"
              />
            </div>
          </div>

          <div className="min-h-0 flex-1 overflow-y-auto px-5 py-4">
            <div className="space-y-3">
              <AssistantRuntimeChoiceRow
                title={typeof autoLabel === "string" ? autoLabel : "Auto"}
                subtitle="Use the pod default model"
                selected={!value && !runtime}
                onClick={() => handleSelect(null, null)}
              />

              {filteredGroups.map((group) => (
                <AssistantHarnessRuntimeGroup
                  key={group.key}
                  group={group}
                  expanded={expandedHarnessKey === group.key || query.trim().length > 0}
                  selectedKey={selectedKey}
                  onToggle={() => setExpandedHarnessKey((current) => current === group.key ? null : group.key)}
                  onSelect={(option, optionRuntime) => handleSelect(option.id, optionRuntime)}
                />
              ))}

              {!filteredGroups.length ? (
                <div className="rounded-md border border-[var(--border-subtle)] bg-[var(--surface-1)] px-3 py-3 text-sm text-[var(--text-secondary)]">
                  No models match that search.
                </div>
              ) : null}
            </div>
          </div>
        </DialogContent>
      </Dialog>
    </div>
  );
});

function AssistantRuntimeChoiceRow({
  title,
  subtitle,
  selected,
  onClick,
}: {
  title: string;
  subtitle?: string | null;
  selected: boolean;
  onClick: () => void;
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      className={cn(
        "lemma-assistant-runtime-choice-button flex min-h-11 w-full items-center gap-3 rounded-md px-3 py-2 text-left transition-colors hover:bg-[var(--surface-2)]",
        selected && "bg-[var(--action-primary-soft)] text-[var(--text-primary)]",
      )}
    >
      <span className="min-w-0 flex-1">
        <span className="block truncate text-sm font-medium leading-5 text-[var(--text-primary)]">{title}</span>
        {subtitle ? (
          <span className="block truncate text-xs leading-4 text-[var(--text-tertiary)]">{subtitle}</span>
        ) : null}
      </span>
      <span
        className={cn(
          "flex size-[18px] shrink-0 items-center justify-center rounded-full border",
          selected
            ? "border-[var(--action-primary)] bg-[var(--action-primary)] text-[var(--text-on-brand)]"
            : "border-[var(--border-subtle)] text-transparent",
        )}
      >
        <Check className="size-3.5" />
      </span>
    </button>
  );
}

function AssistantHarnessRuntimeGroup({
  group,
  expanded,
  selectedKey,
  onToggle,
  onSelect,
}: {
  group: AssistantRuntimeGroup;
  expanded: boolean;
  selectedKey: string;
  onToggle: () => void;
  onSelect: (option: AvailableModelInfo, runtime: AgentRuntimeConfig | null) => void;
}) {
  const logo = group.harnessKind ? HARNESS_LOGOS[group.harnessKind] : undefined;
  const groupIsSelected = group.options.some((option) => {
    const runtime = modelRuntime(option);
    return runtime ? assistantRuntimeKey(runtime) === selectedKey : option.id === selectedKey;
  });
  const selectedOption = group.options.find((option) => {
    const runtime = modelRuntime(option);
    return runtime ? assistantRuntimeKey(runtime) === selectedKey : option.id === selectedKey;
  });
  const selectedRuntime = selectedOption ? modelRuntime(selectedOption) : null;

  return (
    <section
      className={cn(
        "overflow-hidden rounded-md border bg-[var(--surface-1)] transition-colors",
        groupIsSelected ? "border-[var(--field-border-focus)]" : "border-[var(--border-subtle)]",
      )}
    >
      <button
        type="button"
        onClick={onToggle}
        className="lemma-assistant-runtime-group-button flex min-h-16 w-full items-center gap-3 px-3 py-3 text-left transition-colors hover:bg-[var(--surface-2)]"
        aria-expanded={expanded}
      >
        <span className="flex size-10 shrink-0 items-center justify-center rounded-md border border-[var(--border-subtle)] bg-[var(--card-bg)]">
          {logo ? (
            <Image
              src={logo}
              alt=""
              width={24}
              height={24}
              className="size-6 object-contain"
            />
          ) : (
            <Bot className="size-5 text-[var(--text-tertiary)]" />
          )}
        </span>
        <span className="min-w-0 flex-1">
          <span className="flex items-center gap-2">
            <span className="truncate text-sm font-semibold text-[var(--text-primary)]">{group.displayName}</span>
            {groupIsSelected ? (
              <span className="rounded-md bg-[var(--action-primary-soft)] px-1.5 py-0.5 text-xs font-medium text-[var(--action-primary)]">
                Selected
              </span>
            ) : null}
          </span>
          <span className="mt-0.5 block truncate text-xs text-[var(--text-tertiary)]">
            {selectedRuntime?.model_name
              ? shortAssistantModelName(selectedRuntime.model_name)
              : `${group.options.length} model${group.options.length === 1 ? "" : "s"}`}
          </span>
        </span>
        <ChevronDown
          className={cn(
            "size-4 shrink-0 text-[var(--text-tertiary)] transition-transform",
            expanded && "rotate-180",
          )}
        />
      </button>

      {expanded ? (
        <div className="border-t border-[var(--border-subtle)] bg-[var(--surface-2)] p-1.5">
          {group.options.map((option) => {
            const runtime = modelRuntime(option);
            const modelName = runtime?.model_name ?? option.name ?? option.id;
            const hint = assistantModelPathHint(modelName);
            const optionKey = runtime ? assistantRuntimeKey(runtime) : option.id;
            return (
              <AssistantRuntimeChoiceRow
                key={optionKey}
                title={shortAssistantModelName(modelName)}
                subtitle={hint}
                selected={selectedKey === optionKey}
                onClick={() => onSelect(option, runtime)}
              />
            );
          })}
        </div>
      ) : null}
    </section>
  );
}

export interface AssistantPendingFileChipProps extends ComponentPropsWithoutRef<"div"> {
  label: ReactNode;
  onRemove?: () => void;
  radius?: LemmaAssistantRadius;
}

export interface AssistantComposerProps extends ComponentPropsWithoutRef<"div"> {
  floating?: ReactNode;
  status?: ReactNode;
  pendingFiles?: ReactNode;
  children: ReactNode;
  innerClassName?: string;
  tone?: AssistantSurfaceTone;
  radius?: LemmaAssistantRadius;
  compact?: boolean;
}

export const AssistantComposer = forwardRef<HTMLDivElement, AssistantComposerProps>(function AssistantComposer({
  floating,
  status,
  pendingFiles,
  children,
  innerClassName,
  tone = "subtle",
  radius = "lg",
  compact = false,
  className,
  ...props
}, ref) {
  return (
    <div
      ref={ref}
      data-tone={tone}
      data-has-status={status ? "true" : "false"}
      data-has-pending-files={pendingFiles ? "true" : "false"}
      data-has-floating={floating ? "true" : "false"}
      className={cn(
        "lemma-assistant-composer flex shrink-0 flex-col border-t border-transparent",
        compact ? "gap-1.5 px-3 py-2" : "gap-2 px-4 pb-3 pt-2 sm:px-6",
        tone === "default" && "bg-[var(--bg-canvas)]",
        tone === "subtle" && "bg-transparent",
        tone === "flat" && "border-transparent bg-transparent",
        assistantRadius(radius, "shell"),
        className,
      )}
      {...props}
    >
      {floating ? (
        <div className={cn("mx-auto flex w-full min-w-0 flex-wrap items-center gap-2", innerClassName)}>
          {floating}
        </div>
      ) : null}

      {status ? (
        <div className={cn("mx-auto min-h-6 w-full", innerClassName)} data-has-status="true">
          <div className="flex flex-wrap items-center gap-2">
            {status}
          </div>
        </div>
      ) : (
        <div className="min-h-0" data-has-status="false" />
      )}

      {pendingFiles ? (
        <div className={cn("mx-auto flex w-full flex-wrap gap-1.5", innerClassName)}>
          {pendingFiles}
        </div>
      ) : null}

      <div className={cn("mx-auto w-full min-w-0", innerClassName)}>{children}</div>
    </div>
  );
});

export const AssistantPendingFileChip = forwardRef<HTMLDivElement, AssistantPendingFileChipProps>(function AssistantPendingFileChip({
  label,
  onRemove,
  radius = "lg",
  className,
  ...props
}, ref) {
  return (
    <Badge
      ref={ref}
      variant="default"
      className={cn(
        "lemma-assistant-presented-file-badge inline-flex h-6 max-w-full items-center gap-1.5 px-2 text-xs",
        assistantRadius(radius, "inline"),
        className,
      )}
      {...props}
    >
      <span className="truncate">{label}</span>
      {onRemove ? (
        <button
          type="button"
          onClick={onRemove}
          className="lemma-assistant-file-remove-button inline-flex size-4 items-center justify-center rounded-sm text-[var(--text-secondary)] transition-colors hover:bg-[color:color-mix(in_srgb,var(--surface-2)_80%,transparent)] hover:text-[var(--text-primary)]"
          title="Remove file"
        >
          <X className="size-3" />
        </button>
      ) : null}
    </Badge>
  );
});

export interface AssistantStatusPillProps extends ComponentPropsWithoutRef<"div"> {
  label: ReactNode;
  subtle?: boolean;
  radius?: LemmaAssistantRadius;
}

export const AssistantStatusPill = forwardRef<HTMLDivElement, AssistantStatusPillProps>(function AssistantStatusPill({
  label,
  subtle = false,
  radius = "lg",
  className,
  ...props
}, ref) {
  void radius;

  return (
    <div
      ref={ref}
      className={cn(
        "inline-flex min-h-6 max-w-full items-center gap-2 px-1 py-0.5 text-sm text-[var(--text-secondary)] transition-colors",
        !subtle && "lemma-assistant-text-primary-soft",
        className,
      )}
      {...props}
    >
      <span className="relative flex size-2 shrink-0" aria-hidden="true">
        <span className="absolute inset-0 animate-ping rounded-full bg-[var(--action-primary)] opacity-30" />
        <span className="relative size-2 rounded-full bg-[var(--action-primary)]" />
      </span>
      <span className="truncate">{label}</span>
    </div>
  );
});
