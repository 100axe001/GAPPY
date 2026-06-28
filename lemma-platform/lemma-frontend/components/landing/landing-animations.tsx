import { useEffect, useRef, useState } from "react";
import type { TerminalLine } from "./landing-data";
import {
  fullTerminalLines,
  heroTickerEvents,
  machineStations,
  podBlocks,
  terminalScript,
} from "./landing-data";

export function PodBlockGlyph({ kind }: { kind: (typeof podBlocks)[number]["key"] }) {
  switch (kind) {
    case "data":
      return (
        <svg viewBox="0 0 28 28" className="lp-glyph lp-glyph-data">
          <rect className="lp-g-row" x="4" y="6" width="20" height="3.4" rx="1.4" />
          <rect className="lp-g-row" x="4" y="12.3" width="15" height="3.4" rx="1.4" />
          <rect className="lp-g-row" x="4" y="18.6" width="18" height="3.4" rx="1.4" />
        </svg>
      );
    case "agents":
      return (
        <svg viewBox="0 0 28 28" className="lp-glyph lp-glyph-agents">
          <line className="lp-g-edge" x1="6.5" y1="20" x2="14" y2="8" />
          <line className="lp-g-edge" x1="14" y1="8" x2="21.5" y2="18" />
          <line className="lp-g-edge" x1="6.5" y1="20" x2="21.5" y2="18" />
          <circle className="lp-g-node" cx="6.5" cy="20" r="2.8" />
          <circle className="lp-g-node is-gold" cx="14" cy="8" r="3.2" />
          <circle className="lp-g-node" cx="21.5" cy="18" r="2.8" />
        </svg>
      );
    case "workflows":
      return (
        <svg viewBox="0 0 28 28" className="lp-glyph lp-glyph-workflows">
          <line className="lp-g-edge" x1="5" y1="14" x2="23" y2="14" />
          <circle className="lp-g-node" cx="5" cy="14" r="2.5" />
          <rect
            className="lp-g-gate"
            x="11.2"
            y="11.2"
            width="5.6"
            height="5.6"
          />
          <circle className="lp-g-node" cx="23" cy="14" r="2.5" />
          <circle className="lp-g-packet" cx="0" cy="14" r="1.9" />
        </svg>
      );
    case "apps":
      return (
        <svg viewBox="0 0 28 28" className="lp-glyph lp-glyph-apps">
          <rect className="lp-g-frame" x="4" y="5" width="20" height="18" rx="2.4" />
          <line className="lp-g-edge" x1="4" y1="10" x2="24" y2="10" />
          <rect className="lp-g-bar" x="8" y="13.5" width="2.8" height="6" rx="1" />
          <rect className="lp-g-bar" x="12.6" y="13.5" width="2.8" height="6" rx="1" />
          <rect className="lp-g-bar" x="17.2" y="13.5" width="2.8" height="6" rx="1" />
        </svg>
      );
    case "access":
      return (
        <svg viewBox="0 0 28 28" className="lp-glyph lp-glyph-access">
          <path
            className="lp-g-frame"
            d="M14 4.2l7.6 2.9v5.7c0 4.8-3.2 8.2-7.6 9.8-4.4-1.6-7.6-5-7.6-9.8V7.1z"
          />
          <circle className="lp-g-dot" cx="14" cy="13.4" r="2.2" />
        </svg>
      );
    case "connectors":
      return (
        <svg viewBox="0 0 28 28" className="lp-glyph lp-glyph-connectors">
          <line className="lp-g-edge" x1="14" y1="14" x2="14" y2="5.5" />
          <line className="lp-g-edge" x1="14" y1="14" x2="22.5" y2="14" />
          <line className="lp-g-edge" x1="14" y1="14" x2="14" y2="22.5" />
          <line className="lp-g-edge" x1="14" y1="14" x2="5.5" y2="14" />
          <circle className="lp-g-frame" cx="14" cy="14" r="3.1" />
          <circle className="lp-g-sat" cx="14" cy="5.5" r="1.9" />
          <circle className="lp-g-sat" cx="22.5" cy="14" r="1.9" />
          <circle className="lp-g-sat" cx="14" cy="22.5" r="1.9" />
          <circle className="lp-g-sat" cx="5.5" cy="14" r="1.9" />
        </svg>
      );
  }
}

export function MachineStationIcon({
  kind,
}: {
  kind: (typeof machineStations)[number]["key"];
}) {
  switch (kind) {
    case "inbound":
      return (
        <svg viewBox="0 0 24 24">
          <rect x="3.5" y="5.5" width="17" height="13" rx="2" />
          <path d="M4.5 7l7.5 6 7.5-6" />
        </svg>
      );
    case "agent":
      return (
        <svg viewBox="0 0 24 24">
          <path d="M12 3l7.5 4.4v8.2L12 20l-7.5-4.4V7.4z" />
          <circle cx="12" cy="11.5" r="2.4" />
        </svg>
      );
    case "table":
      return (
        <svg viewBox="0 0 24 24">
          <rect x="3.5" y="4.5" width="17" height="15" rx="2" />
          <line x1="3.5" y1="10" x2="20.5" y2="10" />
          <line x1="3.5" y1="14.5" x2="20.5" y2="14.5" />
          <line x1="10" y1="10" x2="10" y2="19.5" />
        </svg>
      );
    case "approval":
      return (
        <svg viewBox="0 0 24 24">
          <circle cx="12" cy="8.5" r="3.4" />
          <path d="M5 20c.8-3.6 3.6-5.5 7-5.5s6.2 1.9 7 5.5" />
        </svg>
      );
    case "routed":
      return (
        <svg viewBox="0 0 24 24">
          <circle cx="6" cy="12" r="2.4" />
          <circle cx="18" cy="6.5" r="2.4" />
          <circle cx="18" cy="17.5" r="2.4" />
          <line x1="8" y1="11" x2="15.8" y2="7.4" />
          <line x1="8" y1="13" x2="15.8" y2="16.6" />
        </svg>
      );
  }
}

export function MachineAtWork() {
  const wrapRef = useRef<HTMLDivElement>(null);
  const fillRef = useRef<HTMLDivElement>(null);
  const packetRef = useRef<HTMLDivElement>(null);
  const readoutRef = useRef<HTMLSpanElement>(null);
  const stationRefs = useRef<(HTMLDivElement | null)[]>([]);
  const [isStatic, setIsStatic] = useState(false);

  useEffect(() => {
    const reduced = window.matchMedia("(prefers-reduced-motion: reduce)");
    const narrow = window.matchMedia("(max-width: 860px)");
    const sync = () => setIsStatic(reduced.matches || narrow.matches);
    sync();
    reduced.addEventListener("change", sync);
    narrow.addEventListener("change", sync);
    return () => {
      reduced.removeEventListener("change", sync);
      narrow.removeEventListener("change", sync);
    };
  }, []);

  useEffect(() => {
    if (isStatic) return;
    let ticking = false;
    const update = () => {
      ticking = false;
      const wrap = wrapRef.current;
      if (!wrap) return;
      const total = wrap.offsetHeight - window.innerHeight;
      if (total <= 0) return;
      const progress = Math.min(
        1,
        Math.max(0, -wrap.getBoundingClientRect().top / total),
      );
      if (fillRef.current)
        fillRef.current.style.width = `${progress * 100}%`;
      if (packetRef.current)
        packetRef.current.style.left = `${progress * 100}%`;
      let lit = 0;
      stationRefs.current.forEach((station, index) => {
        if (!station) return;
        const threshold = index / (machineStations.length - 1);
        const isLit = progress >= threshold - 0.02;
        station.classList.toggle("is-lit", isLit);
        if (isLit) lit = index + 1;
      });
      if (readoutRef.current)
        readoutRef.current.textContent = `WORK://NORTHWIND :: 0${lit}/05 COMPLETE`;
    };
    const onScroll = () => {
      if (!ticking) {
        ticking = true;
        requestAnimationFrame(update);
      }
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", onScroll, { passive: true });
    update();
    return () => {
      window.removeEventListener("scroll", onScroll);
      window.removeEventListener("resize", onScroll);
    };
  }, [isStatic]);

  return (
    <section
      className={`lp-mw-section${isStatic ? " is-static" : ""}`}
      id="runtime"
      aria-labelledby="mw-title"
    >
      <div className="lp-mw-wrap" ref={wrapRef}>
        <div className="lp-mw-sticky">
          <div className="lp-section-inner">
            <div className="lp-mw-head lp-reveal">
              <div>
                <p className="lp-section-kicker">Runtime</p>
                <h2 className="lp-section-title" id="mw-title">
                  Watch one unit of work <span>move.</span>
                </h2>
                <p className="lp-section-subhead">
                  Not a chat transcript. A piece of work with an owner and
                  state, moving through agents, tables, and people.
                </p>
              </div>
              <span className="lp-mw-readout" ref={readoutRef}>
                WORK://NORTHWIND :: 00/05 COMPLETE
              </span>
            </div>

            <div className="lp-mw-stage">
              <div className="lp-mw-track" aria-hidden="true">
                <div className="lp-mw-fill" ref={fillRef} />
                <div className="lp-mw-packet" ref={packetRef} />
              </div>
              <div className="lp-mw-stations">
                {machineStations.map((station, index) => (
                  <div
                    className="lp-mw-station"
                    key={station.key}
                    ref={(el) => {
                      stationRefs.current[index] = el;
                    }}
                  >
                    <span className="lp-mw-chip" aria-hidden="true">
                      <MachineStationIcon kind={station.key} />
                    </span>
                    <span className="lp-mw-label">{station.label}</span>
                    <span className="lp-mw-sub">{station.sub}</span>
                    <p className="lp-mw-caption">{station.caption}</p>
                    {station.key === "approval" ? (
                      <span className="lp-mw-approval">
                        <strong>Route Northwind to enterprise?</strong>
                        <em>Approved by Dana</em>
                      </span>
                    ) : null}
                  </div>
                ))}
              </div>
            </div>

            <p className="lp-mw-coda">
              The pause at ST/04 was Dana clicking Approve in Slack. Every
              other step ran itself.
            </p>
          </div>
        </div>
      </div>
    </section>
  );
}

export function HeroTicker() {
  const [eventIndex, setEventIndex] = useState(0);

  useEffect(() => {
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    const id = setInterval(
      () => setEventIndex((current) => (current + 1) % heroTickerEvents.length),
      2600,
    );
    return () => clearInterval(id);
  }, []);

  return (
    <p className="lp-hero-ticker" aria-hidden="true">
      <i className="lp-ticker-dot" />
      <span className="lp-ticker-text" key={eventIndex}>
        {heroTickerEvents[eventIndex]}
      </span>
    </p>
  );
}

export function TypingTerminal() {
  const [lines, setLines] = useState<TerminalLine[]>([]);
  const [typed, setTyped] = useState<string | null>(null);
  const [isDone, setIsDone] = useState(false);
  const preRef = useRef<HTMLPreElement>(null);

  useEffect(() => {
    const pre = preRef.current;
    if (!pre) return;

    let cancelled = false;
    const timeouts: ReturnType<typeof setTimeout>[] = [];
    const wait = (ms: number) =>
      new Promise<void>((resolve) => {
        timeouts.push(setTimeout(resolve, ms));
      });

    const run = async () => {
      for (const step of terminalScript) {
        setTyped("");
        for (let i = 1; i <= step.command.length; i += 1) {
          await wait(24);
          if (cancelled) return;
          setTyped(step.command.slice(0, i));
        }
        await wait(260);
        if (cancelled) return;
        setTyped(null);
        setLines((current) => [
          ...current,
          { kind: "command", text: step.command },
        ]);
        for (const text of step.output) {
          await wait(90);
          if (cancelled) return;
          setLines((current) => [...current, { kind: "output", text }]);
        }
        await wait(320);
        if (cancelled) return;
      }
      setIsDone(true);
    };

    const observer = new IntersectionObserver(
      (entries) => {
        if (entries.some((entry) => entry.isIntersecting)) {
          observer.disconnect();
          if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
            setLines(fullTerminalLines);
            setIsDone(true);
            return;
          }
          void run();
        }
      },
      { threshold: 0.4 },
    );
    observer.observe(pre);
    return () => {
      cancelled = true;
      observer.disconnect();
      for (const timeout of timeouts) clearTimeout(timeout);
    };
  }, []);

  return (
    <pre ref={preRef} aria-label="Quickstart terminal session">
      <code>
        {lines.map((line, index) => (
          <span className="lp-term-line" key={`${line.text}-${index}`}>
            {line.kind === "command" ? (
              <>
                <span>$</span> {line.text}
              </>
            ) : (
              line.text
            )}
            {"\n"}
          </span>
        ))}
        {typed !== null ? (
          <span className="lp-term-line">
            <span>$</span> {typed}
            <i className="lp-term-cursor" aria-hidden="true" />
          </span>
        ) : null}
        {isDone ? <i className="lp-term-cursor" aria-hidden="true" /> : null}
      </code>
    </pre>
  );
}
