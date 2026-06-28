export const podBlocks = [
  {
    key: "data",
    title: "Data Stores",
    icon: "/landing-page/pod-icons/data.svg",
    stat: "5 typed tables",
    summary:
      "Structured business data created by the pod and ingested from external sources.",
    detail:
      "Pull from SQL databases, REST APIs, or SaaS apps. Lemma stores it in typed tables. Your leads, tickets, events, and pipeline records are readable by agents, queryable by your app, and owned by the pod.",
  },
  {
    key: "agents",
    title: "Agents",
    icon: "/landing-page/pod-icons/agents.svg",
    stat: "4 active agents",
    summary: "LLM workers that execute judgment tasks inside the pod.",
    detail:
      "Each agent receives a role, input schema, tool grants, accessible tables, folders, and connected apps - never vague access to everything. Results come back as structured data before a workflow or human reviewer decides what happens next.",
  },
  {
    key: "workflows",
    title: "Workflows",
    icon: "/landing-page/pod-icons/workflows.svg",
    stat: "8 workflow graphs",
    summary:
      "Real business processes with agents, humans, approvals, and handoffs.",
    detail:
      "Workflows mix forms, agents, functions, decisions, waits, loops, and approval steps. The same graph can start from a schedule, a Slack action, a new record, a webhook, or a button in the app.",
  },
  {
    key: "apps",
    title: "App Interface",
    icon: "/landing-page/pod-icons/apps.svg",
    stat: "2 operator apps",
    summary: "The operator UI your team runs on, deployed at a URL.",
    detail:
      "Real multi-screen apps, not screenshots - record tables, detail pages, workflow launch forms, review queues, and embedded assistants, all built on the same pod APIs.",
  },
  {
    key: "access",
    title: "RBAC + Auth",
    icon: "/landing-page/pod-icons/auth-rbac.svg",
    stat: "People + agent grants",
    summary: "Roles decide what people and agents can access or change.",
    detail:
      "Pod roles, table grants, resource visibility, and approval policies decide who can view data, change records, run workflows, or let an agent take an external action.",
  },
  {
    key: "connectors",
    title: "Connectors",
    icon: "/landing-page/pod-icons/connectors.svg",
    stat: "4 connected",
    summary: "Connect the pod to tools your team already uses.",
    detail:
      "Gmail, Slack, GitHub, Salesforce, Teams, and custom APIs can be called by functions, workflows, and agents - using the current user's account or a fixed service account, per the pod's rules.",
  },
] as const;

export const surfaceModes = [
  {
    key: "slack",
    label: "Slack",
    caption: "Approvals in channel",
    logos: [{ src: "/landing-page/app-logos/slack.svg", label: "Slack" }],
    headline: "Slack approvals, no extra tab.",
    body: "When a lead like Northwind crosses the line, the approval lands in #sales. Dana approves without leaving Slack - Lemma routes the lead, updates the record, and logs the decision.",
    footnote:
      "Slack is just the surface. The workflow, data, approvals, and connectors live in Lemma.",
  },
  {
    key: "email",
    label: "Gmail",
    caption: "Inbox approvals",
    logos: [{ src: "/landing-page/app-logos/gmail.svg", label: "Gmail" }],
    headline: "Gmail approvals, no inbox sprawl.",
    body: "An email arrives, Lemma drafts the reply from pod context, waits for approval, sends it, and keeps the customer record current.",
    footnote:
      "Gmail is just the surface. Lemma keeps the customer record, workflow state, and approval trail together.",
  },
  {
    key: "outlook",
    label: "Outlook",
    caption: "Mailbox triage",
    logos: [{ src: "/landing-page/app-logos/outlook.svg", label: "Outlook" }],
    headline: "Outlook triage, no manual follow-up.",
    body: "Mailbox threads become structured review work: classify the request, draft the answer, ask the owner, and log the final update.",
    footnote:
      "Outlook is just the surface. The same pod owns the workflow, data updates, and audit trail.",
  },
  {
    key: "teams",
    label: "Teams",
    caption: "Microsoft workspaces",
    logos: [
      { src: "/landing-page/app-logos/teams.svg", label: "Microsoft Teams" },
    ],
    headline: "Teams decisions, no extra dashboard.",
    body: "Lemma can post the summary, collect the decision, route the handoff, and keep Microsoft workspace activity tied to pod state.",
    footnote:
      "Teams is just the surface. The pod still owns the workflow, permissions, and data updates.",
  },
  {
    key: "telegram",
    label: "Telegram",
    caption: "Fast approvals",
    logos: [{ src: "/landing-page/app-logos/telegram.svg", label: "Telegram" }],
    headline: "Telegram approvals, not the system.",
    body: "A quick message can trigger a workflow, ask for the missing decision, and confirm the exact operational change back in chat.",
    footnote:
      "Telegram is just the surface. The pod still decides what changes, who can approve, and what gets logged.",
  },
  {
    key: "whatsapp",
    label: "WhatsApp",
    caption: "Mobile handoffs",
    logos: [{ src: "/landing-page/app-logos/whatsapp.svg", label: "WhatsApp" }],
    headline: "WhatsApp handoffs, without lost state.",
    body: "Field updates, lead routing, and status confirmations can happen on mobile while Lemma keeps ownership and records clean.",
    footnote:
      "WhatsApp is just the surface. The pod still decides what changes, who can approve, and what gets logged.",
  },
  {
    key: "api",
    label: "App + API",
    caption: "Your UI and backend",
    logos: [{ src: "/landing-page/app-logos/api.svg", label: "API" }],
    headline: "API triggers, without custom glue.",
    body: "Use your own UI, webhook, or backend call as the entry point. The same agents, workflows, data, and approvals run behind it.",
    footnote:
      "The API is just the surface. Lemma is the system behind the action.",
  },
] as const;

export type SurfaceMode = (typeof surfaceModes)[number];

export const showcaseCards = [
  {
    tag: "Sales",
    claim: "Automated the entire top of funnel. No SDR. No spreadsheet.",
    flow: "Lead captured -> agent scores ICP -> routed to rep -> sequence drafted -> reply tracked",
  },
  {
    tag: "Support",
    claim: "200 support tickets a day. Zero support hires.",
    flow: "Email arrives -> agent classifies and drafts -> human reviews -> approved -> sent and logged",
  },
  {
    tag: "RevOps",
    claim: "Revenue forecasts that update themselves. Every week.",
    flow: "CRM synced -> agent models pipeline -> forecast updated -> exceptions flagged -> reviewed in app",
  },
  {
    tag: "Finance",
    claim: "Recovered $40k in overdue invoices without awkward emails.",
    flow: "Invoice due -> reminder drafted -> sent via Gmail -> status updated -> escalated if needed",
  },
  {
    tag: "Content",
    claim: "One input. Five content outputs. Twenty minutes of your time.",
    flow: "Topic entered -> sources pulled -> drafts written -> queued for approval -> published",
  },
] as const;

export const githubUrl = "https://github.com/lemma-work/lemma-platform";

export const machineStations = [
  {
    key: "inbound",
    label: "INBOUND",
    sub: "ST/01",
    caption: "Email from Northwind hits the pod inbox.",
  },
  {
    key: "agent",
    label: "AGENT:QUILL",
    sub: "ST/02",
    caption: "Quill parses intent and drafts the lead record.",
  },
  {
    key: "table",
    label: "TABLE:LEADS",
    sub: "ST/03",
    caption: "Row written, row-level security applied.",
  },
  {
    key: "approval",
    label: "HUMAN:APPROVAL",
    sub: "ST/04",
    caption: "The gate pauses the work for a person.",
  },
  {
    key: "routed",
    label: "ROUTED",
    sub: "ST/05",
    caption: "Owner assigned. State updated for everyone.",
  },
] as const;

export const heroTickerEvents = [
  "lead northwind.com hit the inbox",
  "quill scored it 87 · qualified",
  "row written to leads · rls applied",
  "approval sent to #sales on slack",
  "dana approved · routed to enterprise",
] as const;

export const terminalScript = [
  { command: "uv tool install lemma-terminal", output: [] },
  { command: "lemma pods create support-ops", output: [] },
  { command: "lemma pods import ./support-inbox", output: [] },
  {
    command: "lemma apps deploy support-ops",
    output: [
      "",
      "Created pod: support-ops",
      "Tables: tickets, customers, approvals",
      "Agents: classifier, draft-writer, policy-checker",
      "App: https://support-ops.lemma.work",
    ],
  },
] as const;

export type TerminalLine = { kind: "command" | "output"; text: string };

export const fullTerminalLines: TerminalLine[] = terminalScript.flatMap((step) => [
  { kind: "command" as const, text: step.command },
  ...step.output.map((text) => ({ kind: "output" as const, text })),
]);
