import { describe, expect, it, vi } from "vitest";
import type { LemmaClient } from "../client.js";
import {
  WorkflowController,
  buildWorkflowFormSubmit,
  getRunInputFields,
  selectWorkflowOutputs,
  shouldPollWorkflowRun,
} from "../core/workflow/index.js";

interface Handlers {
  create?: (name: string) => unknown;
  get?: (id: string) => unknown;
  submitForm?: (id: string, body: unknown) => unknown;
  list?: (name: string) => unknown;
  cancel?: (id: string) => unknown;
}

function fakeWorkflowClient(handlers: Handlers): LemmaClient {
  const runs = {
    create: async (name: string) => handlers.create?.(name) ?? { id: "run-1", status: "RUNNING" },
    get: async (id: string) => handlers.get?.(id) ?? { id, status: "RUNNING" },
    submitForm: async (id: string, body: unknown) =>
      handlers.submitForm?.(id, body) ?? { id, status: "RUNNING" },
    list: async (name: string) => handlers.list?.(name) ?? { items: [], next_page_token: null },
    cancel: async (id: string) => handlers.cancel?.(id),
  };
  return {
    podId: "pod-1",
    withPod() {
      return this as unknown as LemmaClient;
    },
    workflows: { runs },
  } as unknown as LemmaClient;
}

describe("WorkflowController", () => {
  it("start + connect resolves the run and outputs", async () => {
    const controller = new WorkflowController({
      client: fakeWorkflowClient({
        create: () => ({ id: "run-1", status: "RUNNING", active_wait: null }),
        get: () => ({ id: "run-1", status: "COMPLETED", execution_context: { result: 42 } }),
      }),
      scope: { podId: "pod-1", flowName: "wf" },
      autoPoll: false,
    });

    const created = await controller.start();
    expect(created.id).toBe("run-1");

    const state = controller.getState();
    expect(state.runId).toBe("run-1");
    expect(state.status).toBe("COMPLETED");
    expect(state.isPolling).toBe(false);

    const outputs = selectWorkflowOutputs(state.run);
    expect(outputs.isFinished).toBe(true);
    expect(outputs.output).toEqual({ result: 42 });
  });

  it("polls until terminal status then stops", async () => {
    const controller = new WorkflowController({
      client: fakeWorkflowClient({
        create: () => ({ id: "run-1", status: "RUNNING" }),
        get: () => ({ id: "run-1", status: "COMPLETED" }),
      }),
      scope: { podId: "pod-1", flowName: "wf" },
      autoPoll: true,
      pollIntervalMs: 5,
    });

    await controller.start();
    await vi.waitFor(() => {
      expect(controller.getState().isPolling).toBe(false);
    });
    expect(controller.getState().status).toBe("COMPLETED");
  });

  it("resume submits the active form", async () => {
    let submitted: unknown = null;
    const controller = new WorkflowController({
      client: fakeWorkflowClient({
        get: () => ({
          id: "run-1",
          status: "WAITING",
          active_wait: { wait_type: "HUMAN", node_id: "form1" },
        }),
        submitForm: (_id, body) => {
          submitted = body;
          return { id: "run-1", status: "RUNNING" };
        },
      }),
      scope: { podId: "pod-1", flowName: "wf" },
      autoPoll: false,
      initialRunId: "run-1",
    });

    const resumed = await controller.resume({ inputs: { name: "x" }, connect: false });
    expect(resumed.status).toBe("RUNNING");
    expect(controller.getState().status).toBe("RUNNING");
    expect(submitted).toEqual({ node_id: "form1", inputs: { name: "x" } });
  });

  it("setRunId(null) resets the run", async () => {
    const controller = new WorkflowController({
      client: fakeWorkflowClient({ get: () => ({ id: "run-1", status: "COMPLETED" }) }),
      scope: { podId: "pod-1" },
      autoPoll: false,
      initialRunId: "run-1",
    });

    await controller.refresh("run-1");
    expect(controller.getState().run).not.toBeNull();

    controller.setRunId(null);
    const state = controller.getState();
    expect(state.runId).toBeNull();
    expect(state.run).toBeNull();
    expect(state.status).toBeUndefined();
  });
});

describe("workflow helpers", () => {
  const waiting = {
    id: "run-1",
    status: "WAITING",
    active_wait: {
      wait_type: "HUMAN",
      node_id: "form1",
      payload: {
        input_schema: {
          type: "object",
          properties: { name: { type: "string" } },
          required: ["name"],
        },
      },
    },
  } as never;

  it("getRunInputFields derives fields from the active form schema", () => {
    const fields = getRunInputFields(waiting);
    expect(fields).toHaveLength(1);
    expect(fields[0]?.name).toBe("name");
    expect(getRunInputFields({ id: "x", status: "RUNNING" } as never)).toEqual([]);
  });

  it("shouldPollWorkflowRun skips terminal and human-wait runs", () => {
    expect(shouldPollWorkflowRun({ status: "RUNNING" } as never)).toBe(true);
    expect(shouldPollWorkflowRun({ status: "COMPLETED" } as never)).toBe(false);
    expect(shouldPollWorkflowRun(waiting)).toBe(false);
  });

  it("selectWorkflowOutputs flags a human wait", () => {
    const outputs = selectWorkflowOutputs(waiting);
    expect(outputs.isWaitingForInput).toBe(true);
    expect(outputs.isFinished).toBe(false);
  });

  it("buildWorkflowFormSubmit targets the wait node with collected inputs", () => {
    expect(buildWorkflowFormSubmit(waiting, { name: "x" })).toEqual({
      nodeId: "form1",
      inputs: { name: "x" },
    });
    expect(buildWorkflowFormSubmit({ id: "r", status: "RUNNING" } as never)).toBeNull();
  });
});
