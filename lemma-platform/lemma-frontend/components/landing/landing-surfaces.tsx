import Image from "next/image";
import type { CSSProperties, MouseEvent, TouchEvent } from "react";
import { useState } from "react";
import type { SurfaceMode } from "./landing-data";

export function SurfacePreview({ surface }: { surface: SurfaceMode }) {
  const isMail = surface.key === "email" || surface.key === "outlook";
  const isPhone = surface.key === "telegram" || surface.key === "whatsapp";
  const isWorkspace = surface.key === "slack" || surface.key === "teams";
  const sidebarItems =
    surface.key === "teams"
      ? ["Activity", "Approvals", "Campaigns", "Files"]
      : ["# approvals", "# support-triage", "# customer-escalations", "Apps"];

  if (isPhone) {
    return (
      <aside
        className={`lp-surface-preview is-${surface.key}`}
        aria-label={`${surface.label} surface preview`}
      >
        <div className="lp-surface-window lp-phone-window">
          <SurfacePhoneContent surface={surface} />
        </div>
        <p className="lp-surface-footnote">{surface.footnote}</p>
      </aside>
    );
  }

  if (isMail) {
    return (
      <aside
        className={`lp-surface-preview is-${surface.key}`}
        aria-label={`${surface.label} surface preview`}
      >
        <div className="lp-surface-window lp-mail-window">
          <header className="lp-surface-window-top">
            <span className="lp-surface-brand">
              <Image
                src={surface.logos[0].src}
                alt={surface.logos[0].label}
                width={24}
                height={24}
              />
              <strong>{surface.label}</strong>
            </span>
            <span className="lp-surface-search">Search customer threads</span>
            <Image
              className="lp-surface-avatar"
              src="/landing-page/slack-profile-avatar.jpg"
              alt=""
              width={30}
              height={30}
            />
          </header>
          <div className="lp-mail-window-body">
            <SurfaceEmailContent surface={surface} />
          </div>
        </div>
        <p className="lp-surface-footnote">{surface.footnote}</p>
      </aside>
    );
  }

  if (!isWorkspace) {
    return (
      <aside
        className={`lp-surface-preview is-${surface.key}`}
        aria-label={`${surface.label} surface preview`}
      >
        <div className="lp-surface-window lp-api-window">
          <header className="lp-surface-window-top">
            <span className="lp-surface-brand">
              <Image
                src={surface.logos[0].src}
                alt={surface.logos[0].label}
                width={24}
                height={24}
              />
              <strong>API</strong>
            </span>
            <span className="lp-surface-search">support-ops.lemma.work</span>
            <Image
              className="lp-surface-avatar"
              src="/landing-page/slack-profile-avatar.jpg"
              alt=""
              width={30}
              height={30}
            />
          </header>
          <div className="lp-surface-thread">
            <div className="lp-surface-thread-head">
              <strong>POST /workflow.run</strong>
              <span>{surface.caption}</span>
            </div>
            <SurfaceApiContent />
          </div>
        </div>
        <p className="lp-surface-footnote">{surface.footnote}</p>
      </aside>
    );
  }

  return (
    <aside
      className={`lp-surface-preview is-${surface.key}`}
      aria-label={`${surface.label} surface preview`}
    >
      <div className="lp-surface-window">
        <header className="lp-surface-window-top">
          <span className="lp-surface-brand">
            {surface.logos.map((logo) => (
              <Image
                key={logo.label}
                src={logo.src}
                alt={logo.label}
                width={24}
                height={24}
              />
            ))}
            <strong>{surface.label}</strong>
          </span>
          <span className="lp-surface-search">Search Lemma Ops</span>
          <Image
            className="lp-surface-avatar"
            src="/landing-page/slack-profile-avatar.jpg"
            alt=""
            width={30}
            height={30}
          />
        </header>

        <div className="lp-surface-window-body">
          <div className="lp-surface-sidebar" aria-hidden="true">
            {sidebarItems.map((item, index) => (
              <span className={index === 0 ? "is-selected" : ""} key={item}>
                {item}
              </span>
            ))}
          </div>

          <div className="lp-surface-thread">
            <div className="lp-surface-thread-head">
              <strong>@Lemma</strong>
              <span>{surface.caption}</span>
            </div>

            <SurfaceChatContent surface={surface} />
          </div>
        </div>
      </div>
      <p className="lp-surface-footnote">{surface.footnote}</p>
    </aside>
  );
}

export function StackComparison({
  value,
  onChange,
}: {
  value: number;
  onChange: (value: number) => void;
}) {
  const minSplit = 42;
  const maxSplit = 96;
  const [isMouseDown, setIsMouseDown] = useState(false);
  const compareStyle = {
    "--lp-stack-split": `${value}%`,
  } as CSSProperties;

  const onMouseMove = (
    event: MouseEvent<HTMLDivElement> | TouchEvent<HTMLDivElement>,
  ) => {
    if (!isMouseDown) return;

    const rect = event.currentTarget.getBoundingClientRect();
    let x = 0;

    if ("touches" in event && event.touches.length > 0) {
      x = event.touches[0].clientX - rect.left;
    } else if ("clientX" in event) {
      x = event.clientX - rect.left;
    }

    onChange(Math.min(maxSplit, Math.max(minSplit, (x / rect.width) * 100)));
  };

  return (
    <div
      className="lp-stack-compare-shell"
      aria-label="Compare stitched AI stack with Lemma"
      /* eslint-disable-next-line no-restricted-syntax -- Runtime slider geometry is scoped to one CSS variable. */
      style={compareStyle}
      onMouseMove={onMouseMove}
      onMouseUp={() => setIsMouseDown(false)}
      onMouseLeave={() => setIsMouseDown(false)}
      onTouchMove={onMouseMove}
      onTouchEnd={() => setIsMouseDown(false)}
    >
      <div className="lp-stack-layer lp-stack-layer-stitched">
        <div className="lp-stack-layer-copy">
          <span className="lp-stack-pill">Workshop -&gt; Workspace</span>
          <h2 id="stack-title">The Stack, Without the Stitching</h2>
          <p>
            Every serious AI work system needs agents, workflows, data,
            connectors, UI, permissions, observability, and deployment. Lemma
            gives you that system shape out of the box.
          </p>
        </div>

        <div className="lp-stack-stage is-stitched">
          <span>Messy stitching across 8+ tools</span>
          <Image
            className="lp-stack-stage-image"
            src="/landing-page/stack-compare/stitched-stack.png"
            alt="A stitched AI system made from separate tools and glue code"
            width={1448}
            height={1086}
          />
        </div>
      </div>

      <div className="lp-stack-layer lp-stack-layer-lemma">
        <div className="lp-stack-layer-copy is-lemma-copy">
          <span className="lp-stack-pill">Lemma stack</span>
          <h2>Lemma is the stack.</h2>
          <p>Same system shape, without rebuilding the rails every time.</p>
        </div>

        <div className="lp-stack-stage is-lemma">
          <span>One coherent Lemma workspace</span>
          <Image
            className="lp-stack-stage-image"
            src="/landing-page/stack-compare/lemma-stack.png"
            alt="Lemma showing agents, workflows, data stores, connectors, UI, permissions, observability, and deployment in one stack"
            width={1448}
            height={1086}
            priority={false}
          />
        </div>
      </div>

      <div className="lp-stack-divider">
        <button
          type="button"
          aria-label="Drag to compare stitched stack and Lemma stack"
          onMouseDown={() => {
            setIsMouseDown(true);
          }}
          onMouseUp={() => setIsMouseDown(false)}
          onTouchStart={() => {
            setIsMouseDown(true);
          }}
          onTouchEnd={() => setIsMouseDown(false)}
        >
          <i />
          <i />
          <i />
        </button>
      </div>
    </div>
  );
}

export function SurfaceChatContent({ surface }: { surface: SurfaceMode }) {
  const isTeams = surface.key === "teams";

  return (
    <div className="lp-surface-sequence">
      <div className="lp-surface-message is-human is-sequence-1">
        <Image
          src="/landing-page/slack-profile-avatar.jpg"
          alt=""
          width={34}
          height={34}
        />
        <p>
          <strong>{isTeams ? "Ava" : "Dana"}</strong>{" "}
          {isTeams
            ? "Review Q3 campaign spend. Ask before pausing."
            : "Anything waiting on me?"}
        </p>
      </div>
      <div className="lp-surface-message is-lemma is-sequence-2">
        <span>Le</span>
        <p>
          <strong>Lemma</strong>{" "}
          {isTeams
            ? "Checked spend, goals, and permissions. One pause needs approval."
            : "One approval. Northwind crossed the ICP threshold - Quill scored it 87."}
        </p>
      </div>
      <article className="lp-surface-approval is-sequence-3">
        <div>
          <span className="lp-surface-warning">!</span>
          <strong>
            {isTeams ? "Budget review needed" : "Approval needed"}
          </strong>
          <em>{isTeams ? "Quarterly campaign" : "Lead routing"}</em>
        </div>
        <p>
          Lemma checked policy and queued the decision in this{" "}
          {isTeams ? "workspace" : "channel"}.
        </p>
        <blockquote>
          {isTeams
            ? "Pause spend above threshold until Monday and notify finance."
            : "Route Northwind to the enterprise team and assign an owner."}
        </blockquote>
        <div className="lp-surface-actions">
          <span className="is-primary">Approve</span>
          <span>Revise</span>
          <span>Escalate</span>
        </div>
      </article>

      <div className="lp-surface-message is-human is-sequence-4">
        <Image
          src="/landing-page/slack-profile-avatar.jpg"
          alt=""
          width={34}
          height={34}
        />
        <p>
          <strong>{isTeams ? "Ava" : "Dana"}</strong> Approve
        </p>
      </div>
      <div className="lp-surface-message is-lemma is-sequence-5">
        <span>Le</span>
        <p>
          <strong>Lemma</strong>{" "}
          {isTeams
            ? "Done. Spend paused, finance notified, log updated."
            : "Done. Northwind routed, owner assigned, record updated - same state everywhere."}
        </p>
      </div>
    </div>
  );
}

export function SurfaceEmailContent({ surface }: { surface: SurfaceMode }) {
  const isOutlook = surface.key === "outlook";

  return (
    <div
      className={isOutlook ? "lp-email-surface is-outlook" : "lp-email-surface"}
    >
      <nav className="lp-email-rail" aria-hidden="true">
        {(isOutlook ? ["M", "C", "P", "T"] : ["G", "C", "D", "M"]).map(
          (item, index) => (
            <span className={index === 0 ? "is-active" : ""} key={item}>
              {item}
            </span>
          ),
        )}
      </nav>
      <div className="lp-email-list" aria-hidden="true">
        <strong>{isOutlook ? "Focused" : "Primary"}</strong>
        {[
          [
            isOutlook ? "Alex Morgan" : "Support escalation",
            isOutlook
              ? "Invoice #AC-4482 needs exception review"
              : "Refund exception request",
            "Needs approval",
          ],
          ["Operations", "Customer record changed after reply", "Synced"],
          ["Finance Team", "Friday reminder queued for owner", "Scheduled"],
          [
            isOutlook ? "Vendor Mgmt" : "Customer Success",
            isOutlook ? "Payment policy note" : "Implementation follow-up",
            "Logged",
          ],
          [
            isOutlook ? "Priya Shah" : "Maya Chen",
            isOutlook ? "Approval queue review" : "Refund timeline attached",
            "Open",
          ],
        ].map(([from, subject, status], index) => (
          <article className={index === 0 ? "is-selected" : ""} key={subject}>
            <span>
              <strong>{from}</strong>
              <small>{subject}</small>
            </span>
            <em>{status}</em>
          </article>
        ))}
      </div>
      <div className="lp-email-reading-pane">
        <article className="lp-email-card">
          <div>
            <span className="lp-email-avatar">{isOutlook ? "AM" : "CS"}</span>
            <span>
              <strong>
                {isOutlook
                  ? "Invoice exception review"
                  : "Refund exception request"}
              </strong>
              <small>Received 9:15 AM</small>
            </span>
          </div>
          <p>
            {isOutlook
              ? "Please check the attached invoice against our payment policy and flag anything that needs approval."
              : "Priority customer is asking for a one-time exception after unresolved implementation issues."}
          </p>
        </article>
        <div className="lp-surface-compose">
          <div>
            <Image src={surface.logos[0].src} alt="" width={24} height={24} />
            <strong>Lemma draft ready</strong>
          </div>
          <p>
            {isOutlook
              ? "I found one policy exception, drafted the approval note, and added it to Finance Review."
              : "The exception can be approved once, with a follow-up task opened for the implementation issue."}
          </p>
          <span>
            {isOutlook ? "Send reply in Outlook" : "Send reply in Gmail"}
          </span>
        </div>
        <div className="lp-email-sync-list" aria-hidden="true">
          {[
            ["approval.status", "waiting"],
            ["customer.record", "ready to update"],
            ["follow_up.owner", isOutlook ? "Finance" : "CSM"],
          ].map(([label, value]) => (
            <div key={label}>
              <span>{label}</span>
              <strong>{value}</strong>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export function SurfacePhoneContent({ surface }: { surface: SurfaceMode }) {
  const isWhatsApp = surface.key === "whatsapp";
  const messages = isWhatsApp
    ? [
        {
          from: "from-user",
          copy: "New lead crossed ICP threshold. Assign to Maya?",
        },
        {
          from: "from-pod",
          copy: "Matched the account and found Maya is owner.",
        },
        { from: "from-user", copy: "Yes. Assign and draft intro." },
        {
          from: "from-pod",
          copy: "Assigned. Draft saved for review.",
          card: ["Lead routed", "Maya owns next step"],
        },
      ]
    : [
        {
          from: "from-user",
          copy: "Pause campaign spend above the anomaly threshold.",
        },
        {
          from: "from-pod",
          copy: "Found Meta and GA4 campaigns. Two are above threshold.",
        },
        {
          from: "from-pod",
          copy: "Hold budget until Monday and notify finance?",
        },
        { from: "from-user", copy: "Approve hold until Monday." },
        {
          from: "from-pod",
          copy: "Done. Campaigns paused, Finance logged, dashboard updated.",
        },
      ];

  return (
    <div
      className={
        isWhatsApp ? "lp-phone-shell is-whatsapp" : "lp-phone-shell is-telegram"
      }
    >
      <div className="lp-phone-status" aria-hidden="true">
        <span>9:41</span>
        <span>
          <i />
          <i />
          <i />
        </span>
      </div>
      <header className="lp-phone-header">
        <span aria-hidden="true">{"<"}</span>
        <span className="lp-phone-pod-avatar">
          <Image
            src={surface.logos[0].src}
            alt={surface.logos[0].label}
            width={28}
            height={28}
          />
        </span>
        <span className="lp-phone-title">
          <strong>
            {isWhatsApp ? "Sales Pod" : "Executive Assistant Pod"}
          </strong>
          <small>{isWhatsApp ? "Lemma app" : "online"}</small>
        </span>
        {isWhatsApp ? (
          <>
            <i aria-hidden="true" />
            <i aria-hidden="true" />
          </>
        ) : null}
        <span className="lp-phone-menu" aria-hidden="true">
          <i />
          <i />
          <i />
        </span>
      </header>
      <main className="lp-phone-thread">
        <span className="lp-chat-date">Today</span>
        {messages.map((message, index) => (
          <article
            className={`lp-phone-message ${message.from} is-step-${index + 1}`}
            key={message.copy}
          >
            {message.from === "from-pod" ? (
              <span className="lp-phone-mini-avatar">Le</span>
            ) : null}
            <p>
              {message.copy}
              {message.card ? (
                <span className="lp-phone-task-card">
                  <strong>{message.card[0]}</strong>
                  <small>{message.card[1]}</small>
                </span>
              ) : null}
              <span className="lp-phone-time">
                9:{String(15 + index).padStart(2, "0")} AM
                {message.from === "from-user" ? (
                  <i className="lp-phone-check" aria-hidden="true" />
                ) : null}
              </span>
            </p>
          </article>
        ))}
        <span className="lp-phone-typing" aria-hidden="true">
          <i />
          <i />
          <i />
        </span>
      </main>
      <footer className="lp-phone-input" aria-hidden="true">
        <span>
          <i>{isWhatsApp ? "+" : "@"}</i>
          Message
        </span>
        <strong>{isWhatsApp ? "m" : ">"}</strong>
      </footer>
    </div>
  );
}

export function SurfaceApiContent() {
  return (
    <div className="lp-api-surface">
      <div className="lp-api-call">
        <span>POST</span>
        <strong>/pods/support-ops/workflows/refund-review/run</strong>
      </div>
      <pre aria-label="API request body">
        <code>
          {
            '{\n  "customer_id": "cus_82914",\n  "amount": 420,\n  "channel": "app"\n}'
          }
        </code>
      </pre>
      {[
        ["input.customer_id", "cus_82914"],
        ["workflow.status", "waiting_for_approval"],
        ["agent.draft_reply", "ready"],
        ["table.customers.updated", "true"],
      ].map(([key, value]) => (
        <div className="lp-api-row" key={key}>
          <span>{key}</span>
          <strong>{value}</strong>
        </div>
      ))}
    </div>
  );
}
