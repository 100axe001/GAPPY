# Recipe — a workflow inbox (FORM waits)

Show the human half of a workflow: FORM nodes parked waiting on the signed-in
member, rendered as forms they submit to advance the run. (← `apps.md`)

## The model

A workflow `FORM` node creates a **wait** assigned to a pod member. Until they
submit, the run is parked. Each assignment is `{ run, wait }`: `run.id` is the run,
`wait.node_id` is the form node, and `wait.input_schema` is the form to render.
Submitting resumes the run.

## Inbox + submit

```tsx
import { useWorkflowRunWaitAssignments, useWorkflowResume } from "lemma-sdk/react";

// FORM waits assigned to the current member:
const { assignments, isLoading, reload } =
  useWorkflowRunWaitAssignments({ client, podId: client.podId });

const { resume } = useWorkflowResume({ client, podId: client.podId });

// render assignment.wait.input_schema as fields, then on submit:
await resume(formValues, { runId: assignment.run.id, nodeId: assignment.wait.node_id });
// formValues are the submitted field values; the run advances past the FORM node.
```

## Render the form from its schema

Use the **`<WorkflowForm>`** preset (it binds a parked run to its fields + a submit;
`children` receives the bound form state), or render `wait.input_schema` yourself
with `useSchemaForm`/`useWorkflowForm` and call `resume(...)`:

```tsx
import { WorkflowForm } from "lemma-sdk/react";

<WorkflowForm client={client} podId={client.podId} runId={run.id} nodeId={wait.node_id}>
  {(f) => <Fields schema={f.schema} values={f.values} onChange={f.set} onSubmit={f.submit} />}
</WorkflowForm>
```

## Make the work visible

Pair the inbox with run status so operators see *where* a process is stuck: show
`useWorkflowRun` (current node label, status) and `useFlowRunHistory` (step
history) next to the form. This is the app side of human-agent collaboration —
don't hide waits in logs.

> Exact fields: `cat /sdk/lemma-typescript/src/react/{useWorkflowRunWaitAssignments,useWorkflowForm,useWorkflowResume}.ts`.
