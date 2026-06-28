# Recipe — a table with live auto-refresh

Read and mutate a table; a local write auto-refreshes the list, and a WebSocket keeps it
live across *other* users' / workloads' changes — no polling. (← `apps.md`)

## What RLS does here

The app runs as the signed-in user (see `pod-model.md`). On an **RLS-on** table the
hooks return **only that user's rows**; on a **shared** table they return the
team's rows. You never filter by `user_id` — the backend scopes it.

## Read + filter + sort (hand-written hook)

```tsx
import { useRecords } from "lemma-sdk/react";

const { records, isLoading, error, loadMore, hasMore } = useRecords({
  client, podId: client.podId, tableName: "tickets", limit: 50,
  filters: [{ field: "status", op: "eq", value: "waiting_approval" }],
  sort:    [{ field: "created_at", direction: "desc" }],
});
```

## CRUD with auto-refresh (generated hooks)

For plain create/read/update/delete, prefer the **generated** TanStack-Query hooks
(`use<Resource>List/Get/Create/Update/Delete`) — a write **auto-invalidates the
matching list**, so the UI updates itself. They need a `QueryClientProvider` (the
scaffold mounts one).

```tsx
import { useRecordList, useRecordCreate, useRecordUpdate } from "lemma-sdk/react";

const list   = useRecordList(client, client.podId, "tickets");          // cached + deduped
const create = useRecordCreate(client, client.podId);
const update = useRecordUpdate(client, client.podId);

create.mutate({ tableName: "tickets", payload: { title: "New ticket", status: "open" } });
// `list` refreshes automatically on success — no refetch wiring.
update.mutate({ tableName: "tickets", recordId, payload: { status: "done" } });
```

Use the hand-written `useRecords` (with `loadMore`) / `useRecordForm` when you need
their richer ergonomics; use the generated hooks when you just want correct CRUD.

## Live updates (subscribe, don't poll)

Two different things keep a list fresh — never a timer:

- **Your own writes** auto-invalidate the matching list via the generated CRUD hooks
  above (TanStack-Query). That covers changes *this* client makes.
- **Other users' / workloads' changes** arrive over the **table WebSocket**. Prefer
  **`useLiveRecords`** — same options as `useRecords`, but it merges insert/update/delete
  deltas **in place** (no flicker, no refetch):

```tsx
import { useLiveRecords } from "lemma-sdk/react";   // SDK ≥ 0.4.1

const { records, isLoading, liveStatus } = useLiveRecords({
  client, podId: client.podId, tableName: "tickets",
  sort: [{ field: "created_at", direction: "desc" }],
});
// render with a stable key={r.id} — rows update in place as the pod changes.
```

Filtered views: the stream carries every change you can *see*, so under the default
`reconcile: "merge"` a new row that doesn't match your `filters` could appear. Keep it
exact with a predicate, or an event-driven refetch:

```tsx
useLiveRecords({ client, tableName: "tickets",
  filters: [{ field: "status", op: "eq", value: "open" }],
  accept: (r) => r.status === "open",   // drop rows that leave the view
  // — or — reconcile: "refetch",        // re-run the query on each change (debounced)
});
```

On the **HTML / no-React path** (or to drive your own state), use the imperative stream
and merge by `record_id`, closing it on teardown:

```js
const rows = new Map();   // id -> row
const handle = client.datastore.watchChanges({
  table: "tickets",
  onChange: (f) => {
    if (f.operation === "delete") rows.delete(f.record_id);
    else rows.set(f.record_id, { ...rows.get(f.record_id), ...f.payload, id: f.record_id });
    render([...rows.values()]);
  },
});
// later: handle.close();
```

Never `setInterval(refetch)` — polling flickers and hammers the API (pod-model
heuristic #4: *never poll a table*).

## Aggregates / cross-table

`useDatastoreQuery(client, podId, sql)` runs a single read-only `SELECT` (RLS still
applies) for counts, group-bys, and joins the record hooks don't cover.

> Exact return fields: `cat /sdk/lemma-typescript/src/react/useRecords.ts` and
> `src/react/generated/records.ts`.
